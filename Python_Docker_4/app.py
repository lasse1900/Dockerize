import pandas as pd
df = pd.read_csv("SampleCSVFile.csv",encoding='latin1')
print(df.head(1000))