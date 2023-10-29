class Flat:
    def __init__(self, kod, maydon):
        self._kod = kod
        self._maydon = maydon
        
    @property
    def kod(self):
        return self._kod
    
    @property
    def maydon(self):
        return self._maydon

    def getCode(self):
        return f'Kodi -- {self._kod}'

    def getDimention(self):
        return f'Maydoni -- {self._maydon}'