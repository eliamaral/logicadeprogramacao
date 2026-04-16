def contar_caminhos(num_pedras):
    if num_pedras <= 1:
        return 1
    return contar_caminhos(num_pedras - 1) + contar_caminhos(num_pedras - 2)

print(contar_caminhos(6))