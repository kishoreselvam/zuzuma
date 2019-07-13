l=input()
if l in ['a','e','i','o','u']:
    print("Vowel")
elif (ord(l)>=97 and ord(l)<=122)or(ord(l)>=65 and ord(l)<=90):
    print("Consonant")
else:
    print("invalid")
