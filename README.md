# 🎓 Dashboard Analitik Universitas

> Dashboard interaktif untuk analisis dan monitoring data mahasiswa berbasis web

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📊 Sumber Data

Dashboard ini menggunakan tiga dataset utama:

### 1. **students.csv**
Dataset mahasiswa yang berisi informasi:
- `student_id`: ID unik mahasiswa
- `name`: Nama lengkap mahasiswa
- `faculty`: Nama fakultas
- `major`: Program studi
- `year_enrolled`: Tahun masuk/pendaftaran
- `gender`: Jenis kelamin (Male/Female)
- `age`: Usia mahasiswa
- `gpa`: Indeks Prestasi Kumulatif (0.00-4.00)
- `status`: Status mahasiswa (Active/Graduated/Inactive)

### 2. **academic_performance.csv**
Dataset performa akademik mahasiswa per semester

### 3. **faculty.csv**
Dataset informasi detail fakultas dan program studi

> **Catatan**: Data yang digunakan adalah data dummy/sampel untuk keperluan demonstrasi dashboard

---

## 🌐 Akses Dashboard

### Cara Menjalankan di Lokal

#### **Prasyarat**
- Python 3.8 atau lebih tinggi
- pip (Python package installer)

#### **Langkah-langkah Instalasi**

1. **Clone repository**
   ```bash
   git clone https://github.com/username/university-dashboard.git
   cd university-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan aplikasi**
   ```bash
   streamlit run app.py
   ```

4. **Akses di browser**
   ```
   http://localhost:8501
   ```

### Akses Online (Deployment)

Dashboard dapat diakses secara online melalui:

🔗 **[Live Demo Dashboard](https://your-dashboard-url.streamlit.app)**

> *Ganti URL di atas dengan link deployment Streamlit Cloud/Heroku Anda*

---

## 📝 Deskripsi Dashboard

**Dashboard Analitik Universitas** adalah aplikasi web interaktif yang dirancang untuk membantu administrator universitas, dosen, dan stakeholder pendidikan dalam:

- 📊 **Memantau data mahasiswa** secara real-time
- 📈 **Menganalisis tren penerimaan** mahasiswa dari tahun ke tahun
- 🎯 **Melihat distribusi mahasiswa** per fakultas dan program studi
- 💯 **Mengevaluasi performa akademik** melalui IPK rata-rata
- 👥 **Memahami demografi mahasiswa** berdasarkan gender dan usia
- 📉 **Mengidentifikasi pola** dalam status keaktifan mahasiswa

Dashboard ini dibangun menggunakan **Streamlit** untuk antarmuka web, **Plotly** dan **Matplotlib** untuk visualisasi interaktif, serta **Pandas** untuk pengolahan data. Semua visualisasi dirancang dengan prinsip **user-friendly** dan **responsive design** agar mudah diakses dari berbagai perangkat.

### 🎯 Tujuan Dashboard

1. **Memudahkan Pengambilan Keputusan** - Menyajikan data dalam format visual yang mudah dipahami
2. **Meningkatkan Efisiensi** - Mengurangi waktu analisis data manual
3. **Monitoring Real-time** - Memantau KPI (Key Performance Indicators) secara langsung
4. **Data-Driven Insights** - Memberikan insight berbasis data untuk strategi akademik

---

## ✨ Fitur Utama Dashboard

### 🔍 **1. Filter Interaktif**
Dashboard dilengkapi dengan sidebar filter yang memungkinkan pengguna untuk:
- **Filter Tahun**: Pilih rentang tahun pendaftaran mahasiswa (slider)
- **Filter Fakultas**: Pilih satu atau beberapa fakultas (multi-select)
- **Filter Gender**: Filter berdasarkan jenis kelamin (dropdown)

Filter ini bekerja secara **real-time** dan langsung memperbarui seluruh visualisasi.

### 📊 **2. KPI Metrics Cards**
Empat metrik utama yang ditampilkan di bagian atas dashboard:
- **Total Mahasiswa** - Jumlah total mahasiswa sesuai filter
- **IPK Rata-rata** - Nilai rata-rata IPK dengan indikator perubahan
- **Jumlah Fakultas** - Total fakultas yang tersedia
- **Mahasiswa Aktif** - Jumlah mahasiswa dengan status aktif

Setiap metric dilengkapi dengan **delta indicator** (↑↓) untuk menunjukkan perubahan.

### 📈 **3. Visualisasi Data Interaktif**
Enam visualisasi utama yang dapat berinteraksi dengan filter:

#### a. **Distribusi Mahasiswa per Fakultas** (Bar Chart)
- Menampilkan jumlah mahasiswa di setiap fakultas
- Tooltip interaktif saat hover
- Warna biru konsisten untuk branding

#### b. **Tren Jumlah Mahasiswa per Tahun** (Line Chart)
- Menunjukkan pola penerimaan mahasiswa dari tahun ke tahun
- Membantu identifikasi tren naik/turun
- Ideal untuk perencanaan kapasitas

#### c. **Status Mahasiswa** (Pie Chart)
- Distribusi status: Active, Graduated, Inactive
- Persentase dan jumlah absolut
- Warna-warna soft & modern

#### d. **IPK Rata-rata per Fakultas** (Horizontal Bar Chart)
- Perbandingan performa akademik antar fakultas
- Menampilkan IPK dan jumlah mahasiswa
- Sorted dari tertinggi ke terendah

#### e. **Distribusi Gender** (Pie Chart)
- Proporsi mahasiswa berdasarkan gender
- Membantu analisis keseimbangan gender

#### f. **Top 5 Program Studi** (Bar Chart)
- Menampilkan 5 program studi dengan mahasiswa terbanyak
- Membantu identifikasi program studi populer

### 📋 **4. Tabel Data Mahasiswa**
- Tabel interaktif dengan **scrolling vertikal**
- Menampilkan semua kolom data mahasiswa
- **Height fixed** (500px) untuk UX yang lebih baik
- Search dan sort capability

### 📥 **5. Export Data**
- **Download button** untuk export data ke CSV
- File otomatis diberi nama dengan timestamp
- Format: `data_mahasiswa_YYYYMMDD_HHMMSS.csv`

### 📊 **6. Statistik Ringkasan**
Tabel statistik yang menampilkan:
- Jumlah Total Mahasiswa
- IPK Rata-rata
- IPK Tertinggi
- IPK Terendah
- Rata-rata Umur Mahasiswa

---

## 📈 Visualisasi Data

Dashboard ini menggunakan kombinasi library visualisasi untuk hasil optimal:

### 🎨 **Library yang Digunakan**

| Library | Fungsi | Visualisasi |
|---------|--------|-------------|
| **Plotly** | Interactive charts | Bar Chart (Fakultas & Prodi) |
| **Streamlit** | Built-in charts | Line Chart (Tren Tahunan) |
| **Matplotlib** | Static charts | Pie Chart (Status & Gender), Horizontal Bar (IPK) |

### 📊 **Jenis Visualisasi**

#### 1. **Bar Chart** - Perbandingan Kategori
- Distribusi Mahasiswa per Fakultas
- Top 5 Program Studi
- **Cocok untuk**: Membandingkan nilai antar kategori

#### 2. **Line Chart** - Tren Waktu
- Tren Jumlah Mahasiswa per Tahun
- **Cocok untuk**: Melihat perubahan dari waktu ke waktu

#### 3. **Pie Chart** - Proporsi
- Status Mahasiswa
- Distribusi Gender
- **Cocok untuk**: Menunjukkan bagian dari keseluruhan

#### 4. **Horizontal Bar Chart** - Ranking
- IPK Rata-rata per Fakultas
- **Cocok untuk**: Membandingkan dan ranking nilai

### 🎨 **Desain & Styling**
- **Color Palette**: Soft modern colors (#60a5fa, #34d399, #fbbf24, dll)
- **Background**: Clean white dengan kontras yang baik
- **Typography**: Font Arial yang readable
- **Interactivity**: Hover tooltips, exploded pie charts
- **Consistency**: Warna dan style konsisten di semua chart

---

## 📸 Tampilan Dashboard

### 1. **Dashboard Utama (Full View)**
Tampilan lengkap dashboard dengan KPI metrics, filter sidebar, dan preview visualisasi.

![Dashboard Main](screenshots/dashboard-main.png)

*Screenshot: Tampilan utama dashboard dengan semua komponen*

---

### 2. **KPI Metrics Cards**
Empat metrik utama di bagian atas dashboard dengan delta indicators.

![KPI Metrics](screenshots/kpi-metrics.png)

*Screenshot: Total Mahasiswa, IPK Rata-rata, Jumlah Fakultas, dan Mahasiswa Aktif*

---

### 3. **Visualisasi Data - Distribusi & Tren**
Dua visualisasi side-by-side: distribusi per fakultas dan tren tahunan.

![Visualization 1](screenshots/visualization-1.png)

*Screenshot: Bar chart distribusi fakultas dan line chart tren tahunan*

---

### 4. **Visualisasi Data - Status Mahasiswa**
Pie chart interaktif menampilkan proporsi status mahasiswa (Active/Graduated/Inactive).

![Status Chart](screenshots/status-chart.png)

*Screenshot: Pie chart dengan persentase dan jumlah mahasiswa per status*

---

### 5. **Visualisasi Data - IPK per Fakultas**
Horizontal bar chart membandingkan IPK rata-rata antar fakultas dengan jumlah mahasiswa.

![IPK Chart](screenshots/ipk-chart.png)

*Screenshot: Comparison IPK rata-rata dengan sorting dari tertinggi ke terendah*

---

### 6. **Visualisasi Data - Distribusi Gender**
Pie chart menunjukkan proporsi mahasiswa laki-laki dan perempuan.

![Gender Chart](screenshots/gender-chart.png)

*Screenshot: Distribusi gender dengan color coding yang jelas*

---

### 7. **Filter Sidebar**
Sidebar dengan tiga filter utama: Tahun, Fakultas, dan Gender.

![Sidebar](screenshots/sidebar.png)

*Screenshot: Filter interaktif dengan slider, multi-select, dan dropdown*

---

### 8. **Tabel Data Mahasiswa**
Tabel interaktif dengan scrolling vertikal dan semua informasi mahasiswa.

![Data Table](screenshots/data-table.png)

*Screenshot: Tabel dengan fixed height dan scrolling untuk banyak data*

---

### 9. **Statistik & Top Program Studi**
Statistik ringkasan dan bar chart top 5 program studi terpopuler.

![Statistics](screenshots/statistics.png)

*Screenshot: Tabel statistik dan visualisasi program studi populer*

---

### 10. **Download Button**
Fitur export data dengan button yang user-friendly.

![Download](screenshots/download-button.png)

*Screenshot: Button download dengan format CSV dan timestamp otomatis*

---

## 🛠️ Teknologi yang Digunakan

```python
streamlit==1.28.0      # Web framework
pandas==2.0.3          # Data manipulation
numpy==1.24.3          # Numerical computing
matplotlib==3.7.2      # Static visualization
plotly==5.17.0         # Interactive visualization
```

---

## 📂 Struktur Project

```
university-dashboard/
│
├── app.py                      # Main application file
├── style.css                   # Custom styling
├── students.csv                # Student dataset
├── academic_performance.csv    # Academic data
├── faculty.csv                 # Faculty data
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
├── .gitignore                  # Git ignore file
│
└── screenshots/                # Dashboard screenshots
    ├── dashboard-main.png
    ├── kpi-metrics.png
    ├── visualization-1.png
    ├── status-chart.png
    ├── ipk-chart.png
    ├── gender-chart.png
    ├── sidebar.png
    ├── data-table.png
    ├── statistics.png
    └── download-button.png
```

---

## 🚀 Deployment

Dashboard dapat di-deploy ke berbagai platform:

### **Streamlit Cloud** (Recommended)
1. Push code ke GitHub
2. Kunjungi [share.streamlit.io](https://share.streamlit.io)
3. Connect repository
4. Deploy!

### **Heroku**
```bash
heroku create university-dashboard
git push heroku main
```

### **Docker**
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD streamlit run app.py
```

---

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

---

## 📄 Lisensi

Project ini dilisensikan di bawah **MIT License**.

---

## 👨‍💻 Author

**[Nama Anda]**
- 📧 Email: your.email@example.com
- 💼 LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- 🐙 GitHub: [@yourusername](https://github.com/yourusername)

---

## 🙏 Acknowledgments

- Streamlit Team untuk framework yang powerful
- Plotly untuk visualisasi interaktif
- Komunitas Python Indonesia
- [Nama Universitas] untuk data reference

---

## 📚 Dokumentasi Tambahan

- [Streamlit Documentation](https://docs.streamlit.io)
- [Plotly Python](https://plotly.com/python/)
- [Pandas Guide](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

---

<p align="center">
  <strong>⭐ Star project ini jika bermanfaat! ⭐</strong>
</p>

<p align="center">
  Made with ❤️ using <a href="https://streamlit.io">Streamlit</a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/username/university-dashboard?style=social" alt="GitHub stars">
  <img src="https://img.shields.io/github/forks/username/university-dashboard?style=social" alt="GitHub forks">
  <img src="https://img.shields.io/github/watchers/username/university-dashboard?style=social" alt="GitHub watchers">
</p>
