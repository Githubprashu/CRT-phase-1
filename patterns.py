"""for i in range(1,5):
    for j in range(1,5):
        print("*",end="")
    print("")"""



"""for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print("")"""



"""for i in range(1,6):
    for j in range(1,7-i):
        print("*",end="")
    print() """


"""r=5
for i in range(1,6):
    for s in range(1,r-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()   """



"""num=1
for i in range(1,5):
    for j in range(1,i+1):
        print(num,end="")
        num = num+1
    print()"""  

"""for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==4 or j==1 or j==4:
            print("*",end="")
        else:
            print(" ",end=+"")
    print"""


"""for i in range(1,12,2):
    print(i)"""


"""n=5
while n>0:
    print(n)"""


"""n=12467
while n>0:
    print(n%10)
    n=n//10"""

"""n=5
while n>0:
    print(n)
    n=n-1"""

"""n=12345
sum=0
while n>0:
    d=n%10
    sum=sum+d
    n=n//10
print(sum)"""
    

"""n=12345
count=0
while n>0:
   n=n//10
   count=count+1
print(count)  """ 
 

"""n=12345
c=0
while n>0:
    d=n%10
    if d%2==0:
        c=c+1
n=n//10
print(n)"""    

"""s=0
n=12
for i in range(1,n):
    if n%i==0:
        s=s+i
if s>n:
    print("true")
else:
    print("flase")"""

"""n=int(input(" n= "))
sum=0
n1=n
while n>0:
    d=n%10
    n=n//10
    sum=sum+d
if n1%sum==0:
    print("divisible")
else:
    print("not divisible")   """ 

"""n=int(input("n="))
num=0
n1=n
org=n
while n>0:
    n=n//10
    num=num+1
sum1=0    
while n1>0:
    d=n1%10
    sum1=sum1+d**num
    n1=n1//10
if sum1==org:
    print("yes")
else:
    print("no")"""  



 ## palindrom   


"""r=0
n=int(input("n="))
n1=n
while n>0:
    d=n%10
    r=r*10+d
    n=n//10
print(r)
if r==n1:
    print("palindrom")
else:
    print("not")""" 

##list


"""ourslist=["prasanth",30,"sridhar",4.56,True]
ourslist.append("teja")
ourslist.insert(2,"hari")
print(ourslist)
for i in ourslist:
    print(i)
for i in range(0,len(ourslist)):
    print(ourslist[i])
print(ourslist[1])
print(ourslist[:3])
print(ourslist[: :5])
ourslist[1]="nari"    
print(ourslist)"""


##tupples


"""tuple=("prasanth",80,50.6,"hari",False)
print(tuple)
print(type(tuple))
tuple=tuple+("teja",)
print(tuple)
tuple=tuple+(80,7.0,"teja")
print(tuple)
for i in range(0,5):
    n=int(input("enter n "))
    tuple=tuple+(n,)
    print(tuple)"""

"""list=[42,36,28,96,4,-1,1]
mini=999
maxi=-999
for i in range(0,len(list)):
    if list[i]<mini:
        mini=list[i]
    if list[i]>maxi:
        maxi=list[i]
print(mini+maxi)"""        
    

#distorany

"""dis={1:"a",
     2:"b",
     3:"c",
     "4":"d"
     }
dis[3]="e"
dis[5]="f"
print(dis)
print(dis[5])
for i in dis:
   print(i)
for i in dis.values():
    print(i)
for x,y in dis.item():
    print(x,y)
dis.pop(2)
print(dis)"""
   

##set

"""set={10,30,5,60}
print(set)
set.add(5)
print(set)
set.remove(30)
print(set)
set.update("prasanth")
print(set)
set.pop()
print(set)
set1={3,5,8,0}
set2=set.union(set1)
print(set2)
set2=set.intersection(set1)
print(set2)
print(set.difference(set1))"""

##function program (prime)


"""def prime():
    f=1    
    n=int(input( "enter n"))
    for i in range(2,n):
         if n%i==0:
           f=0
           break
    if f==0:
        print("not prime")
    else:
        print("prime")
prime()             """  


###orgements

"""def org(a,b,c):
    d=a+b+c
    print(d/3)
org(2,3,4)    """ 


"""n=1
def login():
    while n!=0:
       username=input("enter username name")
       password=input("enter password")
       if username==password:
           print("login sucessfully")
           break
       else:
           print("invild")
login()       """


##recursion
###factors

"""n=5
def f(n):
    if n==0:
        return 1
    return n*f(n-1)
a=f(5)
print(a)"""

##fabnocci series
"""n=10
def f(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return f(n-1)+f(n-2)
a=f(n)
print(a)"""

##POWER

"""def f(m,n):
    if m==0:
        return 1
    return n*p(n*m-1)
a"""
    
"""a=int(input("enter"))
def check(a):
    if a%10==5:
        return a**2
    elif a%10==3:
        return a**3
    elif a%10==6:
        return -1
    else:
        return a/2
n=check(a)
print(n)   """  

#Oops


"""class f15:
    def light(self):
        print("ok light is on")
    def fan(self,speed):
        print("fan is on and spped is",speed)
        self.s=speed
    def cpu(self):
        print("powering of the system")
        print(self.s)
nari=f15()
nari.light()
nari.fan(5)
nari.cpu()""""""              


""""""class shopping:
    def dresstype(self,cat):
        print("type of dress",cat)
        self.c=cat
    def price(self,range):
        print("price of dress",range)
        self.r=range    
    def size(self,fit):
        print("size of dress",fit)
        self.f=fit
    def display(self):
        print(self.c,self.r,self.f) 
bill=shopping()
bill.dresstype("shirt")
bill.price(3000)
bill.size(39)
bill.display()  """  """    

##Oops constructor

"""""""class shopping:
    def __init__(self,place):
        self.p=place
        print("welcome to ",place)
    def dresstype(self,cat):
        print("type of dress",cat)
        self.c=cat
    def price(self,range):
        print("price of dress",range)
        self.r=range    
    def size(self,fit):
        print("size of dress",fit)
        self.f=fit
    def display(self):
        print(self.c,self.r,self.f,self.p) 
bill=shopping("jockey")
bill.dresstype("shirt")
bill.price(3000)
bill.size(39)
bill.display()"""""

#singallevel inheritance

"""class shopping(f15):
    def __init__(self,place):
        self.p=place
        print("welcome to ",place)
    def dresstype(self,cat):
        print("type of dress",cat)
        self.c=cat
    def price(self,range):
        print("price of dress",range)
        self.r=range    
    def size(self,fit):
        print("size of dress",fit)
        self.f=fit
    def display(self):
        print(self.c,self.r,self.f,self.p) 
bill=shopping("jockey")
bill.dresstype("shirt")
bill.price(3000)
bill.size(39)
bill.display()
bill.light()
bill.fan(5)
bill.cpu()"""

##multilevel inhertance

"""class f15:
    def light(self):
        print("light is on")
f=f15()
class typedress(f15):
    def shirt(self):
        print("type of dress")
d=typedress()
class shopping(typedress):
    def cat(self,men):
        print("type of cat",men)
        self.m=men
e=shopping()
e.shirt("jean")
e.light()  
e.cat(5)"""

## hierarichial
"""class f15:
    def light(self):
        print("light is on")
f=f15()
class typedress(f15):
    def shirt(self):
        print("type of dress")
d=typedress()
class shopping(f15):
    def cat(self,men):
        print("type of cat",men)
        self.m=men
e=shopping()
class btech(f15):
    def place(self):
        print("students are placed")
g=btech()
g.light()
g.shrit()
g.cat(5)
g.place()"""                


#polymorphism
#FUNCTION OVERLOADING
"""class art:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj=art()
obj.add(10)                
obj.add(10,20)
obj.add(1,2,3)      """


#constructor overloading

"""class art:
    def __init__(self):
        print("there is no arguments")
    def __init__(self):
        print("passing one argument")
    def __init__(self):
        print("passing two argument")
obj=art()
#obj=art(10)
obj=art(1,2)  """          
    

##project carshowroom
      
"""class car_showroom:
    def company(self,name):
        c=["landrover","mg","mahindra"]
        if name in c:
            print("welcome to ",name)
    def model(self,name):
        d={"landrover":["rangerover","defender"],"mg":["hector","gloster"],"mahindra":["thar","xuv"]}
        if name in d:
            print(d[name])
    def price(self,name,m):
        print("you have selected",m)
        price_list={"rangerover":20000000,"defender":15000000,"hector":3000000,"gloster":5000000,"thar":4000000,"xuv":3500000}
        if m in price_list:
            car_price=price_list[m]
            cgst=0.1*car_price
            sgst=0.1*car_price
            insurance=100000
            onroad_price=car_price+cgst+sgst+insurance
            print("onroad price:",onroad_price)
n=input("enter car company:")
car=car_showroom()
car.company(n)
car.model(n)
m=input("enter model of car:")
car.price(n,m)"""


class carshowroom:
    def company(self):
        self.cgst=0.1
        self.sgst=0.1
        self.insurance=1000000

        while True: 
           print("mg","tata")
           self.n=input("enter the car company")
           if self.n=="mg":
               print("welcome to mg")
               self.model()
               break
           elif self.n=="tata":
               print("welcome to tata")
               self.model()
               break
           else:
               print("invaild car company")
    def model(self):
        if self.n=="mg":
            while True:
                print("select from hector and gloster")
                self.choice=input("enter the car name")
                if self.choice=="hector":
                    self.price(self.choice)
                    break
                elif self.choice=="gloster":
                    self.price(self.choice)
                    break
                else:
                    print("invaild car model")
        elif self.n=="tata":       
            while True:
                print("select from nexon and punch")
                self.choice=input("enter the car name")
                if self.choice=="nexon":
                    self.price(self.choice)
                    break
                elif self.choice=="punch":
                    self.price(self.choice)
                    break
                else:
                    print("invaild car model")
    def price(self,choice):
        if choice=="hector":
            self.p=30000000
        elif choice=="gloster":
            self.p=50000000
        elif choice=="nexon":
            self.p=15000000
        elif choice=="punch":
            self.p=12000000
            total=self.p+(self.cgst*self.p)+(self.sgst*self.p)+self.insurance
            print(total)
q=carshowroom()
q.company()            
        


                            
                    

                             



       

        
        



 