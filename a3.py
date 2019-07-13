numb = int(input("Enter any number: "))
flag = numb%2
if flag == 0:
    print(numb,"is an even number")
elif flag == 1:
    print(numb,"is an odd number")
else:
    print("Error, Invalid input")
