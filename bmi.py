# my bmi calculator project
# made by me for python class

def calc_bmi(w, h_cm):
    h_m = h_cm / 100
    result = w / (h_m * h_m)
    return round(result, 2)

def check_category(bmi):
    if bmi < 18.5:
        cat = "Underweight"
        msg = "you need to eat more!"
    elif bmi < 25:
        cat = "Normal"
        msg = "nice! you are healthy"
    elif bmi < 30:
        cat = "Overweight"
        msg = "try to exercise more"
    else:
        cat = "Obese"
        msg = "please see a doctor"
    return cat, msg

def get_input(question, low, high):
    while True:
        try:
            val = float(input(question))
            if val <= 0:
                print("please enter a positive number")
            elif val < low or val > high:
                print("that doesnt seem right, try again")
            else:
                return val
        except:
            print("thats not a number, try again")

def show_result(w, h_cm, bmi, cat, msg):
    print()
    print("----------")
    print("your results")
    print("----------")
    print("weight :", w, "kg")
    print("height :", h_cm, "cm")
    print("bmi    :", bmi)
    print("status :", cat)
    print("note   :", msg)
    print("----------")
    print()
    print("bmi chart:")
    print("under 18.5  = underweight")
    print("18.5 to 25  = normal")
    print("25 to 30    = overweight")
    print("above 30    = obese")
    print("----------")

def main():
    print("welcome to my bmi calculator")
    print()

    while True:
        w    = get_input("enter your weight in kg : ", 2, 500)
        h_cm = get_input("enter your height in cm : ", 50, 300)

        bmi = calc_bmi(w, h_cm)
        cat, msg = check_category(bmi)

        show_result(w, h_cm, bmi, cat, msg)

        again = input("want to try again? yes or no : ")
        if again.lower() != "yes":
            print("ok bye!")
            break

main()