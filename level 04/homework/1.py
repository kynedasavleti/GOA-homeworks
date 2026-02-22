# ჩამოწერეთ მინიმუმ 3 ცუდი პრაქტიკა ცვლადის დეკლარირების დროს.

#1. ცვლადის შექმნის დროს არ უნდა დავიწყოთ კოდი რიცხვებიტ
#2.არ უნდა გამოვიყენოთ სფეისი ცვლადის შექმნის დროს
#3. არ უნდა გამოვიენოთ ნებისმიერი სიმბოლო მაგ:  !, @, #

#ახსენით რას ეწოდება Debugging?
# debugging არის შენს მიერ დაწერილ კოდში შეცდომების აღმოჩენა და გასწორება

#ინტერნეტში მოიძიეთ და დაწერეთ თუ ძირითადად რა ტიპის Error-ებს ვხვდებით Python-ში. (მაგ. TypeError და ა.შ

#პითონში ვხვდებით: syntaxerror, nameerror, typeerror, indexerror.  

#გაასწორეთ მოცემული კოდები:

# 1. name = "Lika"
#    print(namme)

name = "Lika"
print(name)

# 2. number = 5
#    text = " apples"
#    result = "number" + "text"
#    print(result)

number = "5"
text = "apples"
result = number + text
print(result)

# 3. name = liKa
#    name2 = naame + "4"

name = "liKa"
name2 = name + "4"


# 4. first_user = "Lika"
#    2nduser = "Giorgi"
#    print(first user)

first_user = "lika"
user2 = "giorgi"
print(first_user)

# 5. first name = Data
#    last % name = "random"

first_name = "Data"
last_name = "random"

# 6. first_user = "Lika"
#    2nduser = "Giorgi"
#    print(first user)

first_user = "lika"
user2 = "giorgi"
print(first_user)

#მომხმარებელს შემოვატანინოდ ინფორმაცია მისი ქალაქის, უბნის, კორპუსის და სართულის შესახებ და შევინახოდ ცალცალკე ცვლადებში და გამოვიტანოთ ტერმინალში სრული მისამართი

city = input("your city: ")
district = input("your district: ")
flat = input("yout flat: ")
floor = input("your floor: ")

print(f"city you live in {city} your district number {district} flat you live in {flat} floor you live at {floor}")

#  მომხმარებელს შემოატანინეთ ასაკი და f სტრინგის გამოყენებით დაუბეჭდეთ წინადადება

age = input("your age") 

print(f"you are {age} years old")



num1 = input("enter your number")
num2 = input("enter your number ")
print(num1 + num2)
print(num1 * num2)
print(num1 % num2)

#ასეთი შედეგი იმიტომ მივიღეთ რომ ჩვენ არ შეგვიძლია სტრინგი ფგავამრავლოთ ან გავყოთ სტრინგზე და საბოლოო ჯამში არ შეგვიძლია გამოვიყენოთ მატემატიკური ოპერატორები მიმატერბის გარდა