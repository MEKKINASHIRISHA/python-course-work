# Sets.py

s=set() #Creating empty Set
s={1,2,3,4,5,}
print("Set s is:",s) #Set s is: {1, 2, 3, 4, 5}

sets=set()
sets={1,2,3,1,4,5,2,3,4,5} #Creating a set with Duplicate elements
print("Creating Set with Duplicate Values:",sets) #Creating Set with Duplicate Values: {1, 2, 3, 4, 5} 
# Sets doesn't allow duplicate values

# OPerations on Sets

# 1.MemberShip Testing
print("Is 2 in s:",2 in s) #Is 2 in s: True
print("Is 18 in s:",18 in s) #Is 18 in s: False
print("Is 4 not in s:",4 in s) #Is 4 not in s: True
print("Is 78 not in s:",78 not in s) #Is 78 not in s: True

# Union Operation
Union= s | sets
print("union operati")