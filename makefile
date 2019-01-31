all: picmaker.py
	python3 picmaker.py
	display image.ppm
	rm image.ppm
