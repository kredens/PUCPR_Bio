def newlist (sizeBlock, startPosition, stringNative):
	stringFinal = []
	p = startPosition
	g = 0
	#criar o primeiro bloco quando este for incompleto
	if(startPosition != 0):
		inc = ""
		for cont in range (0,startPosition):
			inc = inc + stringNative[cont]
		stringFinal.append(inc)
	#criar os blocos principais
	blc = ((len(stringNative)-startPosition)//sizeBlock)
	while (g < blc):
		inc = ""
		for x in range (0, sizeBlock):
			inc = inc + stringNative[p]
			p = p + 1
		g = g + 1
		stringFinal.append(inc)
	#criar o ultimo bloco quando este for incompleto
	if(((len(stringNative)-startPosition)%sizeBlock) != 0):
		inc = ""
		for count in range ((blc*sizeBlock)+startPosition, len(stringNative)):
			inc = inc + stringNative[count]
		stringFinal.append(inc)
	return stringFinal
