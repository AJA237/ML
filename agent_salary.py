# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 06:59:48 2023

@author: Acer
"""


class AgentSalary:
    """"""

    def __init__(self, agent, month):
        self.agent = agent
        self.month = month
        self.books = None
        self.m_books = None

    def get_agent_booking(self, bookings):
        self.books = [book for book in bookings if self.agent in book.agents]

    def get_monthly_booking(self, date):
        date = date.dt.strftime("%Y-%m")

    def residence(self):
        residence_bookings = [book for book in self.books if book.type == "residence"]
        return residence_bookings

    def commercial(self):
        commercial_bookings = [book for book in self.books if book.type == "commercial"]
        return commercial_bookings

    # def res_bonus(self):
        # result =
