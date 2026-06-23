def CkeckEvenOdd(iNo):
    iRemainder = iNo % 2

    if(iRemainder == 0):
        return True
    else:
        return False
    
def main():

    iValue = int(input("Enter Number : "))

    iRet = CkeckEvenOdd(iValue)

    if(iRet == True):
        print(f"{iValue} is Even")
    else:
        print(f"{iValue} is Odd")

if __name__ == "__main__":
    main()
