class Emosi:
	def __init__(self, skor):
		self.skor = skor

	def tentukan_label(self):
		if self.skor >= 0.6:
			return "senang"
		if self.skor <= 0.3:
			return "sedih"
		return "netral"
