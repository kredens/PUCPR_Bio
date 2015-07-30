def verificarbloco (sizeBlock,sizeString,startPosition):
	numMaxBloc = (sizeString//2)
	if (numMaxBloc >= sizeBlock):
		return True
	else:
			if ((startPosition + sizeBlock) <= sizeString):
				return True
			else:
				return False
