from art import logo

print(logo)

bids = {}

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid price? $ "))

    bids[name] = bid

    answer = input("Is there any other user who want to bid? 'yes' or 'no' ")
    if answer == 'no':
        break


def highest_bidder(bids_dict):
    index = list(bids_dict.keys())[0]
    for key in bids_dict:
        index = key if bids_dict[key] > bids_dict[index] else index
    return bids_dict[index], index


value, name = highest_bidder(bids)

print(f"The highest bid is equal to {value} created by {name}")
