# 4.PythonOPerators

#1.Arithmetic Operators

a=20
b=10
print("Addition(+):",a+b) #Addition(+): 30
print("Subtraction(-):",a-b) #Subtraction(-): 10
print("Multiplication(*):",a*b) #Multiplication(*): 200
print("Division(/):",a/b) #Division(/): 2.0
print("Floor Division(//):",a//b) #Floor Division(//): 2
print("Modulus(%):",a%b) #Modulus(%): 0
print("Exponentiation(**):",a**b) #Exponentiation(**): 10240000000000


# 2.Comparision Operators
print("Equal(==):",a==b) #Equal(==): False
print("Not Equal(!=):",a!=b) #Not Equal(!=): True
print("Greater than(>):",a>b) #Greater than(>): True
print("Less than(<):",a<b) #Less than(<): False
print("Greater than or Equal(>=):",a>=b) #Greater than or Equal(>=): True
print("Less than or Equal(<=):",a<=b) #Less than or Equal(<=): False


# 3.Assignment Operators
a=b
print("Assign(=):",a) #Assign(=): 10
a+=30
print("Add & Assign(+=):",a) #Add & Assign(+=): 40
a-=5
print("Subtract & Assign(-=):",a) #Subtract & Assign(-=): 35
a*=3
print("Multiply & Assign(*=):",a) #Multiply & Assign(*=): 105
a/=2
print("Divide & Assign(/=):",a) #Divide & Assign(/=): 52.5
a//=4
print("Floor Divide & Assign(//=):",a) #Floor Divide & Assign(//=): 13.0
a%=10
print("Modulus & Assign(%=):",a) #Modulus & Assign(%=): 1.0
a**=b
print("Exponentiate & Assign(**=):",a) #Exponentiate & Assign(**=): 1.0


# 4.Logical Operators
print(a>0 and a<5) #False
print(a%2==0 and a%3==0 and a%7==0) #False
print(a%3==0 and a%9==0) #True
print(a<=81000 or a%2==0) #True
print(a*2==1000000 or a+10==59059) #True
print(a<=0 and a==5000) #False
print(a%27==0) #True
print(not a%2==0) #True

# 5.membership

# Using String
s="Shirisha"
print("Is 'a' in s:",'a' in s) #Is 'a' in s: True
print("Is 'v' in s:",'v' in s) #Is 'v' in s: False
print("Is 'i' not in s:",'i' not in s) #Is 'i' not in s: False
print("Is 'k' not in s:",'k' not in s) #Is 'k' not in s: True

# Using list
l=['Shirisha','Navitha','Gangadhar','Nehanth','shanmukha Priya','udeep']
print("Is 'susmitha' in l:",'susmitha' in l) #Is 'susmitha' in l: False
print("Is 'Radhika' not in l:",'Radhika' not in l) #Is 'Radhika' not in l: True
print("Is 'Gangadhar' in l:",'Gangadhar' in l) #Is 'Gangadhar' in l: True
print("Is 'udeep' not in l:",'udeep' not in l) #Is 'udeep' not in l: False

# USing Tuple
t=[56,7,9,762,23]
print("Is 762 in t:",762 in t) #Is 762 in t: True
print("Is 56 not in t:",56 not in t) #Is 56 not in t: False
print("Is 45 in t:",45 in t) #Is 45 in t: False98
print("Is 6 not in t:",6 not in t) #Is 6 not in t: True

# Using sets
se={45,8987,13,67,12}
print("Is 67 in se:",67 in se) #Is 67 in se: True
print("Is 13 not in se:",13 not in se) #Is 13 not in se: False
print("Is  98 in se:",98 in se) #Is  98 in se: False
print("Is 23 not in se:",23 not in se) #Is 23 not in se: True

# Using Dictionary
d={'name':'Shirisha','age':'20','course':'DA'}
print("Is 'name' in d:",'name' in d) #Is 'name' in d: True
print("Is 'course' not in d:",'name' not in d) #Is 'course' not in d: False
print("Is 'DA'  in d:",'DA' in d) #Is 'DA'  in d: False
print("Is 20 not in d:",20 not in d) #Is 20 not in d: True


# 6.Identity Operator
a=[1,2,3,4]
b=[1,2,3,4]
print("Is a is b:",a is b) #Is a is b: False
c=a
print("Is a is c:",a is c) #Is a is c: True
print(id(a)) #2139478504064
print(id(b)) #139475865344
print(id(c)) #2139478504064
print("Is b is not a:",b is not a) #Is b is not a: True
print("Is c is not a:",c is not a) #Is c is not a: False


# 7.Bitwise Operators
6&7
print("Bitwise AND is:",6&7) #Bitwise AND is: 6
