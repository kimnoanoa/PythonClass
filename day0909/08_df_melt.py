import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "Mary"],
    "City": ["New York", "Los Angeles"],
    "Age": [28, 32],
    "Salary": [50000, 60000],
})



print(df)
print()

df_melted = df.melt(id_vars=["Name","City"],
                    var_name="Attribute",
                    value_name="Value")

print(df_melted)
print()

df_melted2 = df.melt(id_vars="Name",
                    var_name="Attribute",
                    value_name="Value")

print(df_melted2)
print()

df_wide = pd.DataFrame({
    "Company": ["Google", "Yahoo"],
    "Income_2019": [100000, 50000],
    "Income_2020": [120000, 55000],
    "Expense_2019": [50000, 30000],
    "Expense_2020": [60000, 35000]
})

print(df_wide)
print()

df_long = pd.wide_to_long(df_wide, stubnames=['Income','Expense'],
                          i = 'Company',
                          j = 'Year',
                          sep='_',
                          suffix='\d+')

df_long = df_long.reset_index()
print(df_long)
print()

