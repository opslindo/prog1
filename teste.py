def rafa(palavra,procu):
	cont = 0
	for i in palavra:
		if proc == i:
			cont += 1

	print("foram encontra apenas {} letra do {}". format(cont,proc))


palavra = input("Informe a palavra:")
proc = input("Informe a procura:")
rafa(palavra, proc)
