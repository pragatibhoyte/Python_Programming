def main():

    digit = 0
    No = 751

    while(No != 0):

        digit = No % 10
        print(digit)
        No = No // 10

if __name__ == "__main__":
    main()