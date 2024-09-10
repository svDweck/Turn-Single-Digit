def turnSingleDigit(n):
    if n<10:
        return n;
    elif n<100:
        return int(n/10);
    elif n<1000:
        return int(n/100);
    elif n<10000:
        return int(n/1000);
    else:
        return 0;


print("Type exit to stop")
number = ""

while(number != "exit"):
    number = input("Enter number to reduce to a single digit: ");
    print(turnSingleDigit(int(number)));