numbers=input("Enter numbers of your with comma in between :")

number = numbers.split(",")
numbers = [int(numeric_string) for numeric_string in number]

final_number= int

for i in numbers:
    present_number= 1
    for d in numbers:
        if i != d:
            present_number= present_number*d
    
    final_number= final_number, present_number

print(final_number)
