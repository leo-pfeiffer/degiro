import datetime
from django.db import models


class DepotManager(models.Manager):

    def get_latest_portfolio(self):
        """
        Return the latest portfolio.
        """
        if not self.exists():
            return self.none()

        return self.filter(date=self.latest('date').date)

    def get_portfolio_at_date(self, date: datetime.date):
        """
        Return the portfolio on a given date.
        """
        if not self.exists():
            return self.none()

        return self.filter(date=date)

    def get_latest_date(self):
        """
        Return the date of the latest portfolio.
        """
        if not self.exists():
            return None
        return self.latest('date').date
