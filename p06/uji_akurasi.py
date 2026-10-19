from baca_log import baca_log
from statistik import ringkasan
from galat import galat_relatif, status


ACUAN = {
    "jumlah": 17,
    "rata": 62.4412,
    "min": 48.6,
    "maks": 73.4,
    "median": 61.8,
}


valid, ditolak = baca_log("log_mikrofon.csv")
hasil = ringkasan(valid)

print("parameter | hasil | acuan | galat (%) | status")

for kunci, acuan in ACUAN.items():
    galat_persen = galat_relatif(hasil[kunci], acuan)
    print(
        kunci,
        "|",
        hasil[kunci],
        "|",
        acuan,
        "|",
        galat_persen,
        "|",
        status(galat_persen),
    )