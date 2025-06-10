# შექმენით პროგრამა რომელიც მიიღებს მომხარებლისგან input-ს რიხვის სახით და დაბეჭდეთ ამ რიცხვამდე ყველა რიცხვი თანმიმდევრობით. (For loop)

num1 = int(input("გთხოვთ შეიყვანოთ რიცხვი"))
for i in range(1, num1):
    print(i)

num2 = int(input("გთხოვთ შეიყვანოთ რიცხვი"))
count = 0
while count <= num2:
    print(count)
    count += 1 