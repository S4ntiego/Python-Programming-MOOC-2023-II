# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents

    def __ne__(self, another):
        return self.__euros != another.__euros or self.__cents != another.__cents

    def __gt__(self, another):
        return self.__euros > another.__euros or self.__cents > another.__cents

    def __lt__(self, another):
        return self.__euros < another.__euros or self.__cents < another.__cents

    def __add__(self, another):
        total_euros = self.__euros + another.__euros
        total_cents = self.__cents + another.__cents
        if total_cents >= 100:
            total_euros += 1
        total_cents = total_cents % 100
        return Money(total_euros, total_cents)

    def __sub__(self, another):
        total_euros = self.__euros - another.__euros
        total_cents = self.__cents - another.__cents
        if total_cents < 0:
            total_euros -= 1
        if total_euros < 0:
            raise ValueError("A negative result is not allowed")
        total_cents = total_cents % 100
        return Money(total_euros, total_cents)
