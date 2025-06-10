# 4)დაწერე პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. სწორი პაროლია "python123". სანამ სწორად არ შეიყვანს, მოთხოვე თავიდან.

correct_password = "python123"

while True:
    password = input("Please enter password: ")
    if password == correct_password:
        print("Succseasful")
        break
    else:
        print("Wrong password try again")
