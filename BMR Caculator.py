#读取输入信息

gender = input("Please input gender(male/female):")
weight = float(input("Pls input weight(kg):"))
height = float(input("Pls input your height(cm):"))
age = int(input("Pls input your age(year old):"))

# 根据性别进行不同计算
if gender == "male":
    bmr = 66.5+13.8*weight+5.0*height-6.8*age
elif gender == "female":
    bmr = 665.1+9.6*weight+1.8*height-4.7*age
else:
    print("gender inputting incorrect, pls input again")
    exit()
# 输出结果

print("Your BMR is %.2f Kcal/day" % bmr)
