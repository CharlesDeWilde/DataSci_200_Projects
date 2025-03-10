#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
This module defines the Bidder class for the second-price auction simulation.
"""

# pylint: disable=too-few-public-methods
class Bidder:
    """
    Represents a bidder in the auction.
    """
    def __init__(self, num_users, num_rounds):
        """
        Initializes a bidder with the total number of users and auction rounds.

        Args:
            num_users (int): The total number of users.
            num_rounds (int): The total number of auction rounds.
        """
        self.num_users = num_users
        self.num_rounds = num_rounds

    def bid(self, _user_id) -> float:
        """
        Return a bid amount for the given user.
        
        Args:
            _user_id (int): The user identifier (unused in this simple strategy).
        
        Returns:
            float: A non-negative bid amount, rounded to three decimals.
        """
        return 1.0

    def notify(self, _auction_winner, _price, _clicked=None) -> bool:
        """
        Notifies the bidder about the auction round outcome.
        
        Args:
            _auction_winner (bool): True if this bidder won the round.
            _price (float): The winning price (the second-highest bid).
            _clicked (bool, optional): True if the ad was clicked (only relevant if won).
        
        Returns:
            bool: Always returns True.
        """
        return True

