import polywrap

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

import pandas as pd

name = "main"

def group_transactions_by_association_rule_mining(data):
  """
  Group transactions together based on association rule mining.

  Args:
    data: The transaction data.

  Returns:
    A list of groups of transactions.
  """

  # Create a transaction encoder.
  encoder = TransactionEncoder()
  encoded_data = encoder.fit_transform(data)

  # Create a frequent itemset object.
  frequent_itemsets = apriori(encoded_data, min_support=0.05)

  # Create a dictionary of groups of transactions.
  groups = {}

  for itemset in frequent_itemsets:
    transactions = []

    for row in data:
      if all(item in row for item in itemset):
        transactions.append(row["transaction_id"])

    groups[itemset] = transactions

  return groups

binding = polywrap.create_binding(group_transactions_by_association_rule_mining)

def etl_pipeline():
  # Read the data from the CSV file.
  data = pd.read_csv("ETH-USD.csv")

  # Group transactions together based on association rule mining.
  groups = binding(data)

  # Print the groups.
  print(groups)

if name == "main":
  etl_pipeline()