gols_time1 = int(input("foram quantos gols do time A: "))
gols_time2 = int(input("foram quantos gols do time B: "))

if gols_time1 == gols_time2:
    print("Empate")
elif gols_time1 > gols_time2:
    print("Time A venceu")
else:
    print("Time B venceu")