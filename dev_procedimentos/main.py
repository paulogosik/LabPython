procedimentos = []


arquivo = open("diretriz.txt", "r+", encoding="utf8")
conteudo = arquivo.readlines()
for line in conteudo:
    line = line.split("\n")
    procedimento = f"{line[0]};"
    procedimentos.append(procedimento)

print(procedimentos)

arquivo = open("teste.txt", "r+", encoding="utf8")
arquivo.writelines(procedimentos)