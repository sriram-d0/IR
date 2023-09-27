n=int(input("Enter no.of documents"))
terms=[]
fname=[]
for i in range(n):
    name=input("enter the name of file")
    fname.append(name)
    f=open(name).read()
    print(f)
    f=f.split()
    l=[]
    for i in range(len(f)-1):
        v=f[i]+' '+f[i+1]
        l.append(v)
        l.append(f[i])
    l.append(f[-1])
    terms.append(l)


exact=set(terms[0])

for i in range(1,len(terms)):
    exact=(set(exact)|set(terms[i]))

exact=list(exact)

d={}
for i in exact:
    d[i]=[]
    for j in range(n):
        if i in terms[j]:
            d[i].append(j)

for k in d.keys():
    print(k,' -- ',d[k])

def AND(l1,l2):
    return list(set(l1) & set(l2));
def OR(l1,l2):
    return list(set(l1) | set(l2));
def NOT(l1,n):
    l=[]
    for i in range(n):
        if i not in l1:
            l.append(i)
    return l;

s=input('enter the string')
l=s.split("'")
l1,qt=[],[]
for i in l:
    if i=='':
        continue
    if i.count(' ')>1:
        l1.append(i.split())
    elif i.count(' ')==1:
        l1.append(i)
for i in l1:
    if(type(i) !=list):
        qt.append(i)
    else:
        for j in i:
            qt.append(j)
print(qt)

for i in range(len(qt)):
    if qt[i] not in(['and','or','not','(',')']):
        qt[i]=d[qt[i]]

print(qt)
post=[]
st=[]
def precidency(c):
    if(c=='('): return 0;
    elif(c=='not'): return 3;
    elif(c=='and'): return 2;
    elif(c=='or'): return 1;
    else:return -1;

def push(e):
    st.append(e)

def pop():
    if len(st)==0:
        return -1
    t=st.pop()
    return t
def peak():
    if len(st)==0:
        return -1
    return st[len(st)-1]
for i in range(len(qt)):
    s=qt[i]
    if( s==')'):
        s1=pop()
        while(s1!='('):
            post.append(s1)
            s1=pop()
    if(s in ['and','or','not','(']):
        while(s!='(' and precidency(s)<=precidency(peak())):
            post.append(pop())
        push(s)
    if(s not in ['and','or','not','(',')']):
        post.append(s)
while(len(st)!=0):
    post.append(pop())
c=[]
for i in range(len(post)):
    if post[i]=='and':
        n1=c.pop()
        n2=c.pop()
        c.append(AND(n1,n2))
    elif post[i]=='or':
        n1=c.pop()
        n2=c.pop()
        c.append(OR(n1,n2))
    elif post[i]=='not':
        n1=c.pop()
        c.append(NOT(n1,n))
    else:
        c.append(post[i])
r=c[0]
for i in r:
    print(fname[i])
if(r==[]):
    print('no documents found')
