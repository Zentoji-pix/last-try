weight = float(input("weight: "))
unit = input('(K)g or (L)bs: ')
unit = str(unit.upper())
lbs_to_kg = 2.20462
kg_to_lbs = 0.453592
if unit == "K":
    weight_in_lbs = float(kg_to_lbs) * weight #for weight in pounds
    print("Weight in Lbs: " + str(weight_in_lbs))
elif unit == "L":
    weight_in_kg = float(lbs_to_kg) * weight #for weight in kg
    print("Weight in Kg: " + str(weight_in_kg))
