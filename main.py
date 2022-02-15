import math
from math import sin, cos, tan, asin, acos, atan, radians, degrees

print("NOTE: everything is rounded to 3 decimal places \n")


# calculate length
def find_sine():
    sine = sin(radians(angle))

    find = input("Would you like to find the hypotenuse or the opposite [o or h]\t").lower()

    if find == "o":
        hyp = float(input("Enter the length of the hypotenuse:\t"))

        opp = sine * hyp
        print(format(opp, ".3f"))
    else:
        opp = float(input("Enter the length of the opposite:\t"))

        hyp = opp/sine
        print(format(hyp, ".3f"))


def find_cosine():
    cosine = cos(radians(angle))

    find = input("Would you like to find the adjacent or the hypotenuse [a or h]\t").lower()

    if find == "a":
        hyp = float(input("Enter the length of the hypotenuse:\t"))

        adj = cosine * hyp
        print(format(adj, ".3f"))
    else:
        adj = float(input("Enter the length of the adjacent:\t"))

        hyp = adj/cosine
        print(format(hyp, ".3f"))


def find_tangent():
    tangent = tan(radians(angle))

    find = input("Would you like to find the opposite or the adjacent [o or a]\t").lower()

    if find == "o":
        adj = float(input("Enter the length of the adjacent:\t"))

        adj = tangent * adj
        print(format(adj, ".3f"))
    else:
        opp = float(input("Enter the length of the opposite:\t"))

        hyp = opp/tangent
        print(format(hyp, ".3f"))


def pythagoras_theorem():
    a_sq = float(input("Enter length of a\t"))**2
    b_sq = float(input("Enter length of b\t"))**2
    c_sq = a_sq + b_sq
    c = math.sqrt(c_sq)

    print(f"c = {c}")


# calculate degrees
def find_degrees():
    find = input("Would you like to use the sine, cosine, or tangent? \nEnter [sin/cos/tan]\t(Think SohCahToa)\t")

    if find == "sin":
        hyp = float(input("Enter the length of the hypotenuse:\t"))
        opp = float(input("Enter the length of the opposite:\t"))

        angle = degrees(asin(opp/hyp))
        print(format(angle, ".3f"), "degrees")
    
    elif find == "cos":
        hyp = float(input("Enter the length of the hypotenuse:\t"))
        adj = float(input("Enter the length of the adjacent:\t"))

        angle = degrees(acos(adj/hyp))
        print(format(angle, ".3f"), "degrees")

    else:
        opp = float(input("Enter the length of the opposite:\t"))
        adj = float(input("Enter the length of the adjacent:\t"))

        angle = degrees(atan(opp/adj))
        print(format(angle, ".3f"), "degrees")



# to figure out what we are calculating

user = input("Would you like to figure out the length or the angle?\t").lower()

if user == "length":
    set_mode = input("Are you using an angle or pythagoras [angle/pt]\t")
    if set_mode == 'pt':
        pythagoras_theorem()
    else:
    
        angle = float(input("Enter the angle:\t"))
    
        # to know which function to call
        sahcahtoa = input("Would you like to use the sine, cosine, or tangent? \nEnter [sin/cos/tan]\t(Think SohCahToa)\t")
    
        if sahcahtoa == "sin":
            find_sine()
        elif sahcahtoa == "cos":
            find_cosine()
        else:
            find_tangent()
else:
    find_degrees()
