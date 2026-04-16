produto = "Arroz"
preco_unitario = 5.79
quantidade = 3

valor_total = preco_unitario * quantidade

if quantidade > 2:
    valor_total = valor_total * 0.9

print("Produto: ", produto)
print("Quantidade: ", quantidade)
print(f"Valor total da compra: R${valor_total:.2f}")