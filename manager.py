from flat import Flat
from client import Client
from bookings import Bookings
class Manager:
    def __init__(self) -> None:
        self._flat_list: list[Flat] = []
        self._client_list: list[Client] = []
    
    def newFlat(self, kod: Flat, maydon: Flat):
        flat = Flat(kod, maydon)
        print('Kvartira yaratildi!!..')
        return flat
    
    def getFlat(self, kod: Flat):
        for flat in self._flat_list:
            if flat._kod == kod:
                return flat
                
    def newClient(self, ism: Client, familya: Client, id: Client):
        for client in self._client_list:
            if client.id == id:
                print('Mijoz mavjud')
                return None
        client = Client(ism, familya, id)
        self._client_list.append(client)
        print('Mijoz yaratildi!!..')
        return client
    
    def getClient(self, id: Client):
        for client in self._client_list:
            if client._id == id:
                return client
        return f'Bu {id} id lik mijoz mavjud emas!!..'
    
    def getClients(self):
        return self._client_list
    
    def bookFlat(self, code, client_id, day, month, year, week, price):
        bookings = Bookings(code, client_id, day, month, year, week, price)
        return bookings