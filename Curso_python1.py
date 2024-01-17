faturamento = 1200 #Número inteiro
custo = 700

taxa_imposto = 0.1 #--> Número decimal: Float
mensagem = "O faturamento foi de "
teve_lucro = False #Boolean

novas_vendas = 300
faturamento = faturamento + novas_vendas

imposto = taxa_imposto * faturamento

print("Faturamento", faturamento)
print("Custo",custo)
print("Lucro", faturamento - custo - imposto)
print(mensagem, faturamento)