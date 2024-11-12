#start = input("Enter you start number: ")
#end = input("Enter your end number: ")

def ran_ge():
    num = int(input("Enter start number: "))
    end = int(input("Enter end number: "))
    arr = []

    if num < end:
        while True:
            num+=1
            arr.append(num)
            if num == end:
                break
    else:
        return "No find number"
    return arr

result = ran_ge()
print(result)
