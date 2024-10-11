string = input("please enter your own word: ")
char = input("please enetr your own character")
i = 0
count = 0
while (i < len(string)):
    if(string[i] == char):
        count = count + 1
    i = i + 1
print("the total number of times ", char, "has occured=" ,count)
lower = int(input("enter a upper range: "))
upper = int(input("enter a lower range: "))
print("prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if ( num % i) == 0:
                break
        else:
                print(num)
num = int(input("enter a number : "))
t = num
numlen = 0
while t>0:
    numlen = numlen+1
    t = int(t/10)
    if numlen>=4:
         numlen = int(numlen/2)
         chk = 0
         while num>0: