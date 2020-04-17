query = (input("Enter the prefix :")).lower()
string = input("Enter the words :")
string = string.split(" ")
for i in string:
    t = i.lower()
    if t[0] == query[0]:
        if t[1] == query[1]:
            print(i)
