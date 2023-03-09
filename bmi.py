# calculate bmi
def calculateBMI(weight, height):
    weight = weight * .45
    height = (height * .025) ** 2
    bmi = weight / height
    print(bmi)
    return bmi

# handle inputs and outputs
def main():
    # get weight and height from user
    weight = int(input("Enter your weight in pounds: "))
    feet, inches = map(int, input("Enter your weight in feet and inches: ").split())
    height = (feet * 12) + inches # convert height to inches
    bmi = calculateBMI(weight, height) # calculate bmi
    # output bmi range
    if bmi < 18.5: input("Underweight")
    elif bmi < 25: input("Normal Weight")
    elif bmi < 30: input("Overweight")
    else: input("Obese")
    return 0

main()
