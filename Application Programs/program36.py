def ChkPrime(No):

    for i in range(2,No):

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