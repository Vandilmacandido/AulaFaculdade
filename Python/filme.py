filmes = ["Filme1" , "Filme 2" , "Filme 3" , "Filme4" , "Filme 5"]

print(" Bem-Vindo a cçassificação de filme.")
print("Você tem 5 filmes para classificar")
print("digite 0 a qualquer momento para parar.")
print("Aqui estão os filmes:")

for filme in filmes:
    classificacao = input ("como você classificaria o '{filme}' de 1 a 5? (ou 0 para parar: )")
    if classificacao == "0":     