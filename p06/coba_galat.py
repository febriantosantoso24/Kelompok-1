from galat import galat_absolut, galat_relatif, status


pasangan = [
    (52.5, 50.0),
    (100.25, 100.0),
    (45.0, 60.0),
    (7.0, 0),
]


for hasil, acuan in pasangan:
    try:
        galat_persen = galat_relatif(hasil, acuan)
        print(
            (hasil, acuan),
            "galat absolut:",
            galat_absolut(hasil, acuan),
            "galat relatif:",
            galat_persen,
            "%",
            "status:",
            status(galat_persen),
        )
    except ValueError as e:
        print((hasil, acuan), "galat:", e)