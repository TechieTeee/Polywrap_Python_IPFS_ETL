import csv
import pandas as pd
from polywrap_core import Uri, ClientConfig
from polywrap_client import PolywrapClient
from polywrap_client_config_builder import PolywrapClientConfigBuilder
from polywrap_sys_config_bundle import sys_bundle
from polywrap_web3_config_bundle import web3_bundle

def main():
    # Configure and instantiate the client
    builder = (
        PolywrapClientConfigBuilder()
        .add_bundle(sys_bundle)
        .add_bundle(web3_bundle)
    )
    config = builder.build()
    client = PolywrapClient(config)

    # Read the data from the CSV file
    with open("ETH-USD.csv", "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    # Create a pandas dataframe from the data
    df = pd.DataFrame(data, columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])

    # Convert the Date column to a numeric column
    df["Date"] = pd.to_datetime(df["Date"])

    # Calculate the moving average for each price column
    for column in ["Open", "High", "Low", "Close"]:
        df["MA_" + column] = df[column].rolling(window=10).mean()

    # Use the Polywrap client to invoke the wrapper to look for trends in the data
    uri = Uri.from_str(
        'wrapscan.io/polywrap/trend-detection'
    )
    args = {
        "data": df.to_json(),
    }
    result = client.invoke(uri=uri, method="detect", args=args, encode_result=False)

    # Print the results
    print(result)


if __name__ == "__main__":
    main()