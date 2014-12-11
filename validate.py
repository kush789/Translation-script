def takelanguages():
	chechklang1 = 1
	chechklang2 = 1
	langset = ['ca', 'cs', 'pt', 'tr', 'lv', 'lt', 'th', 'pl', 'hy', 'hr', 'de', 'da', 'he', 'mk', 'mt', 'uk', 'el', 'en', 'zh', 'vi', 'is', 'it', 'ar', 'et', 'az', 'id', 'es', 'ru', 'nl', 'no', 'ro', 'be', 'fr', 'bg', 'ms', 'bs', 'fi', 'hu', 'ka', 'sr', 'sq', 'sv', 'sk', 'sl']
	while (chechklang1):
		print """
Select language input text is in : (Enter the correct code please)

 -  ar Arabic
 -  az Azerbaijani
 -  be Belarusian
 -  bg Bulgarian
 -  bs Bosnian
 -  ca Catalan
 -  cs Czech
 -  da Danish
 -  de German
 -  el Greek
 -  en English
 -  es Spanish
 -  et Estonian
 -  fi Finnish
 -  fr French
 -  he Hebrew
 -  hr Croatian
 -  hu Hungarian
 -  hy Armenian
 -  id Indonesian
 -  is Icelandic
 -  it Italian
 -  ka Georgian
 -  lt Lithuanian
 -  lv Latvian
 -  mk Macedonian
 -  ms Malay
 -  mt Maltese
 -  nl Dutch
 -  no Norwegian
 -  pl Polish
 -  pt Portuguese
 -  ro Romanian
 -  ru Russian
 -  sk Slovak
 -  sl Slovenian
 -  sq Albanian
 -  sr Serbian
 -  sv Swedish
 -  th Thai
 -  tr Turkish
 -  uk Ukrainian
 -  vi Vietnamese
 -  zh Chinese

==================================================	"""
		fromlang = raw_input()
		if fromlang in langset:
			chechklang1 = 0
		else:
			print "\nPlease select a correct code\n"
	while (chechklang2):
		print """
Select language you want to translate to : (Enter the correct code please)

 -  ar Arabic
 -  az Azerbaijani
 -  be Belarusian
 -  bg Bulgarian
 -  bs Bosnian
 -  ca Catalan
 -  cs Czech
 -  da Danish
 -  de German
 -  el Greek
 -  en English
 -  es Spanish
 -  et Estonian
 -  fi Finnish
 -  fr French
 -  he Hebrew
 -  hr Croatian
 -  hu Hungarian
 -  hy Armenian
 -  id Indonesian
 -  is Icelandic
 -  it Italian
 -  ka Georgian
 -  lt Lithuanian
 -  lv Latvian
 -  mk Macedonian
 -  ms Malay
 -  mt Maltese
 -  nl Dutch
 -  no Norwegian
 -  pl Polish
 -  pt Portuguese
 -  ro Romanian
 -  ru Russian
 -  sk Slovak
 -  sl Slovenian
 -  sq Albanian
 -  sr Serbian
 -  sv Swedish
 -  th Thai
 -  tr Turkish
 -  uk Ukrainian
 -  vi Vietnamese
 -  zh Chinese

==================================================	"""
		tolang = raw_input()

		if fromlang in langset:
			chechklang2 = 0
		else:
			print "\nPlease select a correct code\n"
	return fromlang,tolang
