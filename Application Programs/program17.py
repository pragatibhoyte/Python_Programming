def Display(iNo):

    # Input Filter
    
    if(iNo < 0):

        print("Invalid input")
        return

    iCnt = 0

    for iCnt in range(0,iNo):      
        print("Jay Ganesh...")

def main():

    iValue = int(input("Enter frequnecy : "))
    
    Display(iValue)

if __name__ == "__main__":
    main()