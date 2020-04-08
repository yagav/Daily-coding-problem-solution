#Input

String=input("please enter the numbers using comma:")
Stringarray=String.split (",")

#Converting to integer

Integerarray=[int(numeric_string) for numeric_string in Stringarray]

#Process
maximum= max(Integerarray)
number= 0

if number>maximum:
    print("1")


else:    
    loop= True
    while loop:
        number= number+1
        if number not in Integerarray:
            print(number)
            loop= False


