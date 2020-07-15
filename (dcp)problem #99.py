numbers = []
hmn = int(input("How many numbers: "))

for i in range (hmn):
    numbers.append(int(input("Enter a number:")))

s_numbers = sorted(numbers, reverse=True)

lengths = []
correct = 0
length=0
hmn = hmn-1
while hmn > 0:
    diff = s_numbers[hmn-1] - s_numbers[hmn]
    if diff == 1:
        correct+=1
        length+=1
    else:
        correct = 0
        lengths.append(length)
        length = 0
    hmn = hmn-1

try:
    print(max(lengths)+1)
except:
    print(length+1)
