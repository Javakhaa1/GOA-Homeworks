# # დავალება 3: ასაკის შეჯერება დღის მონაკვეთთან
# შეიყვანოს მომხმარებელმა ასაკი და საათი (0-დან 23-მდე). პროგრამამ განსაზღვროს:

# თუ ასაკი < 18 და დრო ≥ 22 → "დროა დაძინების"

# თუ ასაკი ≥ 60 და დრო ≥ 21 → "დასვენება რეკომენდებულია"

# სხვა შემთხვევაში → "შეგიძლიათ გააგრძელოთ აქტივობა"

age = int(input("შეიყვანეთ თქვენი ასაკი: "))
clock = int(input("შეიყვანეთ რომელი საათია: "))

if age < 18 and clock >= 22:
    print("დროა დაძინების")
elif age >= 60 and clock >= 21:
    print("დასვენება რეკომენდირებულია")
else:
    print("შეგიძლიათ გააგრძელოთ აქტივობა")


