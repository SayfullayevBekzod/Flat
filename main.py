from manager import Manager

kv = Manager()

flat1 = kv.newFlat("A1", 75)
#flat2 = kv.newFlat("B2", 100)
#print(flat1.getCode())
#print(flat1.getDimention())

#client1 = kv.newClient('Ali', 'Valiyev', 1)
#client2 = kv.newClient('Vali', 'Aliyev', 2)
#print(kv.getClient(1))
#kv.getClietnts()
#print(client2.getName())
#print(client1.getSurname())
#print(client1.getId())
kv.newClient('Ali', 'Valiyev',12)
print(kv.bookFlat('A1', 12, 12, 10, 2006, 2, 100))