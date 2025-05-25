# 1)დაწერე პროგრამა, რომელიც while ციკლით დაბეჭდავს რიცხვებს 1-დან 10-მდე.
num = 0 
count = 0
while count < 10:
    print(num + count + 1)
    count +=1

# 2)დაწერე პროგრამა, რომელიც დაბეჭდავს რიცხვებს 10-დან 1-მდე.

num1 = 10
while num1 >= 0:
    print(num1)
    num1 -=1

# 3)კომენტარებით ახსენი while loop.

# While Loop მუშაობს იქამდე სანამ არშესრულდება პირობა ან თუ არ აქვს სხეული უსასრულოდ დაიწერება 

# 4)დაწერე პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. სწორი პაროლია "python123". სანამ სწორად არ შეიყვანს, მოთხოვე თავიდან.

correct_password = "python123"

while True:
    password = input("Please enter password: ")
    if password == correct_password:
        print("Succseasful")
        break
    else:
        print("Wrong password try again")

    