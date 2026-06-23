
AGE_INVALID = -1

def CalculateTicketPrice(iAge):

    # Input Filter
    if(iAge < 0):
        return AGE_INVALID

    if (iAge >= 0 and iAge <= 5):
        return 200
    
    elif(iAge >= 6 and iAge <= 15):
        return 500
    
    elif(iAge >= 16 and iAge <= 30):
        return 900
    
    else:
        return 100
    
def main():

    iValue = int(input("Please Enter your Age : "))

    iRet = CalculateTicketPrice(iValue)

    if(iRet == AGE_INVALID):
        print("Please Enter positive Age")
    else:
        print("Your ticket price is : ",iRet)

if __name__ == "__main__":
    main()
