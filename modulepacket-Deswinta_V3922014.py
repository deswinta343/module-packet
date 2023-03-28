#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Selamat datang di kalkulator luas/volume!")
print("Pilih opsi yang Anda inginkan:")
print("1. Menghitung luas 2 dimensi")
print("2. Menghitung volume 3 dimensi")
#memberikan keterangan semacam judul

pilihan = input("Masukkan pilihan Anda (1 atau 2): ")
#memasukkan inputnya dan akan menyimpan input tersebut dalam variabel bernama pilihan

if pilihan == "1":
#menggunakan percabangan jika memilih
    print("Pilih bentuk 2 dimensi yang ingin dihitung:")
    print("1. Persegi")
    print("2. Persegi panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Jajar genjang")
    print("6. Trapesium")
    #opsi pilihan 1-6
    
    bentuk = input("Masukkan pilihan Anda (1-6): ")
    #variabel bentuk untuk menginput ukuran dan rumus bangun ruang

    if bentuk == "1":
        #percabangan if atau perumpamaan dengan angka 1
        sisi = float(input("Masukkan panjang sisi: "))
        luas = sisi * sisi
        print("Luas persegi adalah:", luas)
        #bentuk 1 untuk menghitung luas persegi
    elif bentuk == "2":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        luas = panjang * lebar
        print("Luas persegi panjang adalah:", luas)
        #bentuk 2 untuk menghitung luas persegi panjang
    elif bentuk == "3":
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = 0.5 * alas * tinggi
        print("Luas segitiga adalah:", luas)
        #bentuk 3 untuk menghitung luas segitiga
    elif bentuk == "4":
        jari_jari = float(input("Masukkan jari-jari: "))
        luas = 3.14 * jari_jari**2
        print("Luas lingkaran adalah: ", luas)
        #bentuk 4 untuk mengukur luas lingkaran
    elif bentuk == "5":
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = alas * tinggi
        print("Luas jajar genjang adalah: ", luas)
        #bentuk 5 untuk menghitung luas jajar genjang
    elif bentuk == "6":
        sisi_a = float(input("Masukkan sisi A: "))
        sisi_b = float(input("Masukkan sisi B: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = 0.5 * (sisi_a + sisi_b) * tinggi
        print("Luas trapesium adalah: ", luas)
        #bentuk 6 untuk menghitung luas trapesium
    else:
        print("Maaf, bentuk tidak dikenal.")
        #jika memasukkan bangun diluar ke 6 bangun maka else akan muncul
        
elif pilihan == "2":
    #percabangan else pilihan dengan angka 2
    print("Pilih bentuk 3 dimensi yang ingin dihitung:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("5. Limas")
    print("6. Prisma")
    #user dapat memilih angka sesuai dengan bangun yang ingin diketahui ukurannya

    bentuk = input("Masukkan pilihan Anda (1-6): ")
    #variabel bentuk untuk menginput ukuran dan rumus bangun ruang
    
    if bentuk == "1":
    #menggunakan percabangan if dengan variabel bentuk dengan angka 1
        sisi = float(input("Masukkan panjang sisi: "))
        #membuat variabel dengan nama sisi dengan type data float
        volume = sisi**3
        #rumus volume
        print("Volume kubus adalah: ", volume)
        #dengan memasukkan angka user dapat mengetahui volume kubus
    elif bentuk == "2":
        panjang = float(input("Masukkan panjang balok: "))
        #membuat variabel dengan nama panjang deengan type data float
        lebar = float(input("Masukkan lebar balok: "))
        #type data float
        tinggi = float(input("Masukkan tinggi balok: "))
        #type data float
        volume = panjang * lebar * tinggi
        #rumus balok
        print("Volume balok dengan panjang", panjang, ", lebar", lebar, ", dan tinggi", tinggi, "adalah", volume)
        #hasil dengan memanggil variabel yang telah dimasukkan inputannya dan telah diproses sesuai dengan rumus
        #maka user dapat mengetahui volume balok
    elif bentuk == "3":
        jari_jari = float(input("Masukkan jari-jari tabung: "))
        tinggi = float(input("Masukkan tinggi tabung: "))
        volume = math.pi * jari_jari ** 2 * tinggi
        print("Volume tabung dengan jari-jari", jari_jari, "dan tinggi", tinggi, "adalah", volume)
    elif bentuk == "4":
        jari_jari = float(input("Masukkan jari-jari kerucut: "))
        tinggi = float(input("Masukkan tinggi kerucut: "))
        volume = 1/3 * math.pi * jari_jari ** 2 * tinggi
        print("Volume kerucut dengan jari-jari", jari_jari, "dan tinggi", tinggi, "adalah", volume)
    elif bentuk == "5":
        alas = float(input("Masukkan luas alas limas: "))
        tinggi = float(input("Masukkan tinggi limas: "))
        volume = 1/3 * alas * tinggi
        print("Volume limas dengan luas alas", alas, "dan tinggi", tinggi, "adalah", volume)
    elif bentuk == "6":
        alas = float(input("Masukkan alas segitiga prisma: "))
        tinggi = float(input("Masukkan tinggi segitiga prisma: "))
        tinggi_prisma = float(input("Masukkan tinggi prisma: "))
        volume = 1/2 * alas * tinggi * tinggi_prisma
        print("Volume prisma segitiga dengan alas", alas, ", tinggi", tinggi, ", dan tinggi prisma", tinggi_prisma, "adalah", volume)
    else:
        print("Bentuk tidak dikenali.")

