class NumberX:

    def DisplayFactors(self, iNo):

        for i in range(1,iNo):

            if(iNo % i == 0):

                print(i)
        
def main():

    nobj = NumberX()

    iValue = 0

    iValue = int(input("Enter Number : "))

    nobj.DisplayFactors(iValue)

if __name__ == "__main__":
    main()
