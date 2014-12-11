def takelanguages():
	chechklang1 = 1
	chechklang2 = 1
	langset = ["ru","en","pl","uk","de","fr","es","it","bg","cs","tr","ro","se"]
	while (chechklang1):
		print """
Select language input text is in : (Enter the correct code please)

	ru : Russian
	en : English
	pl : Polska
	uk : Ukrainian
	de : German
	fr : French
	es : spanish
	it : Italian
	bg : Bulgarian
	cs : czech
	tr : Turkish
	ro : Romanian
	sr : Serbian

==================================================	"""
		fromlang = raw_input()
		if fromlang in langset:
			chechklang1 = 0
		else:
			print "\nPlease select a correct code\n"
	while (chechklang2):
		print """
Select language you want to translate to : (Enter the correct code please)

	ru : Russian
	en : English
	pl : Polska
	uk : Ukrainian
	de : German
	fr : French
	es : spanish
	it : Italian
	bg : Bulgarian
	cs : czech
	tr : Turkish
	ro : Romanian
	sr : Serbian

==================================================	"""
		tolang = raw_input()

		if fromlang in langset:
			chechklang2 = 0
		else:
			print "\nPlease select a correct code\n"
	return fromlang,tolang
