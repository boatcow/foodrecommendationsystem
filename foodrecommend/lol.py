import pandas as pd
from collections import Counter
import math
df = pd.read_csv('foodtestg.csv')
Diet="v"#vegetarian diet(user input 1)
df = df[df["diet"]==Diet]
k=df.iloc[2]["ingredients"]
listA=list(k.split(","))
listB=["carrot","beans","capsicum"]#ingredients from user (user input 2)
l=len(df.index)
counterA = Counter(listA)
counterB = Counter(listB)
def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)
counterB = Counter(listB)
m=0
l1=[]
for i in range(l):
  k=df.iloc[i]["ingredients"]
  listA=list(k.split(","))
  counterA = Counter(listA)
  v=counter_cosine_similarity(counterA, counterB)
  l1.append(v)
m=max(l1)
df["score"]=l1
df=df[df["score"]==m]
df[df["nutritional info"]==df["nutritional info"].min()]
print(df.iloc[0]["foodname"])
