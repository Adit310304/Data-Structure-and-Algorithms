1. DSA Arrays
   Array adalah struktur data yang digunakan untuk menyimpan beberapa elemen. Array digunakan oleh banyak algoritma. Sebagai contoh, sebuah algoritma dapat digunakan untuk mencari nilai terendah dalam suatu array.

   Algoritma : Mencari nilai terendah dalam array
   Cara Kerja:
   1. Telusuri Nilai dalam sebuah array satu per satu.
   2. Cek apakah nilai saat ini adalah yang terendah sejauh ini, jika iya, simpan.
   3. Setelah melihat semua nilai, nilai yang disimpan akan menjadi yang terendah dari semua nilai yang ada di array.
  
   Implementasi
   1. Buat variabel "minVal" dan atur agar sama dengan nilai pertama dari array.
   2. Telusuri setiap elemen di array.
   3. Jika elemen saat ini memiliki nilai yang lebih rendah dari "minVal", update "minVal" ke nilai ini.
   4. Setelah melihat semua elemen di array, variabel "minVal" sekarang berisi nilai terendah.

   Time Complexity : O(n)
   
