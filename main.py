import random
import re

def khodam_program():
   # DATABASE
   data_khodam = ['Gak Ada', 'Macan Hitam', 'Macan Putih', 'Macan Merah', 'Singa', 'Gajah', 'Ular Kobra', 'Kalajengking', 'Kak Gem', 'Burung Dara', 'Burung Elang']
   kepribadian_khodam = {
      'Macan Hitam': 'Seseorang Yang Tunggu Kiris Besar Nan Perkasa',
      'Macan Putih': 'Seseorang Yang Putih Bersih Dan Baik Hati Rajin Menabung Dan Baik Dengan Istri',
      'Macan Merah': 'Seseorang Yang Galak Dikit-Dikit Marah Emosian Tapi Banyak Duit',
      'Singa': 'Seseorang Yang Matang Dan Mudah Menyerah',
      'Gajah': 'Seseorang Yang membawa energi kuat yang dapat digunakan untuk memberikan kekuatan dan ketahanan gaib kepada individu yang memohon bantuan mereka.',
      'Ular Kobra': 'Seseorang Yang dengan warna yang khas, tubuh yang panjang dan lentur, serta mata yang bijaksana.',
      'Kalajengking': 'Seseorang Yang Tampan Tapi Ngantukan Sangar dan Banyak Disukai Oleh Orang',
      'Kak Gem': 'Seseorang Yang Baik Hati Suka Memberi Semnagat Untuk Orang Lain, PAHAM!!',
      'Burung Dara': 'Seseorang Yang Setia Pada Pasangan Nya atau Pada apapun itu di manapun kapanpun itu',
      'Burung Elang': 'Kamu Memiliki Sifat Yang 11 12 Sama Orang Amerika Suka Menembak Serakah Sombong Dan Rasis ',
   }


   # HOME (MAIN)
   print("\n==== CEK KHODAM ====\n")

   while True:
      nama = input("Siapa Nama Anda: ")
      if re.match(r'^[a-zA-Z\s-]+$', nama.strip()):
         break
      else:
         print("Masukan Nama Yang Benar")

   while True:
      umur = input("Berapa Umur Kamu: ")
      if umur.strip() and umur.isdigit():
         umur = int(umur)
         break
      else:
         print("Itumah Bukan Umur! Masukan Umur Yang Valid!")

   # OUTPUT
   hasil_khodam = random.choice(data_khodam)
   print(f"\nHalo {nama}, Khodam Kamu {hasil_khodam}")
   if hasil_khodam in kepribadian_khodam:
      print(f"Kepribadian {hasil_khodam} Artinya {kepribadian_khodam[hasil_khodam]}")
   elif hasil_khodam not in kepribadian_khodam:
      print(f"Kepribadian {hasil_khodam} Artinya Kamu Gak Punya Khodam")

# LOOPING
cek_lagi = True
while cek_lagi:
   khodam_program()
   while True:
      cek = input("Mau Ngecheck Lagi Gak? (y/t): ")
      if cek == 'y':
         break
      elif cek == 't':
         cek_lagi = False
         break
      else:
         ("Masukkan Pilihan Yang Valid Y/T")
