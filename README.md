# Skin Vault 
**Nama:**   Malvin Scafi<br>
**NPM:**    2306152430<br>
**Kelas:**  PBP F<br>

Hasil proyek dapat dilihat pada [link berikut](http://malvin-scafi-skinvault.pbp.cs.ui.ac.id/).

## Tugas 6

### 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

- Interaktivitas: JavaScript memungkinkan pengembang untuk membuat halaman web yang dinamis dan interaktif. Misalnya, efek hover, validasi form di sisi klien, pembaruan data tanpa memuat ulang halaman (melalui AJAX), dan animasi semuanya dapat dilakukan dengan JavaScript.
- Responsif di sisi klien (Client-Side Processing): Dengan JavaScript, pemrosesan data bisa dilakukan di browser pengguna tanpa harus selalu berkomunikasi dengan server. Ini mempercepat respons waktu aplikasi dan meningkatkan pengalaman pengguna.
- Kompatibilitas lintas platform: JavaScript dapat berjalan di hampir semua browser web modern, seperti Chrome, Firefox, Safari, dan Edge, tanpa memerlukan pengaturan atau instalasi tambahan. Ini membuat aplikasi web dapat diakses oleh pengguna dari berbagai perangkat dan platform.
- Ekosistem dan Komunitas yang Kuat: JavaScript memiliki ekosistem library dan framework yang sangat luas seperti React, Angular, dan Vue.js, yang mempercepat proses pengembangan dan memudahkan penerapan fitur canggih. Ditambah, komunitas pengembang JavaScript sangat aktif, sehingga banyak sumber daya dan dukungan yang tersedia.
- Manajemen Konten Asinkron: JavaScript mendukung pemrograman asinkron melalui AJAX dan Fetch API. Ini memungkinkan aplikasi untuk mengambil atau mengirim data ke server di latar belakang tanpa harus memuat ulang halaman, sehingga pengalaman pengguna lebih lancar, seperti yang terlihat pada single-page applications (SPA).
- Pengembangan Full-Stack: Dengan hadirnya Node.js, JavaScript dapat digunakan tidak hanya di sisi klien (front-end) tetapi juga di sisi server (back-end). Ini memungkinkan pengembang full-stack untuk menggunakan satu bahasa pemrograman di kedua sisi, yang menyederhanakan alur kerja dan meningkatkan produktivitas.
- Pengayaan UI/UX: JavaScript memungkinkan pengembang untuk membangun antarmuka pengguna (UI) yang menarik dan intuitif, seperti drag-and-drop, slideshow, popup, dan modal window, yang meningkatkan pengalaman pengguna (UX).
- Kompatibilitas dengan API: JavaScript mempermudah integrasi dengan berbagai API, baik internal maupun eksternal, sehingga aplikasi web dapat berinteraksi dengan layanan pihak ketiga, seperti pembayaran online, peta, atau integrasi media sosial.

JavaScript menjadi bahasa inti untuk pengembangan web modern karena fleksibilitas dan kapabilitasnya untuk membuat aplikasi yang cepat, dinamis, dan interaktif.


### 2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?

Fungsi `await` dalam penggunaan `fetch()` di JavaScript adalah untuk menunggu hingga promise yang dihasilkan oleh `fetch()` selesai sebelum melanjutkan ke baris kode berikutnya. `fetch()` adalah operasi asynchronous yang mengembalikan promise, dan `await` memungkinkan kita untuk menulis kode seolah-olah itu synchronous (berjalan secara berurutan), meskipun sebenarnya tetap asynchronous di balik layar.

**Fungsi `await` dalam `fetch()`**
- `fetch()` sendiri mengembalikan promise, yang merepresentasikan proses request yang belum selesai.
- Dengan `await`, kita memberitahu program untuk menunggu sampai promise selesai dan hasilnya (response) tersedia.
- Setelah request selesai, `await` akan memberikan hasil dari promise tersebut, yang biasanya berupa object response.
- Tanpa `await`, kode akan terus berjalan, bahkan sebelum request selesai, sehingga kita mungkin mencoba menggunakan response yang belum tersedia.
- Contoh penggunaan `await` dengan fetch():
```javascript
async function getData() {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  console.log(data);
}
```

**Apa yang terjadi jika tidak menggunakan `await`?**

Jika tidak menggunakan `await`, kode akan berlanjut tanpa menunggu promise selesai. Hasil dari `fetch()` akan tetap berupa promise, bukan nilai dari response-nya. Jadi, kita tidak bisa langsung menggunakan data yang dikembalikan oleh server.

- Contoh tanpa `await`:
```javascript
function getData() {
  const response = fetch('https://api.example.com/data');
  console.log(response);  // Ini hanya mencetak promise, bukan data dari response
}
```
Di sini, alih-alih menampilkan data yang kita harapkan, `console.log()` akan menampilkan objek promise, karena proses fetch belum selesai pada saat log dipanggil.

Kesimpulan:
- Dengan `await`: Program akan menunggu hingga request selesai dan bisa menggunakan hasilnya langsung.
- Tanpa `await`: Program akan terus berjalan tanpa menunggu, sehingga kita mungkin hanya mendapatkan promise, bukan hasil dari request-nya.

### 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

Kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX POST dalam kasus tertentu karena Django secara default memiliki perlindungan Cross-Site Request Forgery (CSRF) untuk semua request POST. CSRF merupakan serangan di mana penyerang bisa membuat pengguna yang sudah login di suatu website melakukan aksi tanpa sepengetahuannya melalui website lain.

Namun, ketika kita menggunakan AJAX request dari frontend (misalnya dengan JavaScript) dan ingin mengirimkan data melalui POST, CSRF token harus dikirimkan bersamaan dengan request. Jika tidak, Django akan menolak request tersebut karena tidak ada CSRF token yang valid.

Jika kita tidak ingin memvalidasi CSRF token untuk request tersebut, kita bisa menggunakan decorator `@csrf_exempt` untuk mengecualikan view tersebut dari perlindungan CSRF.

Namun, perlu berhati-hati dalam menggunakannya. Menggunakan `@csrf_exempt` bisa membuka celah keamanan jika request tersebut rentan terhadap serangan CSRF. Sebaiknya, hanya digunakan ketika kita yakin bahwa request tersebut tidak memerlukan perlindungan CSRF, misalnya dalam kasus API endpoint yang tidak memerlukan autentikasi pengguna atau sudah dilindungi dengan cara lain.

**Contoh:**
```python
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def my_ajax_view(request):
    if request.method == 'POST':
        # Handle the AJAX POST request
        data = {'message': 'Success'}
        return JsonResponse(data)
```
Namun, solusi yang lebih baik adalah memastikan bahwa CSRF token dikirimkan dalam setiap request POST, bahkan dalam AJAX request, sehingga kita tetap memanfaatkan lapisan keamanan yang disediakan Django.

### 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

- Keamanan: Melakukan pembersihan data di backend membantu melindungi sistem dari serangan yang berbahaya, seperti SQL injection atau XSS (Cross-Site Scripting). Jika pembersihan hanya dilakukan di frontend, penyerang yang terampil bisa saja memanipulasi data sebelum dikirim ke backend dengan melewati validasi frontend.
- Keandalan Data: Pengguna mungkin menonaktifkan atau memanipulasi JavaScript di browser mereka, sehingga pembersihan yang dilakukan di frontend tidak berjalan. Dengan pembersihan di backend, kamu memastikan bahwa setiap input yang diterima sudah dibersihkan dengan benar tanpa bergantung pada client-side validation.
- Konsistensi: Backend adalah titik sentral di mana semua data diproses dan disimpan, sehingga pembersihan di backend memastikan konsistensi data untuk semua input, baik yang berasal dari web, mobile apps, atau API lain.
- Kontrol Penuh: Backend memiliki akses penuh ke seluruh data dan logika pemrosesan, sehingga bisa memastikan validasi lebih kompleks dan memutuskan apakah input benar-benar sesuai dengan standar yang diharapkan sebelum data disimpan atau diproses lebih lanjut.

Melakukan pembersihan di kedua tempat, baik frontend maupun backend, memberikan perlindungan ganda untuk aplikasi.


### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

tar dl aj mending bobok dl




## Tugas 5
### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
CSS memiliki aturan prioritas (specificity) dalam menentukan style mana yang akan diterapkan pada elemen HTML jika ada beberapa CSS selector yang diterapkan. Berikut adalah urutan prioritasnya, dari yang tertinggi:
1. **Inline Style**: Style yang ditulis langsung di elemen HTML memiliki prioritas tertinggi. Contoh: `<p style="color: purple;">Skapi mw bobo</p>`.
2. **ID Selector**: Selector yang mengacu pada ID elemen HTML, menggunakan tanda `#`. Contoh: `#header { background-color: green; }`.
3. **Class Selector**: Selector yang mengacu pada kelas tertentu dalam HTML, ditandai dengan `.`. Contoh: `.box { color: blue; }`.
4. **Tag Selector**: Selector yang langsung mengacu pada tag HTML seperti h1, p, atau div. Contoh: `p { color: red; }`.
5. **Style Default Browser**: Style bawaan yang ditentukan oleh browser, misalnya ukuran teks default pada tag `<h1>` yang lebih besar dibandingkan teks dalam tag `<p>`.

Selain urutan di atas, ada juga penggunaan flag `!important` yang akan mengesampingkan semua prioritas lainnya. Jika ada lebih dari satu `!important` di elemen yang sama, prioritas ditentukan berdasarkan specificitiy selector.


### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Responsive design menjadi penting dalam pengembangan aplikasi web karena beberapa alasan utama:
1. **Beragam Perangkat dan Ukuran Layar**: Pengguna mengakses situs web dari berbagai perangkat seperti ponsel, tablet, laptop, dan desktop dengan ukuran layar yang berbeda. Responsive design memastikan tampilan dan fungsionalitas web tetap optimal di semua ukuran layar.
2. **Pengalaman Pengguna yang Lebih Baik**: Dengan tampilan yang menyesuaikan layar perangkat, pengguna akan mendapatkan pengalaman yang lebih nyaman. Navigasi yang mudah, konten yang terbaca dengan baik, dan elemen-elemen yang tetap fungsional membuat pengguna lebih betah.
3. **SEO (Search Engine Optimization)**: Google dan mesin pencari lainnya memprioritaskan situs yang responsif dalam hasil pencarian mobile. Hal ini meningkatkan visibilitas situs dan jumlah pengunjung.

4. **Efisiensi Pengembangan**: Dengan responsive design, pengembang hanya perlu membuat satu situs web yang dapat diakses di berbagai perangkat, sehingga mengurangi biaya dan waktu pengembangan dibandingkan membuat situs terpisah untuk mobile dan desktop.

#### Contoh Aplikasi yang Menerapkan Responsive Design:
1. **Airbnb**: Situs ini dapat menyesuaikan tampilannya di berbagai perangkat. Pada perangkat mobile, tata letak berubah menjadi lebih vertikal dan elemen-elemen besar untuk memudahkan interaksi, sementara di desktop, layout lebih lebar dan memanfaatkan ukuran layar penuh.
2. **Spotify Web Player**: Spotify menerapkan responsive design, di mana tampilan pemutar musiknya disesuaikan dengan ukuran layar pengguna, baik di desktop maupun mobile.

#### Contoh Aplikasi yang Belum Menerapkan Responsive Design:
1. **Website OS**: 

![SS Proof](assets/assignment/NoResponsiveWeb.png)

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

**1. Margin**
Margin adalah ruang di luar elemen, antara elemen tersebut dengan elemen lainnya. Ini mengontrol jarak antara elemen-elemen yang ada di halaman web.
- Penggunaan: Mengatur jarak antar elemen.
- Implementasi CSS:
```CSS
.contoh {
    margin-top: 10px;
    margin-right: 15px;
    margin-bottom: 20px;
    margin-left: 25px;
}
```
**2. Border**
Border adalah garis yang mengelilingi elemen dan terletak di antara padding dan margin. Border memberikan batas visual di sekitar elemen.
- Penggunaan: Menambah batas atau frame di sekitar elemen.
-  Implementasi CSS:
```CSS
.contoh {
    border-top: 2px solid red;
}
```
**3. Padding**
Padding adalah ruang di dalam elemen, antara konten elemen dengan border elemen. Padding mendorong konten menjauh dari tepi elemen.
- Penggunaan: Mengatur jarak antara konten dan border.
- Implementasi CSS:
```CSS
.contoh {
    padding-top: 5px;
    padding-right: 10px;
    padding-bottom: 15px;
    padding-left: 20px;
}
```
#### Contoh Implementasi Bersamaan:
```CSS
.contoh {
    margin: 20px;           /* Margin luar 20px di semua sisi */
    padding: 15px;          /* Padding dalam 15px di semua sisi */
    border: 2px solid blue; /* Border tebal 2px, solid, warna biru */
}
```
Pada contoh ini, elemen akan memiliki:
- Jarak 20px dari elemen lain di luar elemen tersebut (margin).
- Garis border berwarna biru setebal 2px.
- Ruang 15px antara border dan konten di dalam elemen (padding).

#### Visualisasi
```CSS
+------------------------+
|        Margin          |
|  +------------------+  |
|  |     Border       |  |
|  |  +------------+  |  |
|  |  |  Padding   |  |  |
|  |  |  +------+  |  |  |
|  |  |  |Content| |  |  |
|  |  |  +------+  |  |  |
|  |  +------------+  |  |
|  +------------------+  |
+------------------------+
```

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox dan Grid Layout adalah dua model tata letak (layout) yang sangat berguna dalam CSS untuk mengatur elemen-elemen dalam desain web. Keduanya memiliki kekuatan dan kegunaannya masing-masing.

**1. Flexbox (Flexible Box Layout)**

Flexbox dirancang untuk mengatur elemen dalam satu dimensi, baik secara horizontal maupun vertikal. Ini memungkinkan elemen dalam kontainer fleksibel untuk mengubah ukuran dan posisi mereka secara dinamis untuk mengisi ruang yang tersedia.

Konsep Utama:
- Kontainer Flex: Elemen induk yang memiliki properti `display: flex`;.
- Item Flex: Elemen anak dalam kontainer flex.
- Arah: Dapat diatur untuk mengalir ke arah baris (`row`) atau kolom (`column`).

Kegunaan:
- Memudahkan perataan elemen dalam satu dimensi.
- Memungkinkan pengaturan elemen responsif yang lebih baik tanpa banyak media query.
- Cocok untuk layout sederhana seperti toolbar, daftar, dan kartu.

Contoh Implementasi:
```CSS
.container {
    display: flex;
    justify-content: space-between; /* Mengatur jarak antara item */
    align-items: center;            /* Memusatkan item secara vertikal */
}

.item {
    flex: 1;                        /* Item akan tumbuh untuk mengisi ruang yang tersedia */
}
```

**2. Grid Layout**

Grid Layout adalah sistem tata letak dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom. Ini memberikan kontrol yang lebih besar atas tata letak halaman secara keseluruhan.

Konsep Utama:
- Kontainer Grid: Elemen induk yang memiliki properti `display: grid;`.
- Item Grid: Elemen anak dalam kontainer grid.
- Baris dan Kolom: Grid dibagi menjadi baris dan kolom, dan Anda dapat mengatur ukuran setiap baris/kolom secara terpisah.

Kegunaan:
- Ideal untuk layout yang lebih kompleks, seperti desain halaman penuh, tabel, dan papan informasi.
- Memungkinkan penempatan item di dalam grid dengan posisi yang sangat fleksibel.
- Mempermudah pengaturan elemen dengan ukuran yang berbeda dan spasi yang konsisten.

Contoh Implementasi:
```CSS
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* Membagi grid menjadi 3 kolom */
    grid-gap: 10px;                         /* Spasi antara item grid */
}

.item {
    grid-column: span 2;                   /* Item ini akan mengambil 2 kolom */
    grid-row: span 1;                       /* Item ini akan mengambil 1 baris */
}
```
#### **Perbandingan :**
- Flexbox lebih baik untuk tata letak satu dimensi (baris atau kolom), sementara Grid Layout cocok untuk tata letak dua dimensi (baris dan kolom).
- Flexbox lebih mudah digunakan untuk layout yang sederhana dan responsif, sedangkan Grid memberikan kontrol yang lebih besar atas tata letak kompleks.


### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

1. Mengimplementasi fungsi mengedit dan menghapus produk dengan menambahkan fungsi tersebut pada `views.py`.
```python
def edit_product(request, id):
    # Get product entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```
```python
def delete_product(request, id):
    # Get product berdasarkan id
    product = Product.objects.get(pk = id)
    # Hapus product
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
```
2. Menambahkan *Navigation Bar* pada aplikasi
3. Mengkonfigurasi *Static FIles* pada aplikasi untuk menampilkan gambar
4. Menambahkan *Styles* pada aplikasi dengan menggunakan Tailwind serta External CSS
    - Menambahkan file `global.css`
    - Menghubungkan `global.css` dan *script* Tailwind ke `base.html`
    - Mnambahkan *custom styling* ke dalam `global.css`
5. Men-*Styling* Halaman `login`, `Register`, dan `Home`
6. Menambahkan `card_info.html` dan `card_product.html` lalu di *Styling* halaman Create Product Entry serta halaman Edit Product
7. Melakukan git add, commit, push



## Tugas 4
### 1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
`HttpResponseRedirect()` dan `redirect()` adalah dua cara untuk mengalihkan pengguna ke URL lain dalam aplikasi Django, tetapi ada beberapa perbedaan antara keduanya:
#### A. HttpResponseRedirect():
Ini adalah kelas yang secara langsung membuat respons pengalihan HTTP (HTTP 302) dan harus memberikan URL tujuan sebagai argumen.
Contoh Penggunaanya:
```python
from django.http import HttpResponseRedirect

def my_view(request):
    return HttpResponseRedirect('/some-url/')
```
#### B. redirect():
Ini adalah fungsi pembantu yang lebih fleksibel dan lebih tinggi tingkatannya. Dapat memberikan URL sebagai string, tetapi juga dapat memberikan nama view atau objek model. Fungsi ini akan mengelola pengalihan berdasarkan argumen yang diberikan.
Contoh Penggunaaannya:
```python
from django.shortcuts import redirect

def my_view(request):
    return redirect('some-view-name')
```
`redirect()` secara otomatis menangani URL yang dihasilkan dari nama view dan dapat juga menangani argumen tambahan jika diperlukan.

#### Secara umum, `redirect()` lebih umum digunakan karena kemudahannya dan dukungan untuk pengalihan berdasarkan nama view.

### 2. Jelaskan cara kerja penghubungan model `Product` dengan `User`!
Terdapat proses penghubungan antara model `Product` di aplikasi `main` dengan data `User`, yang ditambahkan sebagai field baru dalam `Product`. Dengan adanya koneksi ini, setiap `Product` kini terkait dengan seorang `User` di database. Penghubungan tersebut dilakukan melalui penambahan field `user` yang berfungsi sebagai Foreign Key ke model `User` pada model `Product`.
```python
from django.contrib.auth.models import User

class Product(models.Model): 
    # Atribut lainnya...
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Atribut lainnya...
```
Dari kode di atas, field `user` ditambahkan ke dalam model `Product` sebagai sebuah Foreign Key yang mengacu ke model `User`, sehingga setiap produk di database akan terhubung dengan pemiliknya. Foreign Key ini membuat hubungan many-to-one, artinya setiap produk hanya dimiliki oleh satu pengguna, namun satu pengguna bisa memiliki banyak produk.

Selain itu, terdapat parameter `on_delete` dengan nilai `models.CASCADE` dalam Foreign Key tersebut. Pengaturan ini memastikan bahwa jika seorang `user` dihapus dari database, semua produk yang dimiliki oleh `user` tersebut juga akan ikut terhapus. Hal ini mencegah adanya entri produk yang tidak memiliki pemilik di dalam database.

### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
- ***Authentication***

Authentication adalah proses verifikasi identitas user untuk memastikan mereka adalah yang mereka klaim. Biasanya, Authentication dilakukan dengan meminta username dan password. Dalam Django, setelah user mencoba login, kredensial mereka diperiksa. Jika valid, Django membuat session yang mengaitkan user dengan identitasnya.

Di project ini, Authentication menggunakan sistem bawaan Django melalui fungsi `login_user()` di `views.py` yang berisi :
```python
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```
Django menggunakan `AuthenticationForm()` untuk autentikasi login user. Form ini dapat ditampilkan otomatis di template HTML dengan `{{ form.as_table }}`. Setelah login berhasil, Django membuat entri session di database dan mengaitkannya dengan ID user yang terautentikasi, menggunakan middleware session.

- ***Authorization***
Authorization adalah proses verifikasi hak akses user terhadap sumber daya atau tindakan tertentu setelah mereka terautentikasi. Django menentukan aktivitas yang diizinkan untuk user, misalnya admin bisa mengakses dashboard, sementara user biasa hanya dapat melihat profilnya.

Dalam project ini, authorization diterapkan saat user ingin mengakses halaman utama, menggunakan decorator `@login_required(login_url='/login')`, yang mengarahkan user yang belum login untuk masuk terlebih dahulu. Contoh implementasinya:
```python
@login_required(login_url='/login')
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)
    ...
```
Selain `@login_required`, Django juga menyediakan decorator lain seperti `@permission_required` untuk mengelola otorisasi.


### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Cookies dalam Django digunakan untuk mengelola sesi dan menyimpan data pengguna setelah login, memungkinkan server untuk mengenali pengguna tanpa memerlukan login berulang. Selain itu, cookies bisa digunakan untuk menyimpan preferensi pengguna, personalisasi iklan, dan autentikasi berkelanjutan ("Remember Me").

Namun, tidak semua cookies aman. Pengelolaan cookies yang buruk dapat menimbulkan risiko seperti:
- Cross-Site Scripting (XSS) & Session Hijacking: Penyerang dapat mencuri session ID dan mengambil alih sesi pengguna.
- Cross-Site Request Forgery (CSRF): Penyerang dapat memanfaatkan session cookie untuk membuat pengguna melakukan tindakan tidak diinginkan tanpa sepengetahuan mereka.
- Privasi & Pelacakan: Persistent cookies dapat melacak aktivitas pengguna, mengancam privasi mereka, terutama untuk iklan yang terlalu agresif.

Django menawarkan perlindungan seperti parameter `HttpOnly`, `Secure`, dan `SameSite` untuk mencegah akses tidak sah dan menjaga keamanan cookies.


### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
**A. Implementasi registrasi, login, dan logout**

Implementasi fitur registrasi dan login dalam proyek ini dapat dilakukan dengan memanfaatkan form bawaan Django, yaitu *UserCreationForm* untuk registrasi dan *AuthenticationForm* untuk login. Berikut adalah langkah-langkah implementasinya:
1. Registrasi
- Views Registrasi: Menggunakan *UserCreationForm* untuk membuat akun baru. Jika form valid, akun disimpan dan pesan sukses ditampilkan. Pengguna akan diarahkan ke halaman login.
- Template: Halaman HTML `register.html` menampilkan form pendaftaran.
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    
    return render(request, 'register.html', {'form': form})
```
2. Login
- Views Login: Menggunakan *AuthenticationForm* untuk otentikasi. Jika valid, pengguna akan login, dan waktu login terakhir disimpan di *Cookies*.
- Template: Halaman `login.html` menampilkan form login.
```python
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    return render(request, 'login.html', {'form': AuthenticationForm(request)})
```
3. Logout
- Views Logout: Memanggil fungsi *logout()* untuk keluar, sekaligus menghapus *Cookies* login terakhir.
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
4. URLs
Pastikan semua views di atas terdaftar di `urls.py`:
```python
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```
**B. Dua Akun Dummy Dengan Masing-Masing 3 Product**
- Akun Wamly
![SS Proof](assets/assignment/DummyWamly.png)
- Akun Dani
![SS Proof](assets/assignment/DummyDani.png)
- Bukti akun di sistem admin Django
![SS Proof](assets/assignment/DjangoAcc.png)

**C. Menghubungkan model `Product` dengan `User`**

Untuk menghubungkan model `Product` dengan `User`, kita perlu menambahkan atribut baru yang berisi *ForeignKey* ke model `User`, sehingga terbentuk relasi antara kedua model tersebut. Atribut ini dapat dibuat menggunakan `models.ForeignKey()` dengan referensi ke model `User`.
```python
from django.contrib.auth.models import User

class Product(models.Model):
    ...
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
Setelah menambahkan atribut user, update database untuk menambahkan kolom baru dengan menjalankan perintah berikut:
```python
python manage.py makemigrations
python manage.py migrate
```


## Tugas 3
### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Sistem data delivery yang efisien dan aman sangat penting dalam implementasi platform untuk mengirim dan menerima data antara client dan server. Dengan menggunakan format seperti XML atau JSON, data dapat ditransfer secara cepat dan dinamis, memungkinkan platform web yang lebih responsif, misalnya melalui penggunaan teknologi AJAX. Ini memungkinkan konten halaman web diperbarui tanpa harus memuat ulang, meningkatkan pengalaman pengguna (UX) dan performa aplikasi secara keseluruhan.

Data delivery juga berperan dalam menjaga sinkronisasi data antar perangkat dan memastikan bahwa data dapat diakses secara real-time. Dengan sistem yang baik, platform dapat mengolah permintaan data secara efisien, meningkatkan interaktivitas dan responsivitas dari sisi pengguna. Selain itu, keamanan dan integritas data tetap terjaga selama proses transfer, menghindari risiko pencurian data melalui proteksi yang memadai di setiap tahap pertukaran data.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON *(JavaScript Object Notation)* cenderung lebih unggul dibandingkan XML *(Extensible Markup Language)* dalam banyak kasus, terutama untuk pertukaran data di aplikasi web. JSON lebih sederhana, ringkas, dan mudah dibaca, baik oleh manusia maupun mesin, karena tidak memerlukan tag pembuka dan penutup yang rumit seperti pada XML. Selain itu, proses parsing JSON lebih cepat di hampir semua bahasa pemrograman, terutama dalam JavaScript, yang merupakan fondasi banyak aplikasi web modern. JSON juga lebih mudah diintegrasikan dengan API dan teknologi web saat ini, sehingga membuatnya lebih populer di kalangan pengembang.

Meskipun XML masih memiliki keunggulan dalam hal struktur dokumen yang lebih kompleks dan fleksibilitas untuk representasi hierarkis, JSON lebih cocok untuk aplikasi yang berorientasi objek dan pertukaran data yang cepat dan efisien. Dukungan yang luas dari teknologi modern seperti RESTful API dan kebutuhan akan format data yang lebih ringan menjadikan JSON sebagai pilihan yang lebih umum di aplikasi web dan mobile. Pada akhirnya, kesederhanaan dan kemudahan penggunaan JSON menjadikannya lebih disukai dibandingkan XML dalam banyak skenario pengembangan modern.

### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada form Django digunakan untuk memvalidasi data yang diinputkan oleh pengguna. Fungsinya adalah memastikan bahwa data tersebut memenuhi aturan validasi yang telah ditentukan, seperti tipe data yang benar atau panjang karakter yang sesuai. Jika valid, method ini akan mengembalikan `True` dan mengisi atribut `cleaned_data` dengan data yang telah dibersihkan, siap digunakan dalam aplikasi. Method ini sangat penting untuk mencegah data yang tidak valid masuk ke dalam sistem, menjaga keamanan, dan memastikan bahwa hanya data yang valid diproses lebih lanjut.

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` diperlukan di Django untuk melindungi aplikasi dari serangan CSRF *(Cross-Site Request Forgery)*, di mana penyerang memanfaatkan sesi aktif pengguna untuk mengirim permintaan berbahaya tanpa sepengetahuan pengguna. `csrf_token` adalah token unik yang dimasukkan ke dalam form untuk memverifikasi bahwa permintaan berasal dari halaman yang sah.

Jika form tidak dilindungi oleh `csrf_token`, penyerang bisa mengirim permintaan palsu atas nama pengguna, misalnya mengubah data atau melakukan transaksi tanpa otorisasi. Dengan menambahkan `csrf_token`, aplikasi terlindung dari eksploitasi semacam ini.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat `form` input di dalam file `forms.py` untuk menambahkan produk baru di aplikasi `.
````python
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "weapon", "exterior","category","quality","price","description","quantity"]
```
Form akan ditampilkan sebagai HTML yang ada pada templates `create_product_entry.html`. Setelah itu HTML tersebut akan diproses dan dikembalikan ke user melewati fungsi `create_product_entry()` yang ada dalam `views.py`
```python
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
2. Menambahkan 4 fungsi baru di `views.py` untuk menampilkan produk yang telah ditambahkan dalam berbagai format dan opsi, yakni:
```python
# Show all product in XML
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Show all product in JSON
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Show all product in XML based on ID
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Show all product in JSON based on ID
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
3. Menambahkan URL routing untuk setiap view baru di file `main/urls.py` agar bisa diakses.
```python
...
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
...
```
4. Melakukan `add - commit - push` ke GitHub dan PWS.

### 6. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman
1. All Products in XML
![SS Proof](assets/assignment/GetAllXML.png)
2. All Products in JSON
![SS Proof](assets/assignment/GetAllJSON.png)
3. Product XML By ID
![SS Proof](assets/assignment/GetXMLByID.png)
4. Product JSON By ID
![SS Proof](assets/assignment/GetJSONByID.png)



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