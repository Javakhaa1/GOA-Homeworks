# დავალება 2: წონის შეფასება ასაკის მიხედვით (უბრალოდ და ლოგიკურად)

Age = int(input("შეიყვანეთ თქვენი ასაკი: "))
KG = int(input("შეიყვანეთ თქვენი წონა: "))
if Age < 10:
    if KG < 20:
        print("წონა დაბალია")
    elif 20 <= KG <= 40:
        print("წონა ნორმალურია")
    else:
        print("წონა მაღალია")

elif Age >= 11 and Age < 17:
     if KG < 40:
       print("წონა დაბალია")
     elif KG > 40 and KG < 65:
       print ("წონა ნორმალურია")
     else:
         print("წონა მაღალია")

elif Age >= 18:
    if KG < 50:
       print("წონა დაბალია")
    elif KG > 50 and KG < 90:
        print("წონა ნორმალურია")
    else:
        print("წონა მაღალია")
