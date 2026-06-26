class NumberX:

    def ChkPerfect(self, iNo):

        iSum = 0

        for i in range(1,(iNo // 2)+1):     

            if(iNo % i == 0):

                iSum = iSum + i

        if(iSum == iNo):
            return True
        else:
            return False

def main():

    nobj = NumberX()

    iValue = 0
    bRet = False

    iValue = int(input("Enter Number : "))

    bRet = nobj.ChkPerfect(iValue)

    if(bRet == True):
        print(f"{iValue} is Perfect Number")
    else:
        print(f"{iValue} is Not Perfect Number")

if __name__ == "__main__":
    main()
