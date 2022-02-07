largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        num = int(num)
        if largest is None:
            largest = num
        elif num>largest:
            largest = num

        if smallest is None:
            smallest = num
        elif num<smallest:
            smallest = num

    except:
        if num == "done" :
            break
        print('Invalid Input')

print("Maximum", largest)
print("Smallest", smallest)
