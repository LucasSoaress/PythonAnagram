import itertools
word = raw_input("Digite sua palavra: ")
print(" ")
anagramas = sorted(set(["".join(perm) for perm in itertools.permutations(word)]))
contador = 1;

for index in range(len(anagramas)):
	print( " " + str(contador) +" - " + anagramas[index])
	contador+=1



