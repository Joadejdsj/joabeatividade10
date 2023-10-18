# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
km = float(input("Digite a velocidade do veicúlo em Km/h: "))
vel = 60
multa = (km-60)*7
if vel > int("60"):
    print("Sua velocidade esta dentro do padrão estabelecido, por favor pode prosseguir com sua viagem.")
else:
    print(f"Sua velocidade excedeu o limite de 60 Km/h, você deverá pagar multa de: R${multa} ")