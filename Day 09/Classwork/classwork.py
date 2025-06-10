# მომხმარებელს შემოატანინეთ სამი რიცხვი, start/end/step და ჩასვით for loop-ში სათანადო ადგილას.

start = int(input("გთხოვთ შემოიყვანეთ ნებისმიერი რიცხვი:  "))
end = int(input("გთხვთ შემოიყვანეთ ნებისმიერი რიცხვი:  "))
step = int(input("გთხოვთ შემოიყვანეთ ნებისმიერი რიცხვი:  "))

for i in range (start, end, step):
    print(i)

# მომხმარებელს შემოატანინეთ რიცხვი და დაპრინტეთ რიცხვი ყოველ იტერაციაზე იქამდე, სანამ რიცხვი მომხმარებლის რიცხვს არ გაუტოლდება (While loop )

user_number = int(input("შეიყვანეთ რიცხვი: "))

i = 0

while i <= user_number:
    print(i)
    i += 1

# გააკეთეთ {2.} classwork For loop-ის გამოყენებით

user_number1 = int(input("შეიყვანეთ რიცხვი: "))
for i in range(0, user_number1 + 1):
    print(i)