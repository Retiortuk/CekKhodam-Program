def khodam_program():

   data_khodam = ['Macan Hitam', 'Macan Putih', 'Macan Merah', 'Singa', 'Gajah', 'Ular Kobra', 'Kalajengking', 'Kak Gem', 'Burung Dara', 'Burung Elang']

   print("==== CEK KHODAM ====\n")

   while True:
      nama = input("Siapa Nama Anda: ")
      if nama.strip() and nama.isalpha():
         break
      else:
         print("Masukkan Nama Yang Benar")



khodam_program()
