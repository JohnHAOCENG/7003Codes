import pandas as pd

# Read the date csv and convert the "Date" col to datetime type
date_data = pd.read_csv("ukpound_exchange.csv", index_col=0)
date_data["Date"] = pd.to_datetime(date_data["Date"])

# Assign all same year same month date data into dic
dic = {}
for i in date_data["Date"]:
    if (str(i.year) + '- ' + str(i.month)) not in dic:
        dic[str(i.year) + '- ' + str(i.month)] = [i]
    else:
        dic[str(i.year) + '- ' + str(i.month)].append(i)

# Using max to extract the last date
last_date = [max(dic[key]) for key in dic]

# Loc the rows and output the data and reformat the datetime
last_date_data = (date_data.loc[date_data["Date"].isin(last_date)])

format_data = last_date_data["Date"].apply(lambda x: x.strftime('%d/%m/%Y'))
last_date_data.pop("Date")
last_date_data.insert(0,"Date",format_data)

# Outout the data
output = last_date_data.to_csv("output.csv")
