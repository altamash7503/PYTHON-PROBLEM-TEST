a=str(input("Please enter the input string between 10-10000: "))

counts = []

words = a.split()

array=str(input("Please enter the validation array less than 1000: "))
b=array.split()


if len(a)<10 or len(a)>10000 or len(b)>1000:#condition was given to give input in range 10-10000
    print("please input between range 10-10000")

    
else:    
    for i in b:
        if i in words:
            print(i,":",a.count(i))
        
    
        

