import random

def khodam_program():

   data_khodam = ['Macan Hitam', 'Macan Putih', 'Macan Merah', 'Singa', 'Gajah', 'Ular Kobra', 'Kalajengking', 'Kak Gem', 'Burung Dara', 'Burung Elang']

   print("==== CEK KHODAM ====\n")

   while True:
      nama = input("Siapa Nama Anda: ")
      if nama.strip() and nama.isalpha():
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

   hasil_khodam = random.choice(data_khodam)
   print(f"Halo {nama}, Khodam Kamu {hasil_khodam}")


khodam_program()
