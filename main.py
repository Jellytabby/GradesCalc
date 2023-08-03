# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    total = input("Total number of points: \n")
    exp = []
    achieved = 0

    points = 0
    while points != "":
        points = input("Exercise points: \n")

        if not points.isnumeric() and points != "":
            print("Invalid input")
        elif points != "":
            if achieved + int(points) > int(total):
                print("You can't achieve more than " + str(total) + " points")
                choice = input("Do you want to restart? (y/n) ")
                if choice == "y":
                    achieved = 0
                    exp = []
                    continue
                elif choice == "n":
                    break
                else:
                    print("Invalid input")
                    break
            else:
                exp.append(int(points))
                achieved += int(points)

    grade = achieved / int(total) * 5 + 1
    percent = achieved / int(total) * 100

    print("-----"* len(exp) + "----")
    for i in range(len(exp)):
        print(str(exp[i]) + " | ", end="")
    print()
    print("-----"* len(exp) + "----")
    print("Total points: " + str(total) + " | ", end="")
    print("Achieved points: " + str(achieved))
    print("Grade: " + str(round(grade, 2)))
    print("Percent: " + str(round(percent, 2)) + "%")
    print()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
