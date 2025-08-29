# -*- coding: utf-8 -*-
"""
Apriori Market Basket Analysis - Python Script
"""

import pandas as pd
from apyori import apriori
import csv

# Load CSV file
df = pd.read_csv("Market_Basket_Optimisation.csv")  # Replace with your CSV path

# Convert all values to strings and replace NaN with 'nan'
df = df.fillna('nan').astype(str)

# Convert DataFrame rows to a list of transactions
transactions = df.values.tolist()
transactions = [[item for item in transaction if item != 'nan'] for transaction in transactions]

# Apply Apriori algorithm
association_rules = apriori(transactions, min_support=0.05, min_confidence=0.1, min_lift=1)
association_results = list(association_rules)

# Prepare results to save in CSV
output_rows = []
for item in association_results:
    items = set(item.items)
    if len(items) > 1:
        for rule in item.ordered_statistics:
            if rule.items_base and rule.items_add:
                output_rows.append([
                    ', '.join(rule.items_base),
                    ', '.join(rule.items_add),
                    item.support,
                    rule.confidence,
                    rule.lift
                ])

# Save results to CSV
with open("association_rules.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Base Item(s)", "A]()
