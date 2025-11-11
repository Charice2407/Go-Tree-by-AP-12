# buat tampilan data kunjungan
class Kunjungan:
    def __init__(self,  id, kelamin, lokasi, tanggal_pengunjungan):
        self.id = id
        self.kelamin = kelamin
        self.lokasi = lokasi
        self.tanggal_pengunjungan = tanggal_pengunjungan
    def Tampilkan_data(self, nomor):
        print(f"| {nomor:<3} | {self.id:<15} | {self.kelamin:<5} | {self.lokasi:<20} | {self.tanggal_pengunjungan:<15} |")

class Pohon(Kunjungan):
    def __init__(self, id, kelamin, lokasi, tanggal_pengunjungan, kondisi_pohon):
        super().__init__(id, kelamin, lokasi, tanggal_pengunjungan)
        self.kondisi_pohon = kondisi_pohon

    def KondisiPohon(self, kondisi_pohon):
        if self.kondisi_pohon.lower() == "subur":
            return "Sehat"
        elif self.kondisi_pohon.lower() == "layu" and "kering":
            return "Tidak Sehat"    
        else:
            return "Unknown"
        
        
    def Tampilkan_data(self, nomor):
        super().Tampilkan_data(nomor)
        print(f"    >> {self.KondisiPohon(self.kondisi_pohon)}")
        
data_kunjungan = []
print("=== SISTEM DATA KUNJUNGAN POHON ===\n")
jumlah = int(input("masukkan jumlah kunjungan: "))
for kunjungan in range(jumlah):
    print(f'\nKunjungan ke --{kunjungan+1}--')
    id = input("ID Pengunjung: ")
    kelamin = input("Jenis Kelamin (L/P): ")
    lokasi = input("Lokasi Pengunjungan: ")
    tanggal_pengunjungan = input("Tanggal Pengunjungan (DD-MM-YYYY): ")
    kondisi_pohon = input("Kondisi Pohon (Subur/Layu/Kering): ")
    kunjungan = Pohon(id, kelamin, lokasi, tanggal_pengunjungan, kondisi_pohon)
    data_kunjungan.append(kunjungan)

print("\n=== DAFTAR KUNJUNGAN POHON ===\n")
print("========================================================================================")   
print("| No | ID Pengunjung  | JK   | Lokasi              | Tanggal          |")
print("========================================================================================")
for i, kunjungan in enumerate(data_kunjungan, start=1):
    kunjungan.Tampilkan_data(i)
print("========================================================================================")


