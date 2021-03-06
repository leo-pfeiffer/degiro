import datetime
from typing import Union

from django.db import models
from django.db.models import QuerySet, F, Sum


class DepotManager(models.Manager):

    def get_latest_portfolio(self) -> QuerySet:
        """
        Return the latest portfolio.
        """
        if not self.exists():
            return self.none()

        return self.filter(symbol_date__date=self.latest('symbol_date__date').symbol_date.date)

    def get_portfolio_at_date(self, date: datetime.date) -> QuerySet:
        """
        Return the portfolio on a given date.
        """
        if not self.exists():
            return self.none()

        return self.filter(symbol_date__date=date).distinct().order_by('symbol_date__symbol')

    def get_latest_date(self) -> Union[datetime.date, None]:
        """
        Return the date of the latest portfolio.
        """
        if not self.exists():
            return None
        return self.latest('symbol_date__date').symbol_date.date

    def with_prices(self) -> QuerySet:
        """
        Return the Depot objects with prices.
        """
        if not self.exists():
            return self.none()

        return self.annotate(symbol=F('symbol_date__symbol'),
                             date=F('symbol_date__date'),
                             price=F('symbol_date__price__price')).values('symbol', 'date', 'pieces', 'price')

    def value_per_date(self) -> QuerySet:
        """
        Return the Depot value per date in order of date.
        """
        if not self.exists():
            return self.none()

        return self.with_prices().annotate(subtotal=F('pieces') * F('price')).values('date')\
            .annotate(total=Sum('subtotal')).order_by('date')


class DimensionSymbolDateManager(models.Manager):
    def get_existing(self, dates, symbols):
        if not self.exists() or len(dates) == 0 or len(symbols) == 0:
            return self.none()

        return self.filter(
            date__gte=min(dates),
            date__lte=max(dates),
            symbol__in=symbols
        ).values_list('id', 'symbol', 'date')


class CashflowManager(models.Manager):

    def get_existing(self, dates):
        if not self.exists():
            return self.none()

        return self.filter(date__in=dates).values('date', 'cashflow')
