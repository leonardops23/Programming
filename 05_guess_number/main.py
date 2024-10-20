def main():
    number = 25

    while(True):
        try:
            input_num = int(input("Enter a number range(1 - 100): "))
            if input_num in range(1, 101):
                if input_num == number:
                    print("Number is correct, {}".format(number))
                    break
                if input_num < number:
                    print("Is max")
                if input_num > number:
                    print("Is less")
            else:
                print("Select number that is range")
        except:
            print("Engrese un number")

if __name__ == '__main__':
    main()
