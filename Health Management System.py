def function1(n):
    n= int(input("Enter 1 for Harry, 2 for Chetan, 3 for Alice:"))
    if n==1:
        n = int(input("You want to lock or check, Enter 1 for Lock, Enter 2 for Check:"))
        if n==1:
            n = int(input("What you want to lock, Press 1 for Exercise, Press 2 for Diet:"))
            if n==1:
                f = open("Harryexe.txt", "a")
                f.write(input("Enter your exercise"))
                f.close()
            elif n==2:
                f = open("Harrydiet.txt", "a")
                f.write(input("Enter your diet taken"))
                f.close()
            else:
                print("Enter a valid Input")
        elif n==2:
            n = int(input("What you want to check, Press 1 for Exercise, Press 2 for Diet:"))
            if n==1:
                f = open("Harryexe.txt", "rt")
                print(f.readlines())
                f.close()
            elif n==2:
                f = open("Harrydiet.txt", "rt")
                print(f.readlines())
                f.close()
            else:
                print("Enter valid input")
    elif n==2:
        n = int(input("You want to lock or check, Enter 1 for Lock, Enter 2 for Check:"))
        if n==1:
            n = int(input("What you want to lock, Press 1 for Exercise, Press 2 for Diet:"))
            if n == 1:
                f = open("Chetanexe.txt", "a")
                f.write(input("Enter your exercise"))
                f.close()
            elif n == 2:
                f = open("Chetandiet.txt", "a")
                f.write(input("Enter your diet taken"))
                f.close()
            else:
                print("Enter a valid Input")
        elif n==2:
            n = int(input("What you want to check, Press 1 for Exercise, Press 2 for Diet:"))
            if n == 1:
                f = open("Chetanexe.txt", "rt")
                print(f.readlines())
                f.close()
            elif n == 2:
                f = open("Chetandiet.txt", "rt")
                print(f.readlines())
                f.close()
            else:
                print("Enter valid input")
    elif n==3:
        n = int(input("You want to lock or check, Enter 1 for Lock, Enter 2 for Check:"))
        if n == 1:
            n = int(input("What you want to lock, Press 1 for Exercise, Press 2 for Diet:"))
            if n == 1:
                f = open("Aliceexe.txt", "a")
                f.write(input("Enter your exercise"))
                f.close()
            elif n == 2:
                f = open("Alicediet.txt", "a")
                f.write(input("Enter your diet taken"))
                f.close()
            else:
                print("Enter a valid Input")
        elif n==2:
            n = int(input("What you want to check, Press 1 for Exercise, Press 2 for Diet:"))
            if n == 1:
                f = open("Aliceexe.txt", "rt")
                print(f.readlines())
                f.close()
            elif n == 2:
                f = open("Alicediet.txt", "rt")
                print(f.readlines())
                f.close()
            else:
                print("Enter valid input")
function1("Function Ends Here")
