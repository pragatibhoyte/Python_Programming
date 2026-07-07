def DisplayDigits(No):

    digit = 0

    while(No > 0):

        digit = No % 10
        print(digit)
        No = No // 10

def main():

    No = int(input("Enter Number : "))

    DisplayDigits(No)

if __name__ == "__main__":
    main()