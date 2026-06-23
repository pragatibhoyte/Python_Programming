def CkeckEvenOdd(iNo):
    iRemainder = iNo % 2
    return iRemainder
    
def main():

    iValue = int(input("Enter Number : "))

    iRet = CkeckEvenOdd(iValue)

    if(iRet == 0):
        print(f"{iValue} is Even")
    else:
        print(f"{iValue} is Odd")

if __name__ == "__main__":
    main()
