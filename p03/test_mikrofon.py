from mikrofon import Mikrofon


def test_kondisi_awal():
    mic = Mikrofon("Mic 1")

    assert mic.nama == "Mic 1"
    assert mic.aktif == False
    assert mic.level == 0


def test_nyalakan():
    mic = Mikrofon("Mic 1")

    mic.nyalakan()

    assert mic.aktif == True


def test_matikan():
    mic = Mikrofon("Mic 1")

    mic.nyalakan()
    mic.set_level(50)
    mic.matikan()

    assert mic.aktif == False
    assert mic.level == 0


def test_set_level_saat_aktif():
    mic = Mikrofon("Mic 1")

    mic.nyalakan()
    mic.set_level(75)

    assert mic.level == 75


def test_set_level_saat_mati():
    mic = Mikrofon("Mic 1")

    mic.set_level(75)

    assert mic.level == 0