Python 3.15.0b3 (tags/v3.15.0b3:cf16a33, Jun 23 2026, 10:03:50) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
KeyboardInterrupt
KeyboardInterrupt
while True:
    print("\n--- AREA CALCULATOR ---")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        radius = float(input("Enter radius: "))
        area = 3.14 * radius * radius
        print("Area of Circle =", int(area))

    elif choice == 2:
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        area = length * breadth
        print("Area of Rectangle =", int(area))

    elif choice == 3:
        side = float(input("Enter side: "))
        area = side * side
        print("Area of Square =", int(area))

    elif choice == 4:
        print("Program exited.")
        break

    else:
        print("Invalid choice! Please enter 1 to 4.")


--- AREA CALCULATOR ---
1. Circle
2. Rectangle
3. Square
4. Exit
Enter your choice: 
============================================ RESTART: C:/Users/student121/AppData/Local/Programs/Python/Python315/day2 ============================================

--- AREA CALCULATOR ---
1. Circle
2. Rectangle
3. Square
4. Exit
Enter your choice: 1
Enter radius: 3.4
Area of Circle = 36

--- AREA CALCULATOR ---
1. Circle
2. Rectangle
3. Square
4. Exit
Enter your choice: 2
Enter length: 4.5
Enter breadth: 5
Area of Rectangle = 22

--- AREA CALCULATOR ---
1. Circle
2. Rectangle
3. Square
4. Exit
Enter your choice: 3
Enter side: 45
Area of Square = 2025

--- AREA CALCULATOR ---
1. Circle
2. Rectangle
3. Square
4. Exit
Enter your choice: 4
Program exited.
>>> 
=============================================== RESTART: C:/Users/student121/Desktop/SAKTHI DEVI/DAY-01-ARTHMETIC.py ==============================================
Enter first number: 
=============================================== RESTART: C:/Users/student121/Desktop/SAKTHI DEVI/DAY-1-ARITHMETIC.py ==============================================
Enter first number: 10
Enter second number: 5
Addition = 15
Subtraction = 5
Multiplication = 50
Division = 2.0
