import pandas as pd
df = pd.DataFrame(columns=list('A'))
df.loc[0] = ['Hello']
print (df)
