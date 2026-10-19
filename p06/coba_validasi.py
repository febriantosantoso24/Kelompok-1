from validasi import periksa

contoh = [
	"",
	"ERR",
	"--",
	"-999",
	"250",
	"61.8",
	"61,8",
	"6e1",
	"nan",
	" 61.8 ",
	"30.0",
	"29.9",
	"120",
	"120.1",
]

for teks in contoh:
	try:
		nilai = periksa(teks)
		print(repr(teks), "-> diterima", nilai)
	except ValueError as e:
		print(repr(teks), "-> ditolak:", e)

# Butir 5:
# - Tebakan "61,8" diterima ternyata salah: float() Python hanya menerima
#   titik sebagai pemisah desimal, sehingga nilai ini ditolak sebagai bukan
#   angka.
# - Tebakan "6e1" ditolak ternyata salah: notasi ilmiah sah untuk float(),
#   sehingga nilai ini diterima sebagai 60.0.
# - Tebakan "nan" ditolak benar: NaN tidak memenuhi perbandingan batas bawah
#   maupun batas atas, sehingga ditolak sebagai di luar rentang.