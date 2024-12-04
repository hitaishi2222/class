budget = int(input("Enter your budget: "))
preference = input("Enter your preference (Adventure/Relaxation): ").lower()

if budget > 150_000:
    if preference == "adventure":
        print("Your destination suggestion is : Himalayas")
    elif preference == "relaxation":
        print("Your destination suggestion is : Paris")
    else:
        print("Enter correct preference")
elif budget <= 150_000 and budget > 0:
    if preference == "adventure":
        print("Your destination suggestion is : Waynad")
    elif preference == "relaxation":
        print("Your destination suggestion is : Goa")
    else:
        print("Enter correct preference")
elif budget < 0:
    print("enter correct budget")
    