import pandas as pd

df1=pd.read_csv("/home/adil/tensorflow-for-poets-2/test/some.csv")
df2 = pd.read_csv("/home/adil/tensorflow-for-poets-2/test/some1.csv")
result = pd.concat([df1, df4], axis=1)
print (result)
