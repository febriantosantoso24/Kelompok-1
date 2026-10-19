def rata_rata(data):
	return sum(data) / len(data)


def tertinggi(data):
	return max(data)


def terendah(data):
	return min(data)


def rentang(data):
	return (min(data), max(data))


def galat_absolut(hasil, acuan):
	return abs(hasil - acuan)


def galat_relatif(hasil, acuan):
	if acuan == 0:
		raise ValueError("acuan 0, galat relatif tidak dapat dihitung")

	return galat_absolut(hasil, acuan) / abs(acuan) * 100


def ringkasan(data):
	return {
		"jumlah": len(data),
		"rata": round(rata_rata(data), 2),
		"min": min(data),
		"maks": max(data),
		"median": median(data),
	}


def median(data):
	data_urut = sorted(data)
	n = len(data_urut)
	tengah = n // 2

	if n % 2 == 1:
		return data_urut[tengah]
	return (data_urut[tengah - 1] + data_urut[tengah]) / 2