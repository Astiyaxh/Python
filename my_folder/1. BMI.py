weight = int(input("Enter weight: "))
height = int(input("Enter height: "))
height = (height) / 100
bmi = float(weight) / (height*height)

if bmi < 18.5:
    print("شما دچار کمبود وزن هستید")
elif 18.5 <= bmi <= 29.9:
    print("وزن شما مناسب است")
elif bmi >= 30:
    print("شما دچار افزونگی وزن هستید")
