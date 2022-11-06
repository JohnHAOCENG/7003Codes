import pandas as pd
from fuzzywuzzy import fuzz
from joblib import Parallel, delayed

# Read the excel and csv
acq_data = pd.read_excel("acquirers.xlsx")
banks_data = pd.read_csv("bank_names.csv", index_col=0)

# For each acquier firm, find all similar ratio of it, and store the top similar 5 banks to the list
def fuzzy_match(acquier):
    match_lst = []
    for bank in banks_data.bank_names:
        ratio = fuzz.ratio(bank.upper(), acquier.upper())
        match_lst.append((ratio, bank))
    return sorted(match_lst, key=lambda tup: tup[0], reverse=True)[:5]

# Using parallel to assign 50 acquier concurrently
all_matched_lst = Parallel(n_jobs=50)(delayed(fuzzy_match)(x) for x in acq_data["Acquirer Name"])

# Create a new pd to store these values based on the output format requirement
output = pd.DataFrame({"acquirers": acq_data["Acquirer Name"]})
for index in range(0,5):
    output[str(index)] = [i[index][1] for i in all_matched_lst]

# Convert to csv
output.to_csv("output.csv")