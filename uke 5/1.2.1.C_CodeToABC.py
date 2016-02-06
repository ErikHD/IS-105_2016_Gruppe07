#Denne algoritmen koder om binaerverdier til deres korresponderende bokstaver

#Mapper verdiene

binToAbc = { '10': 'A', '01': 'B', '111': 'C', '110': 'D', '001': 'E', '000': 'F' }

#Henter input og samler slik at ikke tall tolkes 1om gangen, koder om til binaer
def CodeToAbc() :
	collect = ""
	holdingString = ""
	inputString = raw_input("Tall skrives her: ")
	
	for key in inputString:
		collect = collect + key
		if binToAbc.has_key(collect):
			holdingString = holdingString + binToAbc[collect]
			collect = ""


	print ("Kodet om til: " + holdingString)

CodeToAbc()