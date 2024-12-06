# if B>150000 && P=Himalayas(adventure) or Paris(relaxation)
# if B<150000 && P=Waynad(adventure) or Goa(relaxation)

budget = int(input("Enter your budget: "))
preference = input("Enter preference: (Adventure or Relaxation) -> ").lower()

if budget > 150_000:
    if preference == "adventure":
        print("You can go to Himalayas")
    else:
        print("You can go to Paris")
elif budget < 150_000:
    if preference == "adventure":
        print("You can go to Waynad")
    else:
        print("You can go to Goa")