def get_multiple_6():
    """
    Returns a multiple of 6 that was entered by the user.
    :return: int a number
    """
    while True:
        try:
            n=input("Please give me a multiple of 6: ")
            n=int(n)
            if n/6==n//6:
                return n
            else:
                print("That is not a multiple of 6")
        except ValueError:
            print("You have not entered a number. Please try again.")

print(get_multiple_6())