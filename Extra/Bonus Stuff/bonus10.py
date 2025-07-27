while True:
    try:
        width = float(input("Enter the width of the rectangle: "))
        length = float(input("Enter the length of the rectangle: "))

        area = width * length
        print("The area of the rectangle is", area)
    except ValueError:
        print("Please enter a number for the width and length")

