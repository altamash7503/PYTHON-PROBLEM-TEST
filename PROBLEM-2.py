a=str(input("Please enter the input array less than 1000 :  "))
words=a.split()

b=str(input("Please enter the rejected array less than 1000:  "))
new=b.split()


if len(a)>1000 or len(b)>1000:
    print("Please make an array less than 1000 words")
else:
    
    for i in list(words):
        if i in new:
            words.remove(i)
print("The new array by rejecting words is : " ,words)
