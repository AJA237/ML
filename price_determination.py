# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 01:27:52 2023

@author: Acer
"""

from datetime import date, timedelta

list_trans = []
agent_count = 0
package = ("pickup", "pickup_cleanup")


class PriceDetermination:
    """Evaluate price based on volume for a pickup or a pickup and cleaning"""

    def __init__(self):
        self.volume = 0
        self.price = 0

    def calcul_volume(self, size, quantity):
        self.volume = (size/1000)*quantity
        return self.volume

    def calcul_price(self, package):
        price = self.volume * 0.05
        if package == "pickup":
            self.price = price
        else:
            self.price = 1.2 * price
        return self.price

    def bid(self, price):
        if price < self.price:
            return "Price is too low"
        else:
            return f"{self.price}"

price = PriceDetermination()
print(price.calcul_volume(1000, 10))
print(price.calcul_price("pickup"))
print(price.bid(1))