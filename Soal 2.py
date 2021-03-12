print("Halo! Namaku Fajri Nur Hidayah.")
print('Aku lahir pada 25 Juni 2003, di Kabupaten Barito Kuala, Kalimantan Selatan.')
print('Saat ini aku tinggal di Kota Salatiga, Jawa Tengah.')
print('Tepatnya, rumahku berada di Perumahan Sehati, No. 137, Blotongan, Sidorejo, Kota Salatiga.')
print('Jika kamu ingin mengetahui usiaku saat ini, isilah kolom berikut: ')
tanggal_sekarang = int(input('Tanggal saat ini: '))
bulan_sekarang = int(input('Bulan saat ini: '))
tahun_sekarang = int(input('Tahun saat ini: '))
hari_sekarang = tanggal_sekarang + (bulan_sekarang * 30) + (tahun_sekarang * 365)
tanggal_lahir = 25
bulan_lahir = 6
tahun_lahir = 2003
hari_lahir = tanggal_lahir + (bulan_lahir * 30) + (tahun_lahir * 365)
tahun = int((hari_sekarang - hari_lahir) / 365)
bulan = int(((hari_sekarang - hari_lahir) % 365) / 30)
hari = int(((hari_sekarang - hari_lahir) % 365) % 30)
usia_dalam_tahun = ((hari_sekarang - hari_lahir) / 365)
print('Usiaku saat ini adalah', tahun, 'tahun,', bulan, 'bulan,', hari, 'hari.')
print('Atau', usia_dalam_tahun, 'tahun.')
bb = 40
tb = 156.5
ukuran_sepatu = 37
print('Berat badanku adalah', bb, 'kg dan tinggi badanku adalah', tb, 'cm.')
print('Ukuran sepatuku adalah', ukuran_sepatu)
print('Saat ini aku adalah mahasiswa tahun pertama di Teknik Industri, Universitas Sebelas Maret (UNS).')
jarak_salatiga_uns = 62.3
print('Jarak dari Salatiga ke UNS adalah', jarak_salatiga_uns, 'km.')
print('Aku memilih UNS karena lokasinya yang tidak terlalu jauh dari rumah.')
hobi = 'membaca, menonton film, dan belajar hal baru.'
kebiasaan_diri = 'Aku menyukai hal-hal yang terstruktur dan terjadwal dengan jelas.'
kebiasaan_diri_2 = 'Aku juga sangat menjaga jam tidurku.'
kebiasaan_diri_3 = 'Oleh karena itu, aku lebih memilih untuk belajar dan mengerjakan tugas di siang hari.'
print('Hobiku adalah', hobi)
print(kebiasaan_diri)
print(kebiasaan_diri_2  + kebiasaan_diri_3)
jumlah_anggota_keluarga = 5
jumlah_anak = 3
anak_ke = 2
print('Keluargaku terdiri dari', jumlah_anggota_keluarga, 'orang.')
print('Aku adalah anak ke', anak_ke, 'dari', jumlah_anak, 'bersaudara.')
kakak = 'perempuan'
adik = 'laki-laki'
print('Aku memiliki satu kakak', kakak, 'dan satu adik', adik)

