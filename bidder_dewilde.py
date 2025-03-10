#!/usr/bin/env python
# coding: utf-8
"""
This file defines my bidder for our auction simulation.
I have added logic to learn from past rounds and adjust my bid accordingly.
If my balance is in the red, I bid minimally to avoid further losses.
"""

class Bidder:
    """
    A bidder that adapts its bid based on previous rounds.
    """
    def __init__(self, num_users, num_rounds):
        """
        Set up the bidder with the auction settings.
        
        Args:
            num_users (int): The total number of users in the auction.
            num_rounds (int): The total number of auction rounds.
        
        I also keep track of my own balance and record the winning prices from each round.
        """
        self.num_users = num_users
        self.num_rounds = num_rounds
        self._balance = 0.0  # My current balance; starts at 0.
        self._winning_prices = []  # Memory of winning prices to adapt bids.

    def bid(self, _user_id) -> float:
        """
        Decide how much to bid based on what I've learned from previous rounds.
        
        Strategy:
          - If my balance is negative, bid minimally (0.0) to avoid further losses.
          - In the first round, bid $1.00.
          - Otherwise, calculate the average winning price from history and add $0.01.
          - Also, ensure I never bid more than my current balance.
        
        Args:
            _user_id (int): The user I'm bidding for.
        
        Returns:
            float: The bid amount, rounded to three decimal places.
        """
        # If I'm in the red, bid nothing (or a minimal amount)
        if self._balance < 0:
            return 0.0

        # If no history, start with $1.00.
        if not self._winning_prices:
            return 1.0

        # Otherwise, use the average winning price plus a small increment.
        avg_price = sum(self._winning_prices) / len(self._winning_prices)
        bid_amount = avg_price + 0.01
        # Do not bid more than the balance I have.
        bid_amount = min(bid_amount, self._balance)
        return round(bid_amount, 3)

    def clicked(self, auction_winner, price, clicked=None) -> None:
        """
        Update my records after each auction round.
        
        I record the winning price to adjust future bids.
        If I win the round, update my balance by adding $1 (if the ad was clicked)
        and subtracting the price paid.
        
        Args:
            auction_winner (bool): True if I won this round.
            price (float): The winning price (the second-highest bid).
            clicked (bool, optional): True if the ad was clicked (only matters if I won).
        """
        self._winning_prices.append(price)
        if auction_winner:
            gain = 1 if clicked else 0
            self._balance += gain - price

