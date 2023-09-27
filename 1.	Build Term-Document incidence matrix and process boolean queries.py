n=int(input("enter the no of documents"))
terms=[]
fname=[]
for i in range(n):
    name=input("enter the name of file")
    fname.append(name)
    f=open(name).read()
    terms.append(list(set(f.split())))  #extracting without duplicates from each file and keep in terms list
    print(f)

#exact specifies set of terms in combination of all files
exact=set(terms[0])
for i in range(1,n):
    exact=(set(exact)|set(terms[i]))
exact=list(exact)

#tdm specifies term document matrix
tdm=[[0 for i in range(n)] for j in range(len(exact))]
for i in range(len(exact)):
    for j in range(n):
        if(exact[i] in terms[j]):
            tdm[i][j]=1
for i in range(len(tdm)):
    print(exact[i],' : ',tdm[i])


def NOT(l):
    for i in range(len(l)):
        if l[i]==1:
            l[i]=0
        else:
            l[i]=1
    return l
def AND(l1,l2):
    return list(set(l1) & set(l2));
def OR(l1,l2):
    return list(set(l1) | set(l2));

#taking query as input
print('Note:Enter the string with spaces after each word,paranthesis  ')
s=input()
qt=s.split()                  # splitting at spaces


#replacing the text with their boolean values
for i in range(len(qt)):
    if qt[i] not in(['and','or','not','(',')']):
        index=exact.index(qt[i])
        qt[i]=tdm[index]

print('changing the string to boolean form = ',qt)

post=[]
st=[]
def precedency(c):
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

print(qt)
for i in range(len(qt)):
    s=qt[i]
    if( s==')'):
        s1=pop()
        while(s1!='('):
            post.append(s1)
            s1=pop()
    if(s in ['and','or','not','(']):
        while(s!='(' and precedency(s)<=precedency(peak())):
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
        c.append(NOT(n1))
    else:
        c.append(post[i])

r=c[0]
print(r)
count=0
for i in r:
    if(i==1):
        print(fname[count])
    count=count+1
if(count==0):
    print('no documents found')
