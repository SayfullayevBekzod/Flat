class Bookings:
    def __init__(self, code, client_id, day, month, year, week, price) -> None:
        self._code = code
        self._client_id = client_id
        self._day = day
        self._month = month
        self._year = year
        self._week = week
        self._price = price
        
    @property
    def code(self):
        return self._code
    
    @property
    def client_id(self):
        return self._client_id
    
    @property
    def day(self):
        return self._day
    
    @property
    def month(self):
        return self._month
    
    @property
    def year(self):
        return self._year
    
    @property
    def week(self):
        return self._week
    
    @property
    def price(self):
        return self._price
    
    def __str__(self):
        return f'{self._code} dagi kvartiraga\n{self._client_id} idlik mijoz\n{self._day}/{self._month}/{self._year} vaqti\n{self._week} haftaga\nNarxi -- {self._price} '