#/usr/bin/python
l=input("Please enter a string")
print (l.upper())
print (l.lower())
print(l.title())
k=list(l)
str2=k[0].capitalize()
k.pop(0)
str3="".join(k)
str2+=str3
print (str2)