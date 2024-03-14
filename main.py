from art import logo

print(logo)
print("Welcome to the silent auction!")

bidding_list = []

bidding = True
while bidding:
    name = input("Enter your name: ")
    amount = input("Enter the amount you would like to bid for this object: $")

    information_dict = {
        "name": name,
        "amount": amount
    }

    bidding_list.append(information_dict)
    decision = input("Are there more bidders? y/n ")
    if decision == "n":
        bidding = False
    for i in range(0, 50):
        print("\n")


highest_amount = 0
highest_bidder = ""

for i in bidding_list:
    if int(i["amount"]) > highest_amount:
        highest_amount = int(i["amount"])
        highest_bidder = i["name"]

print(f"The highest bidder was {highest_bidder} with ${highest_amount}")