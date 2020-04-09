
Numbers = input("Enter the number using comma :")
number = Numbers.split(",")
Numbers = [int(numeric_string) for numeric_string in number]
possible_values= ''
for i in Numbers:
    for d in Numbers:
        if i != d:
            Xor= i^d
            possible_values=possible_values + "," + str(Xor)

possible = possible_values.split(",")
print(max(possible))


