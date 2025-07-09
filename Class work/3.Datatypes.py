#3.DataTypes

#1.NumericTypes
a=10
print(type(a)) #<class 'int'>
a=10.0
print(type(a)) #<class 'float'>
a=3+4j
print(type(a)) #<class 'complex'>

#2.string
name='Shirisha'
print(type(name)) #<class 'str'>
name="Shirisha"
print(type(name)) #<class 'str'>
name='''Shirisha'''
print(name) #Shirisha
print(type(name)) #<class 'str'>

print("Lucky and Funny") #Lucky and Funny
print("'Lucky' and 'Funny'") #'Lucky' and 'Funny'

#3.List
fav=['phone','Playstation','traintoy']
# fav=[] - creating list
# fav=list() - creating list using constructor
print("List is:",fav) #List is: ['phone', 'Playstation', 'traintoy']

f=[1,2.3,2+5j,"string",[]]
# list can have any type of data
print(f) #[1, 2.3, (2+5j), 'string', []]
fav.append("Laptop") #append is used to add elements
print("list After appending:",fav) #list After appending: ['phone', 'Playstation', 'traintoy', 'Laptop']

lst=[1,2,3,4,5]
print("list:",lst) #list: [1, 2, 3, 4, 5]
print(type(lst)) #<class 'list'>

# 4.Tuples
t=() # creating a tuple
t=tuple() #creating a tuple using constructor
t=(1,2,3,4,5)
print("Tuple is:",t) #Tuple is: (1, 2, 3, 4, 5)
print(type(t)) #<class 'tuple'>
tu=(1,2,3,1,4,5,2)
print("tuple:",tu) #tuple: (1, 2, 3, 1, 4, 5, 2) -tuple allows duplicates


# 5.sets
s=set() # sets only created using constructor
s={1,1,3,1,2,2,}
print("Set is:",s) #Set is: {1, 2, 3}- sets doesn't allow duplicates
print(type(s)) #<class 'set'>
se=frozenset({1,2,7,5})
print(type(se)) #<class 'frozenset'>
#se.add(45) - it shows error because it cannot be modified

# 6.Dictionaries
d={} #creating a tuple
d=dict() # creating a tuple using a constructor
d={'name':'Shirisha','Course':'DA','batch':14}
print("Dictionary is:",d) #Dictionary is: {'name': 'Shirisha', 'Course': 'DA', 'batch': 14}
d={'name':'Shirisha','Course':'DA','batch':14,'skills':['py','sql','powerbi']}
print("dictionary is:",d) # dictionary is: {'name': 'Shirisha','Course': 'DA', 'batch': 14, 'skills': ['py', 'sql', 'powerbi']}
print("name is:",d['name']) #name is: Shirisha
print("couse is:",d['Course']) #couse is: DA
print("skills are:",d['skills']) #skills are: ['py', 'sql', 'powerbi']


# 7.boolean
lockstatus=True
bestseller=False
randomvar=None
print(type(lockstatus)) #<class 'bool'>
print(type(bestseller)) #<class 'bool'>

# 8.None 
print(type(randomvar)) #<class 'NoneType'>
randomvar="Ravi"
print(type(randomvar)) #<class 'str'>