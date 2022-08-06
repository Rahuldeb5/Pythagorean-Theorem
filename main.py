print("Pythagorean Theorem Calculator\n")

import math

def sqr_sim(und_root, l_strip=None):
    und_root = int(und_root)
    und_root0 = round(und_root)
    rt_fc = []
    coef = 1
    if und_root < 0:
        return None
    elif und_root == 0:
        return 0
    else:
        for i in range(2, und_root0):
            if und_root%(i**2) == 0:
                rt_fc.append(i)
                und_root /= i**2

                for i0 in range(2, und_root0):
                    if und_root%(i0**2) == 0:
                        rt_fc.append(i0)
                        und_root /= i0**2

        for ele in rt_fc:
            coef *= ele
        if coef == 1:
            print('Answer: ' + '√' + str(und_root))
        else:
            print('Answer: '+ str(coef) + '√' + str(int(und_root)))


a = int(input("Enter opposite value (a): "))

b = int(input("Enter adjacent value (b): "))


if a + b <= 900:
    c = math.sqrt((a ** 2 + b ** 2))
else:
    c = math.sqrt((a+b)**2 - 2*a*b)

number = a**2 + b**2

root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print("Hypotenuse value (c): " + str(math.ceil(c)))
else:
    print("Hypotenuse value (c): " + "√" + str(number))
    print("Would you like to simplify?")
    answer = None
    while answer not in ("y", "n"):
        answer = input("Enter y/n: ")
        if answer == "y":
            sqr_sim(str(number))
        elif answer == "no":
            pass
        else:
            print("Please enter y/n.")
