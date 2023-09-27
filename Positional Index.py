import numpy as np
n=int(input("Enter number of files :"))
x=[]
for i in range(n):
    name=input("Enter file {}".format(i+1))
    f=open(name,'r').read().split()
    print("Doc {} : {}".format(i+1,f))
    x.append(f)
y=sorted(set(sum(x,[])))
print(y)
d={}
for i in y:
    m=[]
    for j in range(n):
        l=[]
        if i in x[j]:
            l.append(s[j])
            ind=[]
            for k in range(len(x[j])):
                if i==x[j][k]:
                    ind.append(k)
            m.append([l[0],ind])    
    d[i]=m
print(d)
query=input("Enter a phrase :").split()
t=[]
for i in query:
    t.append(d[i])
r=[] #list of documents for each word in phrase
q=[] # indexes for r 
for i in t:
    r1=[]
    q1=[]
    for j in i:
        r1.append(j[0])
        q1.append(j[1])
    r.append(r1)
    q.append(q1)
sl=list(set(r[0]).intersection(set(r[1])))
res=[]
for i in sl:
    ind1=r[0].index(i)
    ind2=r[1].index(i)
    for j in q[0][ind1]:
        for k in q[1][ind2]:
            if j+1==k:
                res.append(i)
print(res)
