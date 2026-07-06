def ChkPrime(No):

    if No <= 1:
        return False

    for i in range(2,(int(No/2)+1)):

        if(No % i == 0):
            return False
    
    return True

def main():

    No = int(input("Enter Number : "))
    
    Ret = ChkPrime(No)

    if(Ret == True):
        print("Number is prime")
    
    else:
        print("Number is not prime")

if __name__ == "__main__":
    main()