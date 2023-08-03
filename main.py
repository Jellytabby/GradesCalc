if __name__ == '__main__':
    inp = input("Total number of points: \n")
    if inp != "" and isinstance(eval(inp),(int,float)):
        total = eval(inp)
    else:
        print("Invalid input!")
        exit()
    exp = []
    achieved = 0

    points = 0
    while True:
        points = (input("Exercise points: \n"))

        if points == "":
            break
        else:
            points = eval(points)
            if (not isinstance(points, (float, int))) or (points < 0):
                print("Invalid input!")
                continue
            exp.append(points)
            achieved += points

            if achieved > total:
                print("Total number of points exceeded!")
                ans = input("Do you want to reenter the last value? \n")
                if ans.lower()[0] == "y":
                    achieved -= points
                    exp.pop(-1)
                else:
                    exit()

    grade = achieved / int(total) * 5 + 1
    percent = achieved / int(total) * 100

    out = "| "
    for i in range(len(exp)):
        out += (str(exp[i]) + " | ")
    print("-" * len(out))
    print(out)
    print("-" * len(out))
    print("Total points: " + str(total) + " | ", end="")
    print("Achieved points: " + str(achieved))
    print("Grade: " + str(round(grade, 2)))
    print("Percent: " + str(round(percent, 2)) + "%")
    print()

