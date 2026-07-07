def main():

    digit = 0
    No = 751

    digit = No % 10
    print(digit)
    No = No // 10

    digit = No % 10
    print(digit)
    No = No // 10

    digit = No % 10
    print(digit)
    No = No // 10

if __name__ == "__main__":
    main()