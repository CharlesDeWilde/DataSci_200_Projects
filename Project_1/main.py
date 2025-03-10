#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from auction_DeWilde import Auction, User
from bidder_DeWilde import Bidder

if __name__ == "__main__":
    # Set the parameters for testing.
    num_rounds = 10  # Total number of auction rounds.
    num_users = 7    # Total number of users.
    num_bidders = 5  # Total number of bidders.

    # Create a list of bidders and users.
    bidders = [Bidder(num_users, num_rounds) for _ in range(num_bidders)]
    users = [User() for _ in range(num_users)]
    
    # Set up the auction with the generated users and bidders.
    auction = Auction(users, bidders)
    
    # Run the auction for the specified number of rounds.
    for round_number in range(num_rounds):
        print(f"Round {round_number + 1}:")
        auction.execute_round()
        
        # Print the balances for each bidder.
        for bidder, balance in auction.balances.items():
            print(f"{bidder} balance: {balance:.3f}")
        print("-" * 40)

