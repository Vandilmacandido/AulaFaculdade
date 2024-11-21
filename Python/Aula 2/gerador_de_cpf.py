import random
import tkinter as tk
from tkinter import messagebox

# Função para calcular o dígito verificador do CPF
def gerar_digito_verificador(digitos):
    soma = 0
    for i, digito in enumerate(digitos):
        soma += digito * (len(digitos) + 1 - i)
    
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

# Função para gerar um CPF
def gerar_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    primeiro_dv = gerar_digito_verificador(cpf)
    cpf.append(primeiro_dv)
    segundo_dv = gerar_digito_verificador(cpf)
    cpf.append(segundo_dv)
    return f"{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}"

# Função para gerar múltiplos CPFs com base no número informado pelo usuário
def gerar_cpfs():
    try:
        quantidade = int(entry_quantidade.get())
        if quantidade <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")
        return
    
    cpfs_gerados = [gerar_cpf() for _ in range(quantidade)]
    resultado_texto = "\n".join(cpfs_gerados)
    texto_resultado.config(state=tk.NORMAL)
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, resultado_texto)
    texto_resultado.config(state=tk.DISABLED)

# Interface gráfica (GUI) usando tkinter
janela = tk.Tk()
janela.title("Gerador de CPF")

# Label de instrução
label_instrucoes = tk.Label(janela, text="Insira a quantidade de CPFs para gerar:")
label_instrucoes.pack(pady=10)

# Caixa de entrada para a quantidade
entry_quantidade = tk.Entry(janela)
entry_quantidade.pack(pady=5)

# Botão para gerar os CPFs
botao_gerar = tk.Button(janela, text="Gerar CPFs", command=gerar_cpfs)
botao_gerar.pack(pady=10)

# Caixa de texto para exibir os CPFs gerados
texto_resultado = tk.Text(janela, height=10, width=40, state=tk.DISABLED)
texto_resultado.pack(pady=10)

# Iniciar a aplicação
janela.mainloop()
