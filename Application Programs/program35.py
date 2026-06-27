# Input : 5
# Output : -5      -4      -3      -2      -1      0       1       2       3       4       5

def Display(No):

    for i in range(-No,No+1):
        print(i, end="\t")

def main():

    Value = int(input("Enter Number : "))
    Display(Value)

if __name__ == "__main__":
    main()