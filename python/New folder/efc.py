import openpyxl as op
import pandas as pd
# from openpyxl.utils.dataframe import dataframe_to_rows

firstfile = op.load_workbook('e_pi.xlsx')
firstws = firstfile.active
df1 = pd.DataFrame(firstws.values)

secondfile = op.load_workbook('e_pi2.xlsx')
secondws = secondfile.active
df2 = pd.DataFrame(secondws.values)

# df1.compare(df2)

df = pd.concat(df1, df2)
df = df.reset_index(drop=True)
df_gpby = df.groupby(list(df.columns))

idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]
df.reindex(idx)
