import pandas as pd
import random

data = pd.read_csv('data.csv')
Y = data.iloc[:,0:1]

data = data.iloc[:,1:]
a=len(data.columns)
Y = [int(i) for i in Y.values]
b=len(Y)
#minacc = 999999999999999
dic = {}
for i in range (0,1000):
    w =[]
    for j in range (0,a):
        wr= random.randint(-10,10)
        wr=wr/10
        w.append(wr)
    s = 0
    sum = 0
    for j in range(0,b):
        X=data.iloc[j,0:a]
        X = [int(i) for i in X.values]
        for k in range (0,a):
            s= s+ ( w[k] * X[k] )
        
        sum = sum  + abs(Y[j]-s)
    dic[sum] = w 
    
d = min(list(dic.keys()))
column = list(data.head(0))
print ('Required Equation is \n')
print ('Y =', end='')
for i in range (len(dic[d])):
    print (dic[d][i],column[i], '   ', end='')


"""
import pandas as pd
import random

data = pd.read_csv('data.csv')
Y = data.iloc[:,0:1]

data = data.iloc[:,1:]
a=len(data.columns)
Y = [int(i) for i in Y.values]
b=len(Y)
minacc = 999999999999999

for i in range (0,10000):
    w =[]
    for j in range (0,a):
        wr= random.randint(-10,10)
        wr=wr/10
        w.append(wr)
    s = 0
    sum = 0
    for j in range(0,b):
        X=data.iloc[j,0:a]
        X = [int(i) for i in X.values]
        for k in range (0,a):
            s= s+ ( w[k] * X[k] )
        
        sum = sum  + abs(Y[j]-s)
        
    if sum < minacc:
        minacc = sum
        variables = w
        
column = list(data.head(0))
print ('Required Equation is \n')
print ('Y =', end='')
for i in range (len(variables)):
    print (variables[i],column[i], '   ', end='')
"""