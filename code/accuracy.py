from __future__ import division
import pandas as pd
import numpy as np

result = []
df = pd.read_csv('/home/adil/Image_classification/supporting_files/results/pre_result.csv' ,names = ['prediction','actual'])
#df.assign(output = [])
for i in range (len(df)):
    if df.iloc[i][0] == df.iloc[i][1]:
        #df.append(output)
        result.extend([1])
        #print ('1')
    else:
        result.extend([0])
        #print ('0')
#print(df.iloc[1][1])

se = pd.Series(result)
df['Output'] = se.values
print df
a = len(df)

b =  result.count(1)
acc = ((b/a)*100)
print ("Accuracy is =",acc)

df.to_csv('/home/adil/Image_classification/supporting_files/results/final_result.csv', sep='\t', encoding='utf-8')
