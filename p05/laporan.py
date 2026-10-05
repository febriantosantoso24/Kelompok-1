from komponen import LampuIndikator, Mikrofon, SensorSuhu, Servo
from statistik import ringkasan

mik = Mikrofon("mik-1")

suhu = SensorSuhu("suhu-servo")

alis = Servo("alis", 90)

data_mik = [40.0, 55.0, 60.6, 50.0, 70.0, 43.9]

data_suhu = [31.5, 36.9, 33.2, 34.8]

for nilai in data_mik:
	mik.baca(nilai)

for nilai in data_suhu:
	suhu.baca(nilai)

alis.gerak_ke(120)

led = LampuIndikator("led")
led.atur(60)

peta = {"mik": mik, "suhu": suhu, "alis": alis, "led": led}

print("=== Hasil proses tiap perangkat ===")

for kunci, p in peta.items():
	p.nyalakan()
	print(kunci, "-> hasil proses", p.proses())

print("=== Ringkasan data Mikrofon ===")

r = ringkasan(mik.data)

for kunci, nilai in r.items():
	print(kunci, "=", nilai)

