import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Função para calcular o dígito verificador do CPF
def gerar_digito_verificador(digitos):
    soma = 0
    for i, digito in enumerate(digitos):
        soma += digito * (len(digitos) + 1 - i)
    
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

# Função para gerar um CPF baseado na hora atual
def gerar_cpf(index):
    # Pegar a hora atual como base para os 9 primeiros dígitos, incluindo um índice extra para variar
    hora_atual = datetime.now()
    hora_formatada = hora_atual.strftime('%H%M%S%f')  # Hora, minuto, segundo e microsegundo

    # Usar os primeiros 9 números da hora + índice para variar a geração
    cpf = [int(hora_formatada[i % len(hora_formatada)]) for i in range(9)]
    
    # Ajustar o CPF para variar mais, somando o índice em um dos dígitos
    cpf[8] = (cpf[8] + index) % 10

    # Gerar o primeiro dígito verificador
    primeiro_dv = gerar_digito_verificador(cpf)
    cpf.append(primeiro_dv)

    # Gerar o segundo dígito verificador
    segundo_dv = gerar_digito_verificador(cpf)
    cpf.append(segundo_dv)

    # Formatar o CPF como XXX.XXX.XXX-XX
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
    
    # Gerar a quantidade desejada de CPFs
    cpfs_gerados = [gerar_cpf(i) for i in range(quantidade)]
    
    # Exibir os CPFs gerados no campo de texto
    resultado_texto = "\n".join(cpfs_gerados)
    texto_resultado.config(state=tk.NORMAL)
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, resultado_texto)
    texto_resultado.config(state=tk.DISABLED)

# Interface gráfica (GUI) usando tkinter
janela = tk.Tk()
janela.title("Gerador de CPF sem random")

# Label de instrução
label_instrucoes = tk.Label(janela, text="Insira a quantidade de CPFs para gerar:")
label_instrucoes.pack(pady=10)

# Caixa de entrada para a quantidade
entry_quantidade = tk.Entry(janela)
entry_quantidade.pack(pady=5)

# Botão para gerar os CPFs
botao_gerar = tk.Button(janela, text="Gerar CPF", command=gerar_cpfs)
botao_gerar.pack(pady=10)

# Caixa de texto para exibir os CPFs gerados
texto_resultado = tk.Text(janela, height=10, width=40, state=tk.DISABLED)
texto_resultado.pack(pady=10)

# Iniciar a aplicação
janela.mainloop()
