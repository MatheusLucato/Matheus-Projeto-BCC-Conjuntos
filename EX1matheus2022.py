#ler o arquivo txt
file = open("teste.txt", "r")

operacoes = ['U','I', 'D', 'C']
matriz = []
matrizFormatada = []
resultado = []
chars = ','
texto = file.readlines()  #quebra as linhas do arquivo em um vetor só

for i in range(len(texto)):  #esse for percorre as posições do vetor 'texto' e cria um vetor de cada linha dentro da "matriz" transformando as linhas em palavras, excluindo o \n
    matriz.append(texto[i].split())

for j in range(len(matriz)):
    v  = []
    for m in range(len(matriz[j])): #for's para retirar as ',' das strings
        c = matriz[j][m]
        form = c.translate(str.maketrans('', '', chars))
        v.append(form)
    matrizFormatada.append(v)

for linhas in matrizFormatada: #mostrar de uma forma mais bonita
    print(linhas)

for i in range(len(matrizFormatada)):
    if matrizFormatada[i][0] in operacoes:
        operacao = matrizFormatada[i][0]
        if operacao == 'U': #verificar se a operação é UNIAO
            for j in range(len(matrizFormatada[i+1])): #for para adicionar a primeira linha após a letra da operação
                a = matrizFormatada[i+1][j]
                if a not in resultado: #if para procurar/evitar repetido
                    resultado.append(a)
            for k in range(len(matrizFormatada[i+2])): #for para adicionar a segunda linha após a letra da operação
                b = matrizFormatada[i+2][k]
                if b not in resultado: #if para procurar/evitar repetido
                    resultado.append(b)
            print("União: conjunto 1 {",(','.join(matrizFormatada[i+1])),"}, conjunto 2 {",(','.join(matrizFormatada[i+2])),"}, resultado {",','.join(resultado),"}\n") #Saida união
            resultado.clear()
        elif operacao == 'I': #verificar se a operação é INTERSECÇÃO
            for b in range(len(matrizFormatada[i+1])):
                a = matrizFormatada[i+1][b]
                if a in matrizFormatada[i+2]: #if para analisar o a (elemento da linha i+1 e coluna b) esta presente na linha debaixo
                    if a not in resultado: #if para procurar/evitar repetido
                        resultado.append(a)
            print("\nIntersecção: conjunto 1 {",(','.join(matrizFormatada[i+1])),"}, conjunto 2 {",(','.join(matrizFormatada[i+2])),"}, resultado {",(','.join(resultado)),"}\n") #Saida Intersecção
            resultado.clear()
        elif operacao == 'D': #verificar se a operação é DIFERENCIAL
            for p in range(len(matrizFormatada[i+1])):
                a = matrizFormatada[i+1][p]
                if a not in matrizFormatada[i+2]: #if para analisar se o elemento aparece apenas na linha do a (elemento de linha i+1 e coluna p)  
                    if a not in resultado:  #if para procurar/evitar repetidos            
                        resultado.append(a) 
            print("\nDiferença: conjunto 1 {",(','.join(matrizFormatada[i+1])),"}, conjunto 2 {",(','.join(matrizFormatada[i+2])),"}, resultado {",(','.join(resultado)),"}\n")
            resultado.clear()
        else: #verificar se a operação é Produto Cartesiano
            for m in range(len(matrizFormatada[i+1])):
                for n in range(len(matrizFormatada[i+2])): #for para fazer a junção de a e b
                    c = matrizFormatada[i+1][m],matrizFormatada[i+2][n]
                    d = (','.join(c))
                    resultado.append(d) #adicionando ao vetor
            print("\nProduto Cartesiano: conjunto 1 {",(','.join(matrizFormatada[i+1])),"}, conjunto 2 {",(','.join(matrizFormatada[i+2] )),"}, resultado {(",') , ('.join(resultado),")}\n")
            resultado.clear()
