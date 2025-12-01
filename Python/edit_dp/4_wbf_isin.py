import glob
import pandas as pd
import csv

finding_dp_file = glob.glob("DP*")

# Read the CSV
df = pd.read_csv(*finding_dp_file,dtype=str)

# --- Replace ISIN Numbers ---
df['ISIN Number'] = df['ISIN Number'].replace({
    'INE838A01015': 'DUMMYSAN005',
    'INE119J01011': 'DUMMYSAN006',
    'INE312K01010': 'DUMMYSAN007',
    'INE721I01024': 'DUMMYSAN008'
})

# --- Modify Open Authorize Quantity ---
fixed_codes = {"UP1228", "UP1227"}

df.loc[
    df["Client"].isin(fixed_codes) | df["Client"].str.startswith("WBF"),
    "Open Authorize Quantity"
] = 0

# Save output file
df.to_csv(
    *finding_dp_file,
     index=False,
     quoting=csv.QUOTE_MINIMAL,
     escapechar='\\',
     lineterminator="\r\n"
     
     )
