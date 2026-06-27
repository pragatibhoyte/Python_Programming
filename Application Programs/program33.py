# Input : 5
# Output : 1 3 5

def Display(No):

    for i in range(1,No+1,2):
        print(i, end="\t")

def main():

    Value = int(input("Enter Number : "))
    Display(Value)

if __name__ == "__main__":
    main()