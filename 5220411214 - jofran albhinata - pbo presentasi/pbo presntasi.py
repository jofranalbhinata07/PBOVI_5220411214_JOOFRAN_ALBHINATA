class HewanTernak:
    def __init__(self, nama, jenis, harga):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga

    def get_nama(self):
        return self.nama

    def get_jenis(self):
        return self.jenis

    def get_harga(self):
        return self.harga

    def set_nama(self, nama):
        self.nama = nama

    def set_jenis(self, jenis):
        self.jenis = jenis

    def set_harga(self, harga):
        self.harga = harga

    def hitung_total_harga(self, jumlah):
        return self.harga * jumlah


class Sapi(HewanTernak):
    def __init__(self, nama, jenis, harga, warna):
        super().__init__(nama, jenis, harga)
        self.warna = warna

    def get_warna(self):
        return self.warna

    def set_warna(self, warna):
        self.warna = warna

    def hitung_total_harga(self, jumlah):
        # override method hitung_total_harga
        return super().hitung_total_harga(jumlah) * 2


class Kambing(HewanTernak):
    def __init__(self, nama, jenis, harga, berat):
        super().__init__(nama, jenis, harga)
        self.berat = berat

    def get_berat(self):
        return self.berat

    def set_berat(self, berat):
        self.berat = berat

    def hitung_total_harga(self, jumlah):
        # override method hitung_total_harga
        if self.berat > 100:
            return super().hitung_total_harga(jumlah) * 1.5
        else:
            return super().hitung_total_harga(jumlah)


class KambingEtawa(Kambing):
    def __init__(self, nama, jenis, harga, berat, jenis_kambing):
        super().__init__(nama, jenis, harga, berat)
        self.jenis_kambing = jenis_kambing

    def get_jenis_kambing(self):
        return self.jenis_kambing

    def set_jenis_kambing(self, jenis_kambing):
        self.jenis_kambing = jenis_kambing

    def hitung_total_harga(self, jumlah):
        # override method hitung_total_harga
        if self.jenis_kambing == "Etawa":
            return super().hitung_total_harga(jumlah) * 1.2
        else:
            return super().hitung_total_harga(jumlah)


# deklarasi objek
sapi = Sapi("Sapi Jantan", "Sapi Madura", 1000000, "Hitam")
kambing = Kambing("Kambing Betina", "Kambing Etawa", 500000, 70)
kambing_etawa = KambingEtawa("Kambing Etawa Jantan", "Kambing", 600000, 80, "Etawa")

# hitung total harga
total_harga_sapi = sapi.hitung_total_harga(3)
total_harga_kambing = kambing.hitung_total_harga(2)
total_harga_kambing_etawa = kambing_etawa.hitung_total_harga(1)

# cetak total harga
print("Total harga sapi:", total_harga_sapi)
print("Total harga kambing:", total_harga_kambing)
print("Total harga kambing etawa:", total_harga_kambing_etawa)
