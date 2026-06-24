def Display(iNo):

    # Input Filter
    
    if(iNo < 0):

        print("Invalid input")
        return

    iCnt = 0

    for iCnt in range(iNo,0,-1):      
        print(iCnt)

def main():

    iValue = int(input("Enter frequnecy : "))
    
    Display(iValue)

if __name__ == "__main__":
    main()