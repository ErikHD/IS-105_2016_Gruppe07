#Denne algoritmen koder om bokstaver A-F til deres korresponderende binaerverdi

#Mapper verdiene
abcToBin = { 'A': '10', 'B': '01', 'C': '111', 'D': '110', 'E': '001', 'F': '000' }

#Henter input og kapitaliserer, koder om til binaer
def CodeToBin() : 
	holdingString = ""
	inputString = raw_input("ABC skrives her: ")
	inputString = inputString.upper()

	for key in inputString:
		holdingString = holdingString + abcToBin[key]

	print ("Kodet om til: " + holdingString)



CodeToBin()