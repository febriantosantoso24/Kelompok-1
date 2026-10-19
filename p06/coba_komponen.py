from komponen import Mikrofon, Servo

mik = Mikrofon("mik-1")

for nilai in [58.2, 61.0, -999.8, 258.8, 64.5]:
    try:
        mik.baca(nilai)
    except ValueError as e:
        print("ditolak:", nilai, "|", e)

print(mik.data)
print(mik.proses())

mik2 = Mikrofon("mik-2")

try:
    print(mik2.proses())
except ValueError as e:
    print("galat:", e)

alis = Servo("alis", 90)

for sudut in [45, 180, 200, -10]:
    try:
        alis.gerak_ke(sudut)
        print("sudut diterima:", alis.proses())
    except ValueError as e:
        print("ditolak:", sudut, "|", e, "| posisi tetap", alis.proses())