def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def mull(x,y):
    return(x*y)
def div(x,y):
    return(x/y)
if __name__=="__main__":
 print("Enter statment")
 a=input()
def predict(a):
 m={}
 p=0
#print(type(m))
 for b in a:
     if(b.isdigit()):
         m[p]=int(b)
         #print(m[p])
         p=p+1
 p=0

 if  (a.find("sum")!=-1 or a.find("add")!=-1 or a.find('+')!=-1  or a.find("pluse")!=-1):
        k=add(m[p],m[p+1])
        o="sum of {} & {} is {}"
        t=o.format(m[p],m[p+1],k)

 elif (a.find("sub")!=-1 or a.find("substract")!=-1 or a.find('-')!=-1 or a.find("minus")!=-1):
        k=sub(m[p],m[p+1])
        o = "substraction of {} & {} is {}"
        t = o.format(m[p], m[p + 1], k)

 elif  (a.find("divide")!=-1 or a.find("by")!=-1 or a.find('/')!=-1):
        k=div(m[p],m[p+1])
        o = "division of {} & {} is {}"
        t = o.format(m[p], m[p + 1], k)
 elif (a.find("product")!=-1 or (a.find("multiply")!=-1 or a.find('mul')!=-1) or a.find('*')!=-1  or a.find('into')!=-1):
         k=mull(m[p],m[p+1])
         o = "product of {} & {} is {}"
         t = o.format(m[p], m[p + 1], k)
 else:
     t="You gave wrong input"

 return t