import typing
from constants import ALLOWED_CURRENCIES, BASE_CURRENCY, CurrencyVars


class CryptoUtils:
    """
    This service needs structure in this format
    {
    "btc": {
        "symbol": "btc",
        "name": "bitcoin",
        "rates": {
            "inr": "49.6",
            "btc": "0.00005"
            }
        }
    }


    Handles services like:
        -> Store Data
        -> push data to other destinations
        -> Take actions based on other triggers
    """

    CURRENCY_DATA = None

    def __init__(self, data):
        self.set_allowed_currencies(data=data)

    def process_tasks(self):
        """
        This will called to trigger all the tasks related to the specific / all currency
        """
        self.task_print_dogecoin_rate()

    def validate_data(self, data) -> dict:
        """
        Validates the data structure
        """
        pass

    def set_allowed_currencies(self, data: dict) -> typing.Tuple[bool, str]:
        """
        Sets self.CURRENCY_DATA to only allowed currencies
        Currently using this method to validate also, since not much validation is required!
        """
        updated_data = {}
        for currency in ALLOWED_CURRENCIES:
            updated_data[currency] = data[currency]

        self.CURRENCY_DATA = updated_data
        return True, ""

    def get_currency_data(self, currency: str) -> dict:
        """
        Returns the dict for the currency (including the rate dict)
        """
        return self.CURRENCY_DATA[currency]

    def get_currency_rate_dict(self, currency: str) -> dict:
        """
        Returns the currency rate
        """
        return self.CURRENCY_DATA[currency]['rates']

    def get_currency_rate(self, currency: str, exchange_currency: str = BASE_CURRENCY) -> float:
        """
        Returns exchange value for the given currency, to BASE_CURRENCY by default
        """
        return float(self.CURRENCY_DATA[currency]['rates'][exchange_currency])

    def task_print_dogecoin_rate(self):
        """
        Just a sample task function that prints doge rate in INR when fetched
        """

        price = self.get_currency_rate(currency=CurrencyVars.DOGE)
        print("DOGE -> {} INR".format(price))
        return True

