# Logistic Routing Problem

<img src="https://picjumbo.com/wp-content/uploads/white-tir-truck-in-motion-driving-on-highway_free_stock_photos_picjumbo_DSC04205-1080x720.jpg" class="img-responsive" width="50%" height="50%"><img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Luftaufnahmen_Nordseekueste_2013_05_by-RaBoe_tele_46.jpg" class="img-responsive" width="50%" height="50%">

## Tujuan Tugas
1. Review materi pathfinding pada mata kuliah Strategi Algoritma.
2. Mengenal multiple-agent TSP.
3. Melakukan visualisasi data.

## Deskripsi Masalah
Welcome to **Oldenburg** ! Kota kecil cantik ini merupakan sebuah kota kecil di barat laut kota Bremen , Jerman , dengan penduduk kurang lebih 168 ribu jiwa [2018]. Kota kecil ini cocok menjadi lahan uji coba untuk melakukan pemodelan sederhana pembuatan rute pengantaran logistik.<br>
Setiap beberapa jam sekali, sebuah perusahaan logistik akan mengirimkan beberapa kurirnya untuk mengantar barang dari kantor pusat mereka ke beberapa titik tujuan yang tersebar di penjuru kota Oldenburg. Anda diminta untuk mencari rute untuk seluruh kurir sehingga jarak yang ditempuh oleh semua kurir paling kecil, sehingga perusahaan logistik dapat menghemat biaya bensin.

## Multiple-Agent TSP
Masalah pengantaran barang untuk satu kendaraan dengan fungsi objektif jarak minimal dapat dimodelkan oleh Travelling Salesman Problem. Akan tetapi, perusahaan logistik biasanya memiliki lebih dari satu kendaraan yang berangkat bersamaan, sehingga TSP kurang cocok digunakan. Generalisasi TSP untuk beberapa agen adalah **multiple-agent TSP (mTSP)**, dan model masalah ini akan kita gunakan. Pada mTSP, akan terdapat *m* tur yang akan dibangun. Syarat dari semua tur mirip dengan TSP, yaitu bahwa seluruh tur akan kembali ke simpul awal (mewakili kantor pusat) dan setiap tujuan hanya akan dilewati oleh satu tur.

## Milestone 1
Pada milestone 1, anda diminta untuk membangun sebuah upagraf dari graf jalan keseluruhan kota Oldenburg. Upagraf tersebut merupakan sebuah graf lengkap tak berarah, dengan simpul-simpulnya adalah titik tujuan pengiriman barang ditambah titik yang mewakili kantor pusat perusahaan logistik. Hasilkan sebuah matriks jarak antar simpul upagraf lengkap. Nilai untuk milestone pertama maksimal adalah **600**.

## Pathfinding
  Pathfinding merupakan teknik penelusuran graf pada graf berbobot yang digunakan untuk mencari rute dengan bobot terpendek dari satu simpul ke simpul lainnya. Dalam penyelesaian Logistic Routing Problem, pathfinding digunakan untuk menelusuri jalan sehingga diperoleh rute dengan jarak tempuh terpendek.
  Setiap kota atau titik dalam suatu daerah direpresentasikan oleh simpul-simpul pada graf. Setiap jalan yang menghubungkan antar kota direpresentasikan oleh sisi(v,w) dengan v adalah simpul asal dan w adalah simpul tujuan. Setiap jalan tentu memiliki jaraknya masing-masing sehingga setiap sisi(v,w) memiliki bobot bernilai jarak tersebut.
  Pendekatan pathfinding yang digunakan adalah algoritma A*. Algoritma A* adalah algoritma heuristik yang populer digunakan dalam menelusuri graf sehingga diperoleh rute terpendek. Algoritma A* memiliki formula umum sebagai berikut.
  ```
  f(n) = g(n) + h(n)
  ```
  Dalam kasus Logistic Routing Problem, setiap komponen tersebut memiliki makna sebagai berikut.
  f(n) = cost total untuk mencapai simpul tujuan melalui simpul n
  g(n) = jarak tempuh yang sudah ditempuh dari simpul asal ke simpul n
  h(n) = nilai heuristik berdasarkan jarak garis lurus antara simpul n ke simpul tujuan

  Nilai heuristik h(n) dikatakan feasible apabila jarak garis lurus antara simpul n ke simpul tujuan tidak melebihi jarak perjalanan simpul n ke simpul tujuan yang sebenarnya.

  Keterangan:
  x1 = posisi horizontal x dari titik asal pada koordinat kartesius
  x2 = posisi horizontal x dari titik tujuan pada koordinat kartesius
  y1 = posisi vertikal y dari titik asal pada koordinat kartesius
  y2 = posisi vertikal y dari titik tujuan pada koordinat kartesius
  
  Nilai f(n) ini akan menjadi pertimbangan dalam memilih simpul-simpul selanjutnya dalam penelusuran graf. Dengan demikian, penelusuran graf bisa berjalan lebih cepat dalam mencapai simpul tujuan.

## Cara Menjalankan Program
Untuk menjalankan aplikasi ini, dari root directory project ini dapat pindah ke folder src dengan command "cd src". Kemudian, jalankan file main.py dengan command :
```
cd src
python graph.py
```
Masukkan untuk kota berupa "OL" atau "SF". OL untuk kota Oldenburg dan SF untuk San Fransisco.

## Referensi
Silahkan gunakan referensi berikut sebagai awal pengerjaan tugas:<br>
[1] Dataset : https://www.cs.utah.edu/~lifeifei/SpatialDataset.htm<br>
[2] Pengenalan dan formulasi mTSP : https://neos-guide.org/content/multiple-traveling-salesman-problem-mtsp<br>
[3] MIP , pustaka Python untuk optimisasi : https://python-mip.readthedocs.io/en/latest/intro.html<br>
[4] OpenGL untuk Python : https://stackabuse.com/brief-introduction-to-opengl-in-python-with-pyopengl/<br>

## Credits

Akhir Kata, selamat bersenang-senang !

