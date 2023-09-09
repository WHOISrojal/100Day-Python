# Check Prime Number or not

def function(num):
    for i in range(2, num):
        flag = 0
        if num % i == 0:
            flag == 1
    if flag == 0:
        print("Prime number")
    else:
        print("Not a Prime number")

n = int(input("Enter a number\n"))
function(num = n)      