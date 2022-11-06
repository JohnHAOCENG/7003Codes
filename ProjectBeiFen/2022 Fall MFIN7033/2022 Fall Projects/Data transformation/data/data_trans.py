import time
import numpy
import pandas as pd

start = time.time()


dataset = pd.read_csv('deal_level_data.csv')
# Rename all quarter data with new_cols, in order to create "quarter_to_the_event_date" col
# Using dic to pair values and rename the columns
old_cols = dataset.columns[14:39]
new_cols = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
col_dic = {}
for i in range(len(old_cols)):
    col_dic[old_cols[i]] = new_cols[i]
dataset = dataset.rename(columns=col_dic)

# Using melt to change the quarter data from wide to long
deal_headers = dataset.iloc[:, 0:39]
output_1 = deal_headers.melt(id_vars=deal_headers.columns[0:14], var_name="quarter_to_the_event_date",
                             value_name="quarter")

# Extract com_cols and tar_cols from deals_data and rename them for quarter_data file to use
com_cols = list(map(lambda x: x.replace('Acq', 'Com').rstrip('__12'), list(dataset.columns)[39:49]))
tar_cols = list(map(lambda x: x.rstrip('__12'), list(dataset.columns)[289:299]))
all_quarter_cols = com_cols + tar_cols

new_quarter_cols = [i for i in range(-12, 13)]
quarter_cols_dic = {}

# index are the starting point of com_cols and tar_cols
for index in [39, 289]:
    for j in range(index, index + 10):

        # Extract all data of one specific col
        one_data_cols = dataset.columns[list(range(j, j + 241, 10))]

        # Rename all col names of the specific data, in order to do data merging
        for k in range(len(one_data_cols)):
            quarter_cols_dic[one_data_cols[k]] = new_quarter_cols[k]
        dataset = dataset.rename(columns=quarter_cols_dic)

        # Using index to locate the respect col names in all_quarter_cols, 39 for com_cols, 279 for tar_cols
        # Using melt function to convert columns to rows for all data of the specific col
        if index == 39:
            row_data = dataset.iloc[:, (list(range(j, j + 241, 10)) + list([0]))].melt(id_vars='Deal_Number',
                                                                                       var_name='quarter_to_the_event_date',
                                                                                       value_name=all_quarter_cols[
                                                                                           j-39])
        else:
            row_data = dataset.iloc[:, (list(range(j, j + 241, 10)) + list([0]))].melt(id_vars='Deal_Number',
                                                                                       var_name='quarter_to_the_event_date',
                                                                                       value_name=all_quarter_cols[
                                                                                       j-279])
        # Merge all data of the specific col with output_1 based on  "Deal_Number" and ‘quarter_to_the_event_date"
        output_1 = pd.merge(output_1, row_data, on=["Deal_Number", "quarter_to_the_event_date"])

# Adding the log_cols for quarter data, by calculating it from the current cols
for i in ['Com_AvgSalary', 'Com_EmployNum', 'Com_TtlSalary',
          'Tar_AvgSalary', 'Tar_EmployNum', 'Tar_TtlSalary']:
    output_1[(i + '_log')] = numpy.log(output_1[i])

# Sort the rows, first based on Deal_Number, then by quarter_to_the_event_date
output = output_1.sort_values(["Deal_Number", "quarter_to_the_event_date"])

# Rearrange the columns orders, by pop and insert
Com_Total_Assets = output.pop("Com_Total_Assets")
Tar_Total_Assets = output.pop("Tar_Total_Assets")
Com_AvgSalary_log = output.pop("Com_AvgSalary_log")
Com_EmployNum_log = output.pop("Com_EmployNum_log")
Com_TtlSalary_log = output.pop("Com_TtlSalary_log")
output.insert(22, "Com_Total_Assets", Com_Total_Assets)
output.insert(32, "Tar_Total_Assets", Tar_Total_Assets)
output.insert(26, "Com_AvgSalary_log", Com_AvgSalary_log)
output.insert(27, "Com_EmployNum_log", Com_EmployNum_log)
output.insert(28, "Com_TtlSalary_log", Com_TtlSalary_log)

# Output the quarter data
output.to_csv('output.csv', index=False)

print("Running time: " + str(time.time() - start))
