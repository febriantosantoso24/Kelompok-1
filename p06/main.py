from komponen import LampuIndikator, Mikrofon, SensorSuhu, Servo

mik = Mikrofon("mik-1")

suhu = SensorSuhu("suhu-servo")

alis = Servo("alis", 90)

mik.baca (40.0)

mik.baca(55.8)

mik.baca(70.0)

suhu.baca(31.5)

suhu.baca(36.8)

suhu.baca(33.2)

alis.gerak_ke(120)

lampu = LampuIndikator("lampu-indikator")
lampu.atur(80)

daftar = [mik, suhu, alis, lampu]

for p in daftar:
	p.nyalakan()
	hasil = p.proses()
	print(p, "->", hasil)