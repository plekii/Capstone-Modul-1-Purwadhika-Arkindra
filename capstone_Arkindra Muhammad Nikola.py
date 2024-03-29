#DATA PERUSAHAAN KARYAWAN
from tabulate import tabulate
import regex as re

karyawan = [
    {'kode' : 'FEIA0001','nama panjang': 'Fernanda Aulia','divisi' : 'OPERATION', 'domisili': 'Bekasi', 'email':'aulia.fanda@yahoo.com'},
    {'kode' : 'MONG0002','nama panjang': 'Mohammad Gilang','divisi' : 'FRONT END', 'domisili': 'Bogor', 'email':'gilang@gmail.com'},
    {'kode' : 'SAKA0003','nama panjang': 'Sarah Azka','divisi' : 'PROCUREMENT', 'domisili': 'Jakarta', 'email':'sarah.azka@gmail.com'}
    ]    
id = len(karyawan)
bin = []

def unik(tabel, isi):
    hasil_unik = []
    for i in range(len(tabel)):
        if tabel[i][isi] not in hasil_unik:
            hasil_unik.append(tabel[i][isi])
    return hasil_unik

def saring():
    data_sementara = []
    while True:
        try:
            tanya = input('filter apa yang ingin anda jalankan? (kode/nama panjang/divisi/domisili/email):\n')
            if tanya.replace(" ","").isalpha():
                if tanya == 'kode' or tanya == 'nama panjang' or tanya == 'divisi' or tanya == 'domisili' or tanya == 'email':
                    print (f'\npada key {tanya} terdapat pilihan:\n {unik(karyawan, tanya)}')
                    tanya2 = input(f'{tanya} apa yang ingin anda cari?\n').lower().replace(" ","")
                    for i in range(len(karyawan)):
                        if karyawan[i][tanya].lower().replace(" ","") == tanya2:
                            data_sementara.append(karyawan[i])
                    if len(data_sementara)!= 0:
                        print('\n',tabulate(data_sementara, headers = 'keys', tablefmt='pretty'))
                    else:
                        print('\nData tidak tersedia')
                    break
                else:
                    print('\nfilter yang anda masukkan tidak tersedia')  
                    break              
            else:
                print('\nmasukkan hanya alfabet\n')
                break
        except:
            print ('\ninput tidak valid\n')
            break
        
def cekAlpha3(kata):
    while True:
        hasil = input(f'Masukkan {kata} karyawan: ').capitalize()
        try :
            if hasil.replace(" ","").isalpha():
                return hasil
            else:
                 print('\nmasukkan hanya alphabet (tanpa angka maupun simbol)')
        except:
            print('\ninput tidak valid\n')


def cekAlpha2(kata):
    while True:
        if kata.replace(" ","").isalpha():
            break
        else:
            print('\nmasukkan hanya alphabet (tanpa angka maupun simbol)')
            break         

def kapital(kata):
    kata = kata.split()
    for i in range(len(kata)):
        kata[i] = kata[i].capitalize()
    return ' '.join(kata)

def email():
    while True:
        email = input('masukkan email karyawan: ')
        if re.fullmatch(r"\b\w+(?:\.?\w+)*\@\w+(?:\.?\w+)*\b",email):
            return email
        else:
            print('\nanda salah input')

def listKaryawan():
    ulang = True
    while ulang:
        sortir =  input('apakah anda ingin melakukan sort? (ya/tidak)\nnotes= default sortir menggunakan angka pada kode: ').lower().replace(" ","")
        try :
            if sortir.isalpha():
                if sortir == 'ya':
                    inputan = input('nama panjang/divisi/domisili (pilih satu):').lower()
                    if inputan.replace(" ","").isalpha():
                        for i in karyawan[0].keys():
                            if i == inputan:
                                karyawan2 = sorted(karyawan, key=lambda x: x[inputan])
                                print (f'\nSORTED BY: {inputan.capitalize()} ')
                                print (tabulate(karyawan2, headers = 'keys', tablefmt='pretty'))
                                ulang = False
                                break
                    else:
                        print('\nmasukkan hanya nama panjang/divisi/domisili')
                        
                elif sortir == 'tidak':
                    print('\n',tabulate(sorted(karyawan, key=lambda x: x['kode'][-4:]), headers = 'keys', tablefmt='pretty'))
                    ulang = False
                else:
                    print('\nmasukkan hanya ya/tidak')
            else:
                    print('\nmasukkan hanya ya/tidak')
        except:
            print('\ninput tidak valid')
            ulang = False

def tambahKaryawan():
    print('\n',tabulate(sorted(karyawan, key=lambda x: x['kode'][-4:]), headers = 'keys', tablefmt='pretty'))
    nama = kapital(cekAlpha3('nama'))
    
    global id
    id += 1
    kode_baru = nama[0] + nama[1] + nama[-2] + nama[-1] + str(id).zfill(4)
    divisi_baru = cekAlpha3('divisi').upper()
    domisili_baru = cekAlpha3('domisili')
    dom = kapital(domisili_baru)
    
    email_baru = email()
            
    tambah_karyawan = {'kode':kode_baru.upper(),
        'nama panjang':nama,
        'divisi':divisi_baru,
        'domisili':dom,
        'email':email_baru}
    karyawan.append(tambah_karyawan)
    print(f'\nKaryawan {nama} berhasil dimasukkan')
    print(tabulate(sorted(karyawan, key=lambda x: x['kode'][-4:]), headers = 'keys', tablefmt='pretty'))
    
def hapusKaryawan():
    isContinue = True
    while isContinue:
        try:   
            print('\n',tabulate(sorted(karyawan, key=lambda x: x['kode'][-4:]), headers = 'keys', tablefmt='pretty'))
            isSuccess = False
            hapus_karyawan = input('Masukkan kode karyawan yang ingin dihapus: ').upper().replace(" ","")
            for i in range(len(karyawan)):
                if karyawan[i]['kode'] == hapus_karyawan:
                    bin.append(karyawan[i])
                    print (f'\nkode {hapus_karyawan} berhasil dihapus')
                    del karyawan[i]
                    print(tabulate(sorted(karyawan, key=lambda x: x['kode'][-4:]), headers = 'keys', tablefmt='pretty'))
                    isSuccess = True
                    break
            if not isSuccess:     
                print('\nkode yang anda masukkan tidak valid!')
            while True:
                ask = input('apakah anda ingin mencoba lagi(ya/tidak): ').lower().replace(" ","")
                if ask == 'ya':
                    break
                elif ask == 'tidak':
                    isContinue = False
                    break
                else:
                    print('\nmasukkan hanya ya/tidak')
                    
        except :
            print('\ninput tidak valid')
                
def updateKaryawan():
    isContinue = True
    while isContinue:
        try:   
            print('\n',tabulate(sorted(karyawan, key=lambda x: x['kode'][-4:]), headers = 'keys', tablefmt='pretty'))
            isSuccess = False
            kode = input('Masukkan kode karyawan yang ingin diedit: ').upper().replace(" ","")
            i = 0
            for i in range(len(karyawan)):
                if karyawan[i]['kode'] == kode:
                    isSuccess = True
                    break
                else:
                    i+=1
            if not isSuccess:     
                print('\nkode yang anda masukkan tidak valid!')
            while isSuccess:
                field = input('Masukkan yang ingin diganti (divisi/domisili/email): ').lower().replace(" ","")
                cekAlpha2(field)
                if field == 'divisi' or field == 'domisili':
                    print (f'\n{field} lama {kode} adalah {karyawan[i][field]}')
                    new_value = cekAlpha3(field)
                    if field == 'divisi':
                        cekAlpha2(new_value)
                        new_value = new_value.upper()
                    elif field == 'domisili':
                        cekAlpha2(new_value)
                        new_value = kapital(new_value)
                elif field == 'email':
                    new_value = email()
                else:
                    print('\nmasukkan hanya divisi/domisili/email')
                    continue  
                print (f'\n{field} kode {kode} berhasil terupdate')     
                karyawan[i][field] = new_value 
                print(tabulate(sorted(karyawan, key=lambda x: x['kode'][-4:]), headers = 'keys', tablefmt='pretty'))
                isSuccess = False
                isContinue = False
                
        except :
            print ('\ninput tidak valid')
            
def restore():
    if len(bin) !=0:
        table = tabulate(sorted(bin, key=lambda x: x['kode'][-4:]), headers = 'keys', tablefmt='pretty')
        print (f'\nbin:\n{table}') 
        while True:
            inputan = input('anda ingin restore data?(ya/tidak): ').lower().replace(" ","")
            try:
                if inputan == 'ya':
                    isSuccess = True
                    while isSuccess:
                        print (f'\npilihan kode:\n {unik(bin, "kode")}')
                        balik = input('masukkan kode yang ingin anda restore: ').upper().replace(" ","")
                        for i in range(len(bin)):
                            if bin[i]['kode'] != balik:
                                if i == len(bin)-1:
                                    print(f'\n{balik} tidak ditemukan')
                            elif bin[i]['kode'] == balik:
                                print(f'{balik} berhasil direstore')
                                karyawan.append(bin[i])
                                del bin[i]
                                isSuccess = False
                                break
                    print('\n',tabulate(sorted(karyawan, key=lambda x: x['kode'][-4:]), headers = 'keys', tablefmt='pretty'))
                    break
                elif inputan == 'tidak':
                    break
                else:
                    print('\nmasukkan hanya ya/tidak')
            except:
                print('\ninput anda tidak valid')
                break
    else:
        print('\nTidak ada data yang dapat direstore (bin kosong)')
                     

def exit():
    print('\nsampai jumpa')        
def selain():           
    print('\nmasukkan integer range 1-7 saja!')     

while True:
    print('''\nSelamat datang di website perusahaan XYZ:
        1. Menampilkan List Karyawan
        2. Masukkan Data karyawan baru
        3. Menghapus Data Karyawan
        4. Update Data
        5. Mencari Data
        6. Restore Data
        7. Exit Program''')
    try:
        menu = int(input('masukkan angka menu yang ingin dijalankan: '))
        if menu == 1:
            listKaryawan()
        elif menu == 2:
            tambahKaryawan()
        elif menu == 3:
            hapusKaryawan()
        elif menu == 4:
            updateKaryawan ()
        elif menu == 5:
            saring()
        elif menu == 6:
            restore()
        elif menu == 7:
            exit()
            break
        elif menu < 1 or menu > 7:
            selain()
    except:
            print ('\ninput tidak valid')
