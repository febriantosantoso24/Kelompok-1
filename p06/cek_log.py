from pathlib import Path

from baca_log import baca_log, hitung_alasan


nama_berkas = Path(__file__).with_name("log_mikrofon.csv")
valid, ditolak = baca_log(nama_berkas)


print("Data valid:", len(valid))
print("Data ditolak:", len(ditolak))


for no, isi, alasan in ditolak:
	print("baris", no, "|", isi, "|", alasan)

print(hitung_alasan(ditolak))