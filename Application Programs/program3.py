def Addition(No1, No2):
    Sum = No1 + No2
    return Sum

def main():

    fValue1 = float(input("Enter first number : "))
    fValue2 = float(input("Enter second number : "))

    fRet = Addition(fValue1, fValue2)

    print("Addition is : ",fRet)

if __name__ == "__main__":
    main()
