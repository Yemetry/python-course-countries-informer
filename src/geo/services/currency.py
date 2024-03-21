from typing import Optional

from geo.clients.currency import CurrencyClient
from geo.clients.shemas import CurrencyRatesDTO


class CurrencyService:


    def get_currency(self, base: str) -> Optional[CurrencyRatesDTO]:

        data = CurrencyClient().get_rates(base)
        if data:
            return CurrencyRatesDTO(
                base=data["base"],
                date=data["date"],
                rates=data["rates"],
            )

        return None