listnama = []
listnotelp = []
i = True

while i:
    print ('-----------------------------')
    print ('Selamat datang!')
    print ()
    print ('-----' 'Menu' '-----')
    print ('1. Daftar Kontak')
    print ('2. Tambah Kontak')
    print ('3. Keluar')
    print ()
    ans = input('Masukkan kode input = ')

    if ans == '2':
        print ('-----------------------------')
        print ('Masukkan data kontak:')
        nama = (input('Nama = '))       
        notelp = (input('No. Telp = '))
        listnama.append(nama)
        listnotelp.append(notelp)
        print ()
        print ("Data telah tersimpan!")

    elif ans == '1':
        print ('-----------------------------')
        print ("Daftar kontak")
        print ()
        for x in range(len(listnama)):
            print ("Nama = ", listnama[x])
            print ("No.Telp = ", listnotelp[x])

    elif ans == '3':
        print ('-----------------------------')
        print ("Program selesai, sampai jumpa!")
        i = False 
    else: 
        print ('-----------------------------')
        print ("Menu tidak tersedia, silahkan measukkan kembali kode input.")