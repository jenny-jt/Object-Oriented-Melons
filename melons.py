"""Classes for melon orders."""
import random
from datetime import date

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from"""
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        #self.country_code = None

    def get_base_price(self):
        # random_num = random.choice
        # print(random_num)
        print((2020, 10, 9).isoweekday())
        #print(date.isoweekday())
        #datetime.isofweekday()
        #datetime.hour() 
        self.base_price = random.randrange(5,9)
        #if ...

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price

        return total
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

# class AddedFee:
#     def added_fee(self):
#         if self.qty < 10:
#             new_total = total + 3
        
#         return new_total

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
    
    # country_code = country_code

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code
        
    def get_total(self):
        """Calculate price, including tax and added fee"""
        
        total = super().get_total()
        # base_price = 5 * 1.5
        # total = (1 + self.tax) * self.qty * base_price
        new_total = total + 3
        
        return new_total
        
    #     """Initialize melon order attributes."""
    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        if passed:
            self.passed_inspection = True
