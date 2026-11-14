print("Sistema Cinema UVA")
idade = int(input("Insira a sua idade: "))
# Pede para o usuário digitar a idade

if (idade<18): #Condicional, apenas se esta condição for satisfeita, o código indentado abaixo será executado
    print("Tem direito a meia entrada.")
else: #Caso a condição acima não seja cumprida, o código abaixo será executado
    print("Não tem direito a meia entrada.")

print("Sistema finalizado.") #Esta parte do código já não está dentro do if e será executada independentemente das condições anteriores.