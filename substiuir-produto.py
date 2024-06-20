material_escolar = ["lápis", "borracha", "caneta", "cola", "tesoura"]

def substitui_produto(antigo_produto, novo_produto):
    for i in range(len(material_escolar)):
        if material_escolar[i] == antigo_produto:
          material_escolar[i] = novo_produto