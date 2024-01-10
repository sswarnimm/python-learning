s1 = int(input("enter marks of s2 : "))
s2 = int(input("enter marks of s1 : "))
s3 = int(input("enter marks of s3 : "))
s4 = int(input("enter marks of s4 : "))
s5 = int(input("enter marks of s5 : "))

mylist = [s1,s2,s3,s4,s5]
mylist.sort()
print(mylist)


#tuple cannot be changed

a = (1,2,3,45,5)

a[2]= 5