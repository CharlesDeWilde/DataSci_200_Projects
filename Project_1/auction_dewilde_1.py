#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
This module defines the Auction and User classes for the second-price auction simulation.
"""

import random

# pylint: disable=too-few-public-methods
class User:
    """
    Represents a website visitor with a secret probability of clicking an ad.
    """
    def __init__(self):
        """
        Initializes a User with a random click probability between 0 and 1.
        """
        self.__probability = random.uniform(0, 1)

    def show_ad(self) -> bool:
        """
        Simulate showing an ad to the user.

        Returns:
            bool: True if the user clicks the ad, otherwise False.
        """
        return random.random() < self.__probability


# pylint: disable=too-few-public-methods
class Auction:
    """
    Manages auction rounds for a second-price auction.
    """
    def __init__(self, users, bidders):
        """
        Initializes the auction with a list of users and bidders.
        Also sets up a dictionary to track each bidder's balance.

        Args:
            users (list): A list of User objects.
            bidders (list): A list of Bidder objects.
        """
        self.users = users
        self.bidders = bidders
        self.balances = {bidder: 0 for bidder in bidders}

    def execute_round(self) -> None:
        """
        Execute one auction round:
        
        1. Select a random user.
        2. Collect bids from each bidder.
        3. Determine the winning bidder and calculate the second-highest bid.
        4. Show the ad to the selected user and record the click outcome.
        5. Notify all bidders about the outcome.
        6. Update the winning bidder's balance.
        """
        # 1. Select a random user and determine its user_id.
        user = random.choice(self.users)
        user_id = self.users.index(user)

        # 2. Solicit bids from each bidder.
        bids = {}
        for bidder in self.bidders:
            bid_amount = bidder.bid(user_id)
            # Ensure bid is non-negative and round to three decimals.
            bid_amount = round(max(bid_amount, 0.0), 3)
            bids[bidder] = bid_amount

        # 3. Determine the winning bidder and the winning price.
        highest_bid = max(bids.values())
        highest_bidders = [
            bidder for bidder, amount in bids.items() if amount == highest_bid
        ]
        winner = random.choice(highest_bidders)

        # Calculate winning price: if tie, winning price equals the highest bid.
        if list(bids.values()).count(highest_bid) > 1:
            winning_price = highest_bid
        else:
            remaining_bids = list(bids.values())
            remaining_bids.remove(highest_bid)
            winning_price = max(remaining_bids) if remaining_bids else 0.0

        # 4. Show the ad and record if the user clicked.
        clicked = user.show_ad()

        # 5. Notify each bidder of the outcome.
        for bidder in self.bidders:
            if bidder == winner:
                bidder.notify(auction_winner=True, price=winning_price, clicked=clicked)
            else:
                bidder.notify(auction_winner=False, price=winning_price, clicked=None)

        # 6. Update the winning bidder's balance.
        self.balances[winner] += (1 if clicked else 0) - winning_price

