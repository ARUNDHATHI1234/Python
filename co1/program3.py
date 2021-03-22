#3.a)positive list of numbers
list=[-5,10,0,-14,18,17]
newlist=[x for x in list if x>0]
print(newlist)

#3.b)square of n numbers
n=int(input("enter the number of numbers:"))
list=[]
for i in range(n):
  a=int(input("enter the number:"))
  list.append(a)
print(list)
list1=[x**2 for x in list]
print(list1)

#3.c)list of vowels
word=input("enter a word:")
vowels=[x for x in word if x in ['a','e','i','o','u']]
print(vowels)
