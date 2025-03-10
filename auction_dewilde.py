#!/usr/bin/env python
# coding: utf-8
"""
This file defines the Auction and User classes for the second-price auction simulation.
These classes simulate an online ad auction where bidders compete for ad space.
"""

import random

class User:
    """
    Represents a website visitor with a secret probability of clicking on an ad.
    """
    def __init__(self):
        """
        Initialize a User with a random click probability between 0 and 1.
        """
        self.__probability = random.uniform(0, 1)

    def show_ad(self) -> bool:
        """
        Simulate showing an ad to the user.
        
        Returns:
            bool: True if the user clicks the ad; otherwise, False.
        """
        return random.random() < self.__probability

    def get_probability(self) -> float:
        """
        Return the internal probability value for the user.
        """
        return self.__probability


class Auction:
    """
    Manages the auction rounds.
    Selects a random user, collects bids, determines the winner using second-price rules,
    and notifies each bidder of the outcome.
    """
    def __init__(self, users, bidders):
        """
        Initialize the auction with lists of users and bidders.
        
        Args:
            users (list): A list of User objects.
            bidders (list): A list of Bidder objects.
        """
        self.users = users
        self.bidders = bidders

    def execute_round(self) -> None:
        """
        Execute one round of the auction:
          1. Randomly select a user.
          2. Collect bids from each bidder.
          3. Determine the winner (with tie-breaking if necessary).
          4. Calculate the winning price (second-highest bid).
          5. Show the ad and record if the user clicks.
          6. Notify each bidder of the outcome.
        """
        # 1. Select a random user.
        user = random.choice(self.users)
        user_id = self.users.index(user)
        
        # 2. Collect bids from each bidder.
        bids = {}
        for bidder in self.bidders:
            bid_amount = bidder.bid(user_id)
            bid_amount = round(max(bid_amount, 0.0), 3)
            bids[bidder] = bid_amount
        
        # 3. Determine the highest bid and handle ties.
        highest_bid = max(bids.values())
        highest_bidders = [bidder for bidder, amount in bids.items() if amount == highest_bid]
        winner = random.choice(highest_bidders)
        
        # 4. Calculate the winning price.
        if list(bids.values()).count(highest_bid) > 1:
            winning_price = highest_bid
        else:
            remaining_bids = list(bids.values())
            remaining_bids.remove(highest_bid)
            winning_price = max(remaining_bids) if remaining_bids else 0.0
        
        # 5. Show the ad and check for a click.
        clicked = user.show_ad()
        
        # 6. Notify each bidder of the outcome.
        for bidder in self.bidders:
            if bidder == winner:
                bidder.clicked(auction_winner=True, price=winning_price, clicked=clicked)
            else:
                bidder.clicked(auction_winner=False, price=winning_price, clicked=None)
                
    def get_bidders(self):
        """
        Return the list of bidders.
        """
        return self.bidders
