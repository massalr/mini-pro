class Item:
    
    def __init__(self, nama, harga, kuantiti):
        self.nama = nama # atribut
        self.harga = harga # atribut
        self.kuantiti = kuantiti # atribut

    def hitung_total_harga(self, x, y ): # disebut method jika def di dalam class dan didalam tanda kurung adalah parameter argumen
        return x * y


item1 = Item("teh", 20, 4)

item2 = Item("kopi", 25, 3)

print(item1.nama)
print(item1.harga)
print(item2.kuantiti)