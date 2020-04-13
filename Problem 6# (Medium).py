number = int(input("enter the operation :"))
string_number = str(number)
length = len(string_number)
numbers = [int(numeric_string) for numeric_string in string_number]
number = list(numbers)
result = length 

for i in range (length):
    if length-1 == i:
        pass

    else:
        if number[i] > 2:
            result = result-1

print(result)