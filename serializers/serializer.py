import json
from constants import ALLOWED_CURRENCIES


class CryptoSerializerWzrx:
    """
    Serializes the incoming crypto dict data
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

    Wzrx data looks like:
    {
    dock": {
        "btc": "0.0000020432957808703335",
        "eur": "0.092384745",
        "idr": "1602.1296",
        "inr": "9.01",
        "ngn": "45.361234914",
        "rub": "8.322502389",
        "sar": "0.416276529",
        "try": "0.924363489",
        "uah": "3.086746608",
        "usdt": "0.111",
        "wrx": "0.04631503402694617"
            },
        "doge": {
        "btc": "0.000010374788307193874",
        "eur": "0.469081462",
        "idr": "8134.77696",
        "inr": "44.4868",
        "ngn": "230.32064862640001",
        "rub": "42.2573184364",
        "sar": "2.1136347004",
        "try": "4.693434796399999",
        "uah": "15.6728863808",
        "usdt": "0.5636",
        "wrx": "0.23655"
            }
        }

    Functionality
    -> Each provider will have a unique serializer, since the data structure might be different
    -> Serializes the data in the requied above format
    """

    raw_data = None
    data = None

    def __init__(self, data):
        data = json.loads(data) if isinstance(data, str) else data
        self.raw_data = data
        self.validate_data()
        self.convert_to_structure()

    def validate_data(self):
        """
        Validates the data, for required fields
        """
        pass

    def convert_to_structure(self):
        """
        Converts the dict to the required structure
        """
        raw_data = self.raw_data
        data = {}
        for currency in list(ALLOWED_CURRENCIES):
            if currency in raw_data:
                data[currency] = ALLOWED_CURRENCIES[currency]
                data[currency]['rates'] = raw_data[currency]

        self.data = data
