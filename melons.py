"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly

    # order_type = None
    # # tax = 0

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
    

    def get_total(self):
        
        """Calculate price, including tax."""
        base_price = 5
        if self.species == "Christmas melon":
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        
        """Record the fact than an order has been shipped."""

        self.shipped = True 
        



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""


    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code


class GovernmentMelonOrder(AbstractMelonOrder):

    order_type = "government"
    tax = 0.0
    

    def __init__(self, species, quantity):
        super().__init__(species, quantity)
        self.passed_inspection = False

    def mark_inspection(self, passed):

        self.passed_inspection = passed
        
        
    def get_country_code(self):
        """Return the country code."""

        return self.country_code