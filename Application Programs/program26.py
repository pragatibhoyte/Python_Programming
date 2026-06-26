class NumberX:

    def CheckDivisibility(self, iNo):

        if(iNo % 3 == 0 and iNo % 5 == 0):
            return True
        
        else:
            return False
        
def main():

    nobj = NumberX()

    iValue = 0
    bRet = False

    iValue = int(input("Enter Number to Check Divisibility : "))

    bRet = nobj.CheckDivisibility(iValue)

    if(bRet == True):
        print(f"{iValue} is Divisible by both 3 and 5")

    else:
        print(f"{iValue} is Not Divisible by both 3 and 5")

if __name__ == "__main__":
    main()
