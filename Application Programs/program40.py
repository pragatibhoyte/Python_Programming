# Prime number using Count

def ChkPrime(No):

    if No <= 1:
        return False
    
    i = 0

    for i in range(2,(int(No/2)+1)):

        if(No % i == 0):
            break
    
    # ISSUE : Code generates wrong ans for No = 2
    
    if(i == int(No/2)):    
        return True
    else:
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