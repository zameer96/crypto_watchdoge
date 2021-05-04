import typing
import requests
from serializers import CryptoSerializerWzrx
from utils import CryptoUtils


def get_crypto_market_data_from_wzrx():
    """
    This task will be called every N minutes
    -> Fetches the market data
    -> Serializes it
    -> Processes the defined tasks in CryptoUtils.process_tasks()
    """
    url = "https://x.wazirx.com/wazirx-falcon/api/v2.0/crypto_rates"
    res = requests.get(url=url)
    if res.status_code != 200:
        return None
    data = res.json()
    return data


def process_tasks():
    data = get_crypto_market_data_from_wzrx()
    data = CryptoSerializerWzrx(data=data).data
    crypto = CryptoUtils(data=data)
    crypto.process_tasks()


