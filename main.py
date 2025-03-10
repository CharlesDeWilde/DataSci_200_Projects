#!/usr/bin/env python
# coding: utf-8
"""
Main file to test the auction simulation.
This file creates a set of Users, Bidders, and runs the Auction for a number of rounds.
"""

from auction_dewilde import User, Auction
from bidder_dewilde import Bidder

def main():
    # Parameters for the simulation
    num_users = 100
    num_bidders = 20
    num_rounds = 150

    # Create a list of Users.
    users = [User() for _ in range(num_users)]
    
    # Create a list of Bidder instances.
    bidders = [Bidder(num_users, num_rounds) for _ in range(num_bidders)]
    
    # Create an Auction instance.
    auction = Auction(users, bidders)
    
    # Execute multiple rounds of the auction.
    for _ in range(num_rounds):
        auction.execute_round()
    
    # Print final bidder balances.
    # Note: I know _balance is a private attribute; bu here it's accessed for testing purposes to see how my bidder and auction classes do
    print("Final Bidder Balances:")
    for i, bidder in enumerate(bidders):
        print(f"Bidder {i + 1}: Balance = {bidder._balance:.3f}")

if __name__ == "__main__":
    main()