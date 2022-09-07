# ini adalah simulasi tabungan di bank

class RekeningBank:
    
    def __init__(self, tabungan):
        self.tabungan = tabungan

    def cek_saldo(self):
        print("jumlah saldo anda saat ini = Rp {}".format(self.tabungan))

    def menabung(self):
        tambah = float(input("masukan jumlah uang : "))
        self.tabungan += tambah

    def menarik(self):
        kurang = float(input("masukan jumlah yang ingin di tarik : "))
        if self.tabungan < kurang:
            print("mahaf saldo anda tidak cukup, saldo anda saat ini Rp {}".format(self.tabungan))
        else:
            self.tabungan -= kurang

tabunganku = RekeningBank(100000000)
tabunganku.cek_saldo()
tabunganku.menabung()
tabunganku.cek_saldo()
tabunganku.menarik()
tabunganku.cek_saldo()

