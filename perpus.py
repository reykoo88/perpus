import json
from datetime import datetime, timedelta

class Perpustakaan:
    def __init__(self):
        self.mahasiswa = []
        self.katalog_buku = []
        self.transaksi = []

    def load_data(self):
        with open("data.json") as file:
            data = json.load(file)
            self.mahasiswa = data["mahasiswa"]
            self.katalog_buku = data["katalog_buku"]
            self.transaksi = data["transaksi"]

    def save_data(self):
        data = {
            "mahasiswa": self.mahasiswa,
            "katalog_buku": self.katalog_buku,
            "transaksi": self.transaksi
        }
        with open("data.json", "w") as file:
            json.dump(data, file)

    def get_mahasiswa_nama(self, npm):
        for mahasiswa in self.mahasiswa:
            if mahasiswa["npm"] == npm:
                return mahasiswa["nama"]
        return ""

    def is_mahasiswa_have_book(self, npm):
        for transaksi in self.transaksi:
            if transaksi["npm"] == npm and transaksi["status"] == "pinjam":
                return True
        return False

    def tampil_mahasiswa(self):
        print("\nSUB MENU: Tampil Mahasiswa")
        print("====================================")
        print("NPM\tNama")
        print("------------------------------------")
        for mahasiswa in self.mahasiswa:
            print(f"{mahasiswa['npm']}\t{mahasiswa['nama']}")
        print("------------------------------------")

    def tambah_mahasiswa(self):
        print("\nSUB MENU: Tambah Mahasiswa")
        print("====================================")
        npm = input("Masukkan NPM: ")
        nama = input("Masukkan Nama: ")

        if self.get_mahasiswa_nama(npm) == "":
            self.mahasiswa.append({"npm": npm, "nama": nama})
            print("Data mahasiswa berhasil ditambahkan.")
        else:
            print("Data dengan NPM tersebut sudah ada.")

    def edit_mahasiswa(self):
        print("\nSUB MENU: Edit Mahasiswa")
        print("====================================")
        npm = input("Masukkan NPM Mahasiswa: ")
        nama_mahasiswa = self.get_mahasiswa_nama(npm)

        if nama_mahasiswa != "":
            nama_baru = input("Masukkan Nama Mahasiswa Baru: ")
            konfirmasi = input(f"Apakah Anda yakin ingin mengedit nama {nama_mahasiswa} menjadi {nama_baru}? (y/n): ")

            if konfirmasi.lower() == "y":
                for mahasiswa in self.mahasiswa:
                    if mahasiswa["npm"] == npm:
                        mahasiswa["nama"] = nama_baru
                        print("Data mahasiswa berhasil diubah.")
                        break
            else:
                print("Proses edit dibatalkan.")
        else:
            print(f"Mahasiswa dengan NPM {npm} tidak ditemukan.")

    def hapus_mahasiswa(self):
        print("\nSUB MENU: Hapus Mahasiswa")
        print("====================================")
        npm = input("Masukkan NPM Mahasiswa: ")
        nama_mahasiswa = self.get_mahasiswa_nama(npm)

        if nama_mahasiswa != "":
            konfirmasi = input(f"Apakah Anda yakin ingin menghapus data mahasiswa dengan NPM {npm} dan Nama {nama_mahasiswa}? (y/n): ")

            if konfirmasi.lower() == "y":
                self.mahasiswa = [mahasiswa for mahasiswa in self.mahasiswa if mahasiswa["npm"] != npm]
                print("Data mahasiswa berhasil dihapus.")
            else:
                print("Proses hapus dibatalkan.")
        else:
            print(f"Mahasiswa dengan NPM {npm} tidak ditemukan.")

    def tampil_katalog_buku(self):
        print("\nSUB MENU: Tampil Katalog Buku")
        print("====================================")
        print("No\tJudul\tTahun Terbit\tPenerbit\tJumlah")
        print("------------------------------------")
        for i, buku in enumerate(self.katalog_buku, start=1):
            print(f"{i}\t{buku['judul']}\t{buku['tahun_terbit']}\t\t{buku['penerbit']}\t\t{buku['jumlah']}")
        print("------------------------------------")

    def tambah_buku(self):
        print("\nSUB MENU: Tambah Buku")
        print("====================================")
        judul = input("Masukkan Judul Buku: ")
        tahun_terbit = input("Masukkan Tahun Terbit: ")
        penerbit = input("Masukkan Penerbit: ")
        jumlah = input("Masukkan Jumlah Buku: ")

        self.katalog_buku.append({
            "judul": judul,
            "tahun_terbit": tahun_terbit,
            "penerbit": penerbit,
            "jumlah": jumlah
        })
        print("Data buku berhasil ditambahkan.")

    def edit_buku(self):
        print("\nSUB MENU: Edit Buku")
        print("====================================")
        judul = input("Masukkan Judul Buku: ")
        buku_ditemukan = False

        for buku in self.katalog_buku:
            if buku["judul"] == judul:
                buku_ditemukan = True
                print("Data Buku:")
                print(f"Judul: {buku['judul']}")
                print(f"Tahun Terbit: {buku['tahun_terbit']}")
                print(f"Penerbit: {buku['penerbit']}")
                print(f"Jumlah: {buku['jumlah']}")
                print("------------------------------------")

                judul_baru = input("Masukkan Judul Buku Baru: ")
                tahun_terbit_baru = input("Masukkan Tahun Terbit Baru: ")
                penerbit_baru = input("Masukkan Penerbit Baru: ")
                jumlah_baru = input("Masukkan Jumlah Buku Baru: ")

                buku["judul"] = judul_baru
                buku["tahun_terbit"] = tahun_terbit_baru
                buku["penerbit"] = penerbit_baru
                buku["jumlah"] = jumlah_baru

                print("Data buku berhasil diubah.")
                break

        if not buku_ditemukan:
            print(f"Buku dengan judul {judul} tidak ditemukan.")

    def hapus_buku(self):
        print("\nSUB MENU: Hapus Buku")
        print("====================================")
        judul = input("Masukkan Judul Buku: ")
        buku_ditemukan = False

        for buku in self.katalog_buku:
            if buku["judul"] == judul:
                buku_ditemukan = True
                konfirmasi = input(f"Apakah Anda yakin ingin menghapus data buku dengan judul {judul}? (y/n): ")

                if konfirmasi.lower() == "y":
                    self.katalog_buku.remove(buku)
                    print("Data buku berhasil dihapus.")
                else:
                    print("Proses hapus dibatalkan.")
                break

        if not buku_ditemukan:
            print(f"Buku dengan judul {judul} tidak ditemukan.")

    def pinjam_buku(self):
        print("\nSUB MENU: Pinjam Buku")
        print("====================================")
        npm = input("Masukkan NPM Mahasiswa: ")
        nama_mahasiswa = self.get_mahasiswa_nama(npm)

        if nama_mahasiswa != "":
            if not self.is_mahasiswa_have_book(npm):
                self.tampil_katalog_buku()
                no_buku = int(input("Masukkan nomor buku yang ingin dipinjam: ")) - 1

                if 0 <= no_buku < len(self.katalog_buku):
                    if int(self.katalog_buku[no_buku]["jumlah"]) > 0:
                        tanggal_pinjam = datetime.now().strftime("%Y-%m-%d")
                        tanggal_kembali = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

                        self.transaksi.append({
                            "npm": npm,
                            "judul": self.katalog_buku[no_buku]["judul"],
                            "tanggal_pinjam": tanggal_pinjam,
                            "tanggal_kembali": tanggal_kembali,
                            "status": "pinjam"
                        })

                        self.katalog_buku[no_buku]["jumlah"] = int(self.katalog_buku[no_buku]["jumlah"])
                        self.katalog_buku[no_buku]["jumlah"] -= 1

                        print("Buku berhasil dipinjam.")
                    else:
                        print("Maaf, stok buku tidak tersedia.")
                else:
                    print("Nomor buku tidak valid.")
            else:
                print("Mahasiswa sudah memiliki buku yang dipinjam.")
        else:
            print(f"Mahasiswa dengan NPM {npm} tidak ditemukan.")

    def kembalikan_buku(self):
        print("\nSUB MENU: Kembalikan Buku")
        print("====================================")
        npm = input("Masukkan NPM Mahasiswa: ")
        nama_mahasiswa = self.get_mahasiswa_nama(npm)

        if nama_mahasiswa != "":
            if self.is_mahasiswa_have_book(npm):
                print("Buku yang dipinjam oleh mahasiswa:")
                print("No\tJudul\tTanggal Pinjam\tTanggal Kembali")
                print("------------------------------------")

                for i, transaksi in enumerate(self.transaksi, start=1):
                    if transaksi["npm"] == npm and transaksi["status"] == "pinjam":
                        print(f"{i}\t{transaksi['judul']}\t{transaksi['tanggal_pinjam']}\t{transaksi['tanggal_kembali']}")
                print("------------------------------------")

                no_transaksi = int(input("Masukkan nomor transaksi buku yang ingin dikembalikan: ")) - 1

                if 0 <= no_transaksi < len(self.transaksi):
                    if self.transaksi[no_transaksi]["npm"] == npm and self.transaksi[no_transaksi]["status"] == "pinjam":
                        judul_buku = self.transaksi[no_transaksi]["judul"]

                        for buku in self.katalog_buku:
                            if buku["judul"] == judul_buku:
                                buku["jumlah"] += 1
                                break

                        self.transaksi[no_transaksi]["status"] = "kembali"
                        print("Buku berhasil dikembalikan.")
                    else:
                        print("Nomor transaksi buku tidak valid.")
                else:
                    print("Nomor transaksi buku tidak valid.")
            else:
                print("Mahasiswa tidak memiliki buku yang dipinjam.")
        else:
            print(f"Mahasiswa dengan NPM {npm} tidak ditemukan.")

    def main_menu(self):
        while True:
            print("\nMAIN MENU")
            print("====================================")
            print("1. Mahasiswa")
            print("2. Katalog Buku")
            print("3. Peminjaman Buku")
            print("4. Pengembalian Buku")
            print("0. Keluar")
            print("------------------------------------")
            menu = input("Pilih menu (0-4): ")

            if menu == "1":
                self.sub_menu_mahasiswa()
            elif menu == "2":
                self.sub_menu_katalog_buku()
            elif menu == "3":
                self.sub_menu_peminjaman_buku()
            elif menu == "4":
                self.sub_menu_pengembalian_buku()
            elif menu == "0":
                break
            else:
                print("Menu tidak valid.")

    def sub_menu_mahasiswa(self):
        while True:
            print("\nSUB MENU: Mahasiswa")
            print("====================================")
            print("1. Tampil Mahasiswa")
            print("2. Tambah Mahasiswa")
            print("3. Edit Mahasiswa")
            print("4. Hapus Mahasiswa")
            print("0. Kembali")
            print("------------------------------------")
            menu = input("Pilih menu (0-4): ")

            if menu == "1":
                self.tampil_mahasiswa()
            elif menu == "2":
                self.tambah_mahasiswa()
            elif menu == "3":
                self.edit_mahasiswa()
            elif menu == "4":
                self.hapus_mahasiswa()
            elif menu == "0":
                break
            else:
                print("Menu tidak valid.")

    def sub_menu_katalog_buku(self):
        while True:
            print("\nSUB MENU: Katalog Buku")
            print("====================================")
            print("1. Tampil Katalog Buku")
            print("2. Tambah Buku")
            print("3. Edit Buku")
            print("4. Hapus Buku")
            print("0. Kembali")
            print("------------------------------------")
            menu = input("Pilih menu (0-4): ")

            if menu == "1":
                self.tampil_katalog_buku()
            elif menu == "2":
                self.tambah_buku()
            elif menu == "3":
                self.edit_buku()
            elif menu == "4":
                self.hapus_buku()
            elif menu == "0":
                break
            else:
                print("Menu tidak valid.")

    def sub_menu_peminjaman_buku(self):
        while True:
            print("\nSUB MENU: Peminjaman Buku")
            print("====================================")
            print("1. Pinjam Buku")
            print("0. Kembali")
            print("------------------------------------")
            menu = input("Pilih menu (0-1): ")

            if menu == "1":
                self.pinjam_buku()
            elif menu == "0":
                break
            else:
                print("Menu tidak valid.")

    def sub_menu_pengembalian_buku(self):
        while True:
            print("\nSUB MENU: Pengembalian Buku")
            print("====================================")
            print("1. Kembalikan Buku")
            print("0. Kembali")
            print("------------------------------------")
            menu = input("Pilih menu (0-1): ")

            if menu == "1":
                self.kembalikan_buku()
            elif menu == "0":
                break
            else:
                print("Menu tidak valid.")

perpustakaan = Perpustakaan()
perpustakaan.load_data()
perpustakaan.main_menu()
perpustakaan.save_data()
