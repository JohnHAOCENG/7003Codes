import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

df_raw = pd.read_csv("11.5Q5.csv")

df_data = df_raw[['gvkey', 'cusip', 'fyear', 'ni', 'at', 'revt', 'add1', 'city', 'state']]

df_data['roa'] = df_data['ni']/df_data['at']

df_data_roa_not_pos = df_data[((df_data['roa']).isnull()|(df_data['roa'] <= 0)) & (df_data['fyear'] == 2010)]

firm_roa_not_pos = df_data_roa_not_pos.cusip.tolist()

df_data_final = df_data[~df_data.cusip.isin(firm_roa_not_pos)]

print(df_data_final)