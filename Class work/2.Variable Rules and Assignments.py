# 2.Variable  rules and Assignments

myvar=10
myVar=10
myvar1=10
my_var=10
#my@var=10 **SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?**
myvar=10 #valid Var
Myvar=10 #valid Var
myvar18=10 #valid var
#1myvar=10 **syntaxError: invalid decimal literal**
_myvar=10 #valid var
#@myvar=10 **syntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of**
#my var=10 **syntaxError: invalid syntax**

myvar=10 #case-sensitive
Myvar=30 #case-sensitive
print(myvar,Myvar) #10 30

a=10 #Assignment
a,b,c=10,20,30 #Multiple Assignment
print(a,b,c) #10 20 30

a=b=c=10 #same value Assignment
print(a,b,c) #10 10 10

a=10
b=20
print("Before swapping(a,b):",a,b) #Before swapping(a,b): 10 20
a,b=b,a
print("After Swapping(a,b):",a,b) #After Swapping(a,b): 20 10

del a
#print(a)
'''Traceback (most recent call last)
File "<pydhell#30>,line 1,in <module>
print(a)
NameError: name a is not defined'''

b=20 #Reassignment
print(b) #20