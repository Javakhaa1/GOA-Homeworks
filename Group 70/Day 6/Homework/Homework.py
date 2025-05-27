# 2) კომენტარებით ახსენით რა არის sequences, iteration და selection. მოიყვანეთ მათი მაგალითები

# Sequence-ის მაგალითი .. :Sequenece არის რაც მიყოლებით ხდება 
print("გაღვიძება")
print("ჩაცმა")
print("კბილების გახეხვა")


# Iteration ნიშნავს ერთი და იგივე მოქმედების რამოდენიმეჯერ გამეორებას


#selection აქ გაქვს არჩევნის საშუალება 

# 3) კომენტარებით ახსენით, რა არის ალგორითმი და ჩამოთვალეთ რა გზები არსებობს მის წარმოსადგენად.

#ალგორითმი მაგალითები: როდესაც შენ გინდა გაიკეთო მაგალითად ჩაი
# 1)ჩაასხი წყალი ქვაბში
# 2)დადგი გაზზე
# 3)მოადუღე
# 4)ჩაყარე ჩაი
# 5)დაელოდე რამდენიმე წუთი
# 6)ჩაასხი ფინჯანში 
# ეს არის ჩაის გაკეთების ალგორითმი 

# 4) შეეცადეთ თქვენით მიხვდეთ, თუ რა პასუხს გამოიტანს შემდეგი კოდი:

print(True or False and False or True and False or False and False or False and True and False or True)
print(5 > 10 or 7 * 7 / 7 == 7 and False or True and "1234" != "1234" and 7 + 3 * 3 + 1 == 15 and True and True or 100 > 100 or True)

# 5) მომხმარებელს შემოატანინეთ რიცხვი და თუ ის არის ლუწი და არის 10-ზე მეტი, ან ტოლია 7-ის, დაბეჭდეთ True

number = int(input("Please enter a number: "))

if number >= 10 or 7:
    print("True")

# 6) ივარჯიშეთ შემდეგ ფუნქციებზე: int, str, float, bool. თითოეულზე გააკეთეთ 3-3 მაგალითი

number1 = int(5)
num = int(5 + 5 * 100)
num2 = int(5 + 5 * 100 / 10)

Name = str(input("please enter your name:        "))
Surname = str(input("please enter your surname   "))
Nickname = str(input("Please enter your nickname "))

float0 = float(input("Please enter your kg"))
float1 = float(input("Please enter your sm"))
float2 = float(input("Please enter your "))

# 7) მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ, თუ ის არის ნაკიანი დაბეჭდეთ "This is leap year".(ნაკიანი წელიწადი იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე)

year = int(input("Please enter your Year of Birth:  "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
    print("This is leap year")
   
  

