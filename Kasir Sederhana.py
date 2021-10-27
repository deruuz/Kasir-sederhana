# Data awal
print("SELAMAT DATANG DI WARUNG BU SUK")
print("SILAHKAN PILIH MENUNYA : ")
print("1. MIE AYAM = Rp. 10.000 \n2. ES TEH = Rp. 7.000 \n3. NASI GORENG = Rp. 12.000")
print("BELI LEBIH DARI 2 MENU MENDAPATKAN DISKON SEBESAR 10% (semua menu yang tersedia)\n"
      "TIDAK BOLEH NGUTANG !!!")
menu = input("PILIH MENU : ")

# Program kasir
# Menu awal adalah mie ayam dengan harga 10.000 dan jika membeli lebih dari 1 akan mendapat diskon sebesar 10%
# dan dilanjut ke menu - menu yang ada
while True :
    if menu == "1":
        jumlah = int(input("JUMLAH BELI : "))
        uang = int(input("MASUKAN UANG ANDA : "))
        harga_mieayam = 10000
        diskon = 10/100
        harga_mieayamku = jumlah * harga_mieayam
        Kembalian = uang - harga_mieayamku
        harga_diskon = harga_mieayamku * diskon
        print("ANDA MEMBELI MIE AYAM DENGAN JUMLAH",
              jumlah, "DENGAN HARGA ", harga_mieayamku)

        if uang > harga_mieayamku:
            if jumlah == 1 :
                print("JADI KEMBALIANNYA ADALAH", Kembalian)
                print("TERIMA KASIH TELAH MEMBELI DI WARUNG BU SUK")
            else : 
                print("ANDA MENDAPAT DISKON SEBESAR", harga_diskon)
                print("JADI KEMBALIANNYA ADALAH", harga_diskon + Kembalian)
                print("TERIMA KASIH TELAH MEMBELI DI WARUNG BU SUK")
        elif uang == harga_mieayamku:
            if jumlah == 1 :
                print("ANDA TIDAK MENDAPAT KEMBALIAN")
                print("TERIMA KASIH TELAH MEMBELI DI WARUNG BU SUK")
            else :
                print("ANDA MENDAPAT DISKON SEBESAR", harga_diskon)
                print("JADI KEMBALIANNYA ADALAH", harga_diskon + Kembalian)
                print("TERIMA KASIH TELAH MEMBELI DI WARUNG BU SUK")
        else:
            print("UANG YANG ANDA MILIKI TIDAK CUKUP !!!")
        break

    elif menu == "2":
        jumlah = int(input("JUMLAH BELI : "))
        uang = int(input("MASUKAN UANG ANDA "))
        harga_esteh = 7000
        diskon = 10/100
        harga_estehku = jumlah * harga_esteh
        Kembalian = uang - harga_estehku
        harga_diskon = harga_estehku * diskon
        print("ANDA AKAN MEMBELI ES TEH DENGAN JUMLAH",
              jumlah, "DENGAN HARGA", harga_estehku)

        if uang > harga_estehku:
            if jumlah == 1 :
                print("JADI KEMBALIANNYA ADALAH", Kembalian)
                print("TERIMA KASIH TELAH MEMBELI DI WARUNG BU SUK")
            else :
                print("ANDA MENDAPAT DISKON SEBESAR", harga_diskon)
                print("JADI KEMBALIANNYA ADALAH", harga_diskon + Kembalian)
                print("TERIMA KASIH TELAH MEMBELI DI WARUNG BU SUK")
        elif uang == harga_estehku:
            if jumlah == 1 :
                print("ANDA TIDAK MENDAPAT KEMBALIAN")
                print("TERIMA KASIH TELAH MEMBELI DI WARUNG BU SUK")
            else :
                print("ANDA MENDAPAT DISKON SEBESAR", harga_diskon)
                print("JADI KEMBALIANNYA ADALAH", harga_diskon + Kembalian)
                print("TERIMA KASIH TELAH MEMBELI DI WARUNG BU SUK")
        else:
            print("UANG YANG ANDA MILIKI TIDAK CUKUP !!!")
        break

    elif menu == "3":
        jumlah = int(input("JUMLAH BELI : "))
        uang = int(input("MASUKAN UANG ANDA : "))
        harga_nasigoreng = 12000
        diskon = 10/100
        harga_nasigorengku = jumlah * harga_nasigoreng
        Kembalian = uang - harga_nasigorengku
        harga_diskon = harga_nasigorengku * diskon
        print("ANDA MEMBELI NASI GORENG DENGAN JUMLAH",
              jumlah, "DENGAN HARGA", harga_nasigorengku)

        if uang > harga_nasigorengku:
            if jumlah == 1 :
                print("JADI KEMBALIANNYA ADALAH", Kembalian)
                print("TERIMA KASIH TELAH MEMEBELI DIWARUNG BU SUK")
            else :
                print("ANDA MENDAPAT DISKON SEBESAR", harga_diskon)
                print("JADI KEMBALIANNYA ADALAH", harga_diskon + Kembalian)
                print("TERIMA KASIH TELAH MEMEBELI DIWARUNG BU SUK")
        elif uang == harga_nasigorengku:
            if jumlah == 1 :
                print("ANDA TIDAK MENDAPATK KEMBALIAN")
                print("TERIMA KASIH TELAH MEMEBELI DIWARUNG BU SUK")
            else :
                print("ANDA MENDAPAT DISKON SEBESAR", harga_diskon)
                print("JADI KEMBALIANNYA ADALAH", harga_diskon + Kembalian)
                print("TERIMA KASIH TELAH MEMEBELI DIWARUNG BU SUK")
        else:
            print("UANG YANG ANDA MILIKI BELUM CUKUP !!!")
        break

    else:
        print("MENU YANG ANDA MASUKAN BELUM ADA")
        print("COBALAH MEMASUKAN MENU YANG ADA")
        menu = input("PILIH MENU : ")
