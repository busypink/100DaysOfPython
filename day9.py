print("welcome to the silent auction simulator")
bids = {}
bidding_end = False


def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_end:
    name = input("Name:")
    price = int(input("What's your bid? $"))
    bids[name] = price
    bidding_status = input("are there any other bidders? Type 'yes' or 'no':")
    if bidding_status == "no":
        bidding_end = True
        highest_bidder(bids)
