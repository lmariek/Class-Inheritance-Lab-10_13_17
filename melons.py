"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """A melon order within the USA."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas melons":
            base_price = 7.5
        else:
            base_price = 5

        if self.order_type == "international" and self.qty < 10:
            total = ((1 + self.tax) * self.qty * base_price) + 3
        else:
            total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize domestic melon order attributes."""

        super(DomesticMelonOrder, self).__init__(species, qty, 'domestic', 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize international melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty,
                                                    'international',
                                                    0.17)
        self.country_code = country_code

    def get_country_code(self):

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government-inspected melon order."""

    def __init__(self, species, qty):
        """Initialize domestic melon order attributes."""

        super(GovernmentMelonOrder, self).__init__(species, qty, 'government', 0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Record the fact than an order has been inspected."""

        if passed:
            self.passed_inspection = True
        else:
            self.passed_inspection = False