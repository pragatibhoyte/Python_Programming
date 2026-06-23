def CkeckEvenOdd(iNo):
    iRemainder = iNo % 2
    if(iRemainder == 0):
        print(f"{iNo} is Even")
    else:
        print(f"{iNo} is Odd")
    

def main():

    iValue = int(input("Enter Number : "))

    CkeckEvenOdd(iValue)

if __name__ == "__main__":
    main()
