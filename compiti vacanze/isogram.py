def is_isogram(string):
	for lettera in 'abcdefghijklmnopqrstuvwxyz':
		cont = 0
		for letteraP in string:
			if lettera == letteraP.lower():
				cont += 1
		if cont > 1:
			return False
	return True