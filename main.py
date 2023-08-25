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

    # Use the Polywrap client to invoke the IPFS wrapper to retrieve data
    uri = Uri.from_str('wrapscan.io/polywrap/ipfs-http-client')  # Updated URI
    args = {
        "cid": "QmW54fYzbsYbgbu2rhShauWEKgjjkS1keecTncp24L4DLu",  # Uploaded CSV file's CID with ETH USD data
        "ipfsProvider": "https://ipfs.io",
    }
    result = client.invoke(uri=uri, method="cat", args=args, encode_result=False)

    # Decode the retrieved data from bytes to string
    retrieved_data = result.decode('utf-8')

    # Convert the retrieved data to a DataFrame
    df = pd.read_csv(pd.compat.StringIO(retrieved_data))

    # Perform necessary transformations and calculations on the DataFrame
    # Calculate moving averages for relevant columns
    for column in ["Open", "High", "Low", "Close"]:
        df["MA_" + column] = df[column].rolling(window=10).mean()

    # Convert the DataFrame to JSON format
    processed_data_json = df.to_json()

    # Use the IPFS wrapper to upload the processed data to IPFS
    ipfs_uri = Uri.from_str('wrapscan.io/polywrap/ipfs-http-client')  # IPFS wrapper URI
    ipfs_args = {
        "data": processed_data_json,
        "ipfsProvider": "https://ipfs.io",
    }
    ipfs_result = client.invoke(uri=ipfs_uri, method="add", args=ipfs_args, encode_result=False)

    # Print the IPFS hash of the uploaded data
    print("Processed data uploaded to IPFS with hash:", ipfs_result.decode('utf-8'))

if __name__ == "__main__":
    main()

