#creating a list
empty_list=[]                     #empty list
numbers=[11,4,23,71,58]           #list consisting of only integer values
mixed_list=[1,"mango",6.74,True] #list consisting of different datatypes values
print(empty_list)   
print(numbers)
print(mixed_list)

#Indexing in list
my_list=[45,58,47,78]
print(my_list[0])
print(my_list[2])
print(my_list[-1])
print(my_list[-2])

#slicing in list
list=[20,40,60,80,100,120]
print(list[1:4])
print(list[:3])
print(list[2:])
print(list[-4:-1])

#Common list methods
a=[10,20,23,20]
a.append(30)          #append()
print(a)
a.insert(1,15)        #insert()
print(a)
a.extend([3,4])      #extend()
print(a)
a.remove(20)         #remove()
print(a)
a.pop(1)              #pop()
print(a)
a.sort()              #sort()
print(a)
a.reverse()           #reverse()
print(a)
print(a.count(20))    #count()
print(a.index(23))    #index()
a.clear()
print(a)              #clear()

#WAP to ask user to enter names of their 3 favourite movies and store them in a list
movies=[]
mov1= input("enter your first movie")
mov2=input("enter your second movie")
mov3=input("enter your third movie")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

#WAP to check if a list contains a pallindrome of elements(hint=use copy())
list1=["m","a","a","m"]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("Palindrome")
else:
    print("not palindrome")