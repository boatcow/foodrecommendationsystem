from flask import Flask, render_template, url_for, request, redirect
import pandas as pd
from collections import Counter
import math
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])


def index():
    if request.method == 'POST' and request.form['content']!="":
        df = pd.read_csv('foodtestg.csv')
        Diet="v"
        task_content = request.form['content']
        listB=list(task_content.split(","))
        Diet=str(listB[0])
        Diet=Diet[0]
        print("LOOOOOOOOOOOOOL"+str(Diet))


        if(len(listB)<=1):
            l="enter valid input"
            print("oooooooo"+str(len(listB)))
            return render_template('index.html',food=l)
        if(Diet!="n" and Diet!="v"):
            l="wtf"
            print("enter valid input ffs"+str(len(listB)))
            return render_template('index.html',food=l)
            
        listB=listB[1:]
        Diet=Diet[0]
        df = df[df["diet"]==Diet]

        #listB=[carrot,beans,capsicum]#ingredients from user (user input 2)
        l=len(df.index)

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
        l=str(df.iloc[0]["foodname"])

        try:
            return render_template('index.html',food=l)
        except:
            return str(l)

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


