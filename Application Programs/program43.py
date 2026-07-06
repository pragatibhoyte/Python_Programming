# Prime number 

def ChkPrime(No):

    if No <= 1:
        return False
    
    i = 0

    for i in range(2,int(No**0.5)+1):

        if(No % i == 0):
            break

    else:
        return True
    
    return False

def main():

    No = int(input("Enter Number : "))
    
    Ret = ChkPrime(No)

    if(Ret == True):
        print("Number is prime")
    
    else:
        print("Number is not prime")

if __name__ == "__main__":
    main()