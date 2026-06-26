class NumberX:

    def SumFactors(self, iNo):

        iSum = 0

        for i in range(1,(iNo // 2)+1):     

            if(iNo % i == 0):

                iSum = iSum + i

        return iSum
        
def main():

    nobj = NumberX()

    iValue = 0
    iRet = 0

    iValue = int(input("Enter Number : "))

    iRet = nobj.SumFactors(iValue)

    print(f"Summation of factors is : {iRet}")

if __name__ == "__main__":
    main()
