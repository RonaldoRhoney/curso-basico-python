faturamento = 1200 # tipo -> int (número inteiro)
custo = 750.0 #tipo -> float (número decimal)

novas_vendas = 100
faturamento = faturamento + novas_vendas

imposto  = faturamento * 0.1

lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento

print("Faturamento foi de ", faturamento)
print("O custo foi de ", custo)
print("O lucro foi de ", lucro)
print("A margem de lucro foi de",  round(margem_lucro, 2))


mensagem = "O faturamento da loja foe de tanto" #
email = "ronaldorhoney6910@gmail.com" # string -> texto

teve_lucro = True #tipo -> boolean