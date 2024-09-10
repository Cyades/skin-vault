# skin-vault
**Nama:**   Malvin Scafi<br>
**NPM:**    2306152430<br>
**Kelas:**  PBP F<br>

Hasil proyek dapat dilihat pada [link berikut](http://malvin-scafi-skinvault.pbp.cs.ui.ac.id/).

## Tugas 2
### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat repositori lokal baru, lalu membuat repositori di GitHub dan dihubungkan menggunakan `git remote add origin https://github.com/Cyades/os242.git`.
2. Menambahkan .gitignore untuk mengabaikan file yang tidak diperlukan, dan README.md untuk menjawab pertanyaan tugas proyek.
3. Membuat proyek Django dengan `django-admin startproject skin-vault` . dan mencatat dependensi di `requirements.txt`.
4. Membuat aplikasi bernama `main` dengan perintah `python manage.py startapp main`.
5. Memodifikasi `models.py` di aplikasi `main` untuk membuat model baru yang mendefinisikan struktur data yang akan disimpan di database yaitu:
```Python
class Product(models.Model):
    name = CharField,
    weapon = CharField,
    exterior = CharField,
    category = CharField,
    quality = CharField,
    price = IntegerField,
    description = TextField,
    quantity = IntegerField,

    @property
    def is_product_available(self):
        return self.quantity > 0
```
6. Menyimpan model tersebut dan menjalankan perintah `python manage.py makemigrations` serta `python manage.py migrate` untuk menerapkan model yang baru saya buat.
7. Membuat file baru bernama `main.html` di dalam direktori `main/templates`, kemudian menambahkan view baru yang disebut `show_main()` untuk menampilkan template tersebut dengan menyertakan context berupa identitas diri saya sendiri.
8. Selanjutnya, saya mengatur routing dengan membuat file `urls.py` di folder `main`, lalu membuat suatu pola URL yang akan memanggil fungsi yang telah dibuat di `views.py`. Agar aplikasi `main` terhubung dengan proyek utama, saya juga mengatur file `urls.py` di direktori proyek utama dan menambahkan pola URL yang mengarahkan ke pola URL yang sudah dibuat sebelumnya.
9. Melakukan deployment ke GitHub dan Pacil Web Service.

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Flowchart](flowchart.jpg)

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah sistem kontrol versi yang digunakan dalam pengembangan perangkat lunak untuk:
1. Pelacakan perubahan: Mencatat setiap perubahan pada kode sumber.
2. Kolaborasi: Memungkinkan banyak pengembang bekerja secara bersamaan tanpa mengganggu satu sama lain.
3. Branching: Mengembangkan fitur baru atau memperbaiki bug di cabang terpisah dari kode utama.
4. Reversi perubahan: Mengembalikan perubahan yang salah dengan mudah.
5. Manajemen rilis: Mengelola versi perangkat lunak untuk rilis stabil dan beta.
Dengan Git, pengembangan perangkat lunak menjadi lebih efisien dan terstruktur.

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django dijadikan pilihan untuk pembelajaran pengembangan perangkat lunak karena mudah dipelajari, memiliki dokumentasi yang baik, dan pendekatan "batteries included" yang menyediakan banyak fitur bawaan seperti autentikasi dan manajemen basis data. Dengan arsitektur Model-View-Template (MVT) dan ORM yang sederhana, Django memudahkan pemahaman konsep pengembangan web serta hubungan antara model dan basis data. Framework ini juga sangat aman, skalabel, didukung oleh komunitas besar, dan digunakan dalam proyek nyata, sehingga cocok bagi pemula (seperti saya) yang ingin mempelajari dasar-dasar hingga pengembangan aplikasi skala besar.

### 5. Mengapa model pada Django disebut sebagai ORM?
Dalam Django, model disebut sebagai ORM (Object-Relational Mapping) karena mereka menyediakan cara untuk berinteraksi dengan basis data menggunakan objek Python, bukan menggunakan query SQL langsung. ORM adalah sebuah teknik pemrograman yang memungkinkan pengembang untuk bekerja dengan basis data dengan menggunakan objek dan metode yang sesuai dengan struktur basis data, alih-alih menulis query SQL secara manual.