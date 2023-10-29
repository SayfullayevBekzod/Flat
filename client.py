class Client:
    def __init__(self, ism, familya, id) -> None:
        self._ism = ism
        self._familya = familya
        self._id = id
        
    @property
    def ism(self):
        return self._ism
    
    @property
    def familya(self):
        return self._familya
    
    @property
    def id(self):
        return self._id
    
    def getName(self):
        return f'{self._id}: {self._ism} {self.familya}'
    
    def getSurname(self):
        return f'{self._id}: {self._ism} {self.familya}'
    
    def getId(self):
        return f'{self._id}: {self._ism} {self.familya}'
    
    def __str__(self):
        return f'Mijoz -- {self._id}: {self._familya} {self._ism}'
