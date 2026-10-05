from statistik import median, rata_rata, rentang, ringkasan


def test_rata_rata():
	assert rata_rata([10.0, 20.0, 30.0]) == 20.0


def test_rentang():
	assert rentang([5.0, 0.0, 1.0, 9.0]) == (0.0, 9.0)


def test_ringkasan():
	hasil = ringkasan([2.0, 4.0, 6.0])

	assert hasil["jumlah"] == 3
	assert hasil["rata"] == 4.0


def test_median_ganjil():
	assert median([30.0, 10.0, 20.0]) == 20.0


def test_median_genap():
	assert median([48.0, 10.0, 30.0, 20.0]) == 25.0


def test_median_tidak_mengubah_data():
	data = [3.0, 0.0, 1.0, 2.0]

	median(data)

	assert data == [3.0, 0.0, 1.0, 2.0]