import urllib.request
import pandas as pd
urllib.request.urlretrieve("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/hospitalizations/covid-hospitalizations.csv", "/tmp/covid-hospitalizations.csv")
# read from /tmp, subset for USA, pivot and fill missing values
df = pd.read_csv("/tmp/covid-hospitalizations.csv")
df = df[df.iso_code == 'USA']\
     .pivot_table(values='value', columns='indicator', index='date')\
     .fillna(0)
clean_cols = df.columns.str.replace(' ', '_')
df.columns = clean_cols
df['date'] = df.index
# print the transformed data
print(df)