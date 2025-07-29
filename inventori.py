import json

DATA_FILE = "data_barang.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def tambah_barang():
    nama = input("Nama barang: ")
    stok = int(input("Jumlah stok: "))
    harga = float(input("Harga per unit: "))
    data = load_data()
    data.append({"nama": nama, "stok": stok, "harga": harga})
    save_data(data)
    print("Barang berhasil ditambahkan.\n")

def tampilkan_barang():
    data = load_data()
    if not data:
        print("Data kosong.\n")
        return
    for i, barang in enumerate(data, 1):
        print(f"{i}. {barang['nama']} - Stok: {barang['stok']} - Harga: {barang['harga']}")
    print()

def edit_barang():
    data = load_data()
    tampilkan_barang()
    idx = int(input("Pilih nomor barang untuk diedit: ")) - 1
    if 0 <= idx < len(data):
        data[idx]['nama'] = input("Nama baru: ")
        data[idx]['stok'] = int(input("Stok baru: "))
        data[idx]['harga'] = float(input("Harga baru: "))
        save_data(data)
        print("Barang berhasil diedit.\n")
    else:
        print("Pilihan tidak valid.\n")

def hapus_barang():
    data = load_data()
    tampilkan_barang()
    idx = int(input("Pilih nomor barang untuk dihapus: ")) - 1
    if 0 <= idx < len(data):
        data.pop(idx)
        save_data(data)
        print("Barang berhasil dihapus.\n")
    else:
        print("Pilihan tidak valid.\n")

def export_csv():
    import csv
    data = load_data()
    with open("data_barang.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["nama", "stok", "harga"])
        writer.writeheader()
        writer.writerows(data)
    print("Data berhasil diekspor ke data_barang.csv\n")

def cari_barang():
    keyword = input("Masukkan nama barang: ").lower()
    data = load_data()
    hasil = [b for b in data if keyword in b['nama'].lower()]
    if hasil:
        for b in hasil:
            print(f"{b['nama']} - Stok: {b['stok']} - Harga: {b['harga']}")
    else:
        print("Barang tidak ditemukan.")
    print()

def laporan_ringkas():
    data = load_data()
    total_barang = sum([b['stok'] for b in data])
    total_nilai = sum([b['stok'] * b['harga'] for b in data])
    print(f"Total Barang: {total_barang}")
    print(f"Total Nilai Inventori: Rp{total_nilai:,.2f}\n")

def menu():
    while True:
        print("=== Menu Inventori ===")
        print("1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("3. Edit Barang")
        print("4. Hapus Barang")
        print("5. Cari Barang")
        print("6. Ekspor ke CSV")
        print("7. Laporan Ringkas")
        print("8. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            tampilkan_barang()
        elif pilihan == "3":
            edit_barang()
        elif pilihan == "4":
            hapus_barang()
        elif pilihan == "5":
            cari_barang()
        elif pilihan == "6":
            export_csv()
        elif pilihan == "7":
            laporan_ringkas()
        elif pilihan == "8":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.\n")

menu()
