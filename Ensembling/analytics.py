import pandas as pd
import random
import statistics

data = pd.read_csv('data.csv')
Y = data.iloc[:,0:1]
data = data.iloc[:,1:]

maxacc=0
final=[]
for i in range (0,1000):
    a=random.randint(1,5)
    n=(2*a) - 1
    X = data.sample(n, axis=1)
    count = 0
    j=0
    for j in range (0,6):
        mod=statistics.mode(X.iloc[j,0:n])
        lol = [int(i) for i in Y.values]
        if lol[j] == mod:
            count = count + 1
        accuracy = (count/6)*100
        if accuracy == maxacc:
            b =list(X)
            str1 = ', '.join(b)
            final.append(str1)
        elif accuracy > maxacc:
            del final[:]
            b =list(X)
            str1 = ', '.join(b)
            final.append(str1)
            maxacc = accuracy

for x in range(len(final)): 
    print (final[x], " - ", maxacc)