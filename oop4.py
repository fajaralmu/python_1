class Karyawan:
    nama_perusahaan = 'ABC'
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan):
        self.__nama = nama
        self.__usia = usia
        self.__pendapatan = pendapatan
        self.pendapatan_tambahan = 0
    def lembur(self):
        insentif_lembur = self.insentif_lembur
        if self.__usia > 30:
            insentif_lembur *= 2
        self.pendapatan_tambahan += insentif_lembur
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek
    def total_pendapatan(self):
        return self.__pendapatan + self.pendapatan_tambahan

karyawan_1 = Karyawan('Kiki', 35, 8000000)
karyawan_1.lembur()
karyawan_1.tambahan_proyek(karyawan_1.total_pendapatan())
print(karyawan_1.total_pendapatan())