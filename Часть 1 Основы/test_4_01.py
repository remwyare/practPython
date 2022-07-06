age_str = input("Введите возраст:")
age = int(age_str)
if age < 7:
    print("садик")
elif age < 18:
    print("Школьник")
elif age < 24:
    print("студент")
else:
    print("Работяга")
