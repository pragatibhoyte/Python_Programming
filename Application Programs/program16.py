def Display(iNo):

    # Input Updater
    
    if(iNo < 0):

        iNo = -iNo

    iCnt = 0

    for iCnt in range(0,iNo):      
        print("Jay Ganesh...")

def main():

    iValue = int(input("Enter frequnecy : "))
    
    Display(iValue)

if __name__ == "__main__":
    main()