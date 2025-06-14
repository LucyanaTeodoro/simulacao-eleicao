from tabulate import tabulate

candidatos = {1: 'Renan', 2: 'Osmar', 3: 'Lourdes', 4: 'Sara'}
votosRenan = 0
votosOsmar = 0
votosLourdes = 0
votosSara = 0
votosNulo = 0
votosBranco = 0

tabela_candidatos = [["Código", "Candidato"],
                     [1, 'Renan'],
                     [2, 'Osmar'],
                     [3, 'Lourdes'],
                     [4, 'Sara'],
                     [5, 'Voto Nulo'],
                     [6, 'Voto em Branco']]

print(tabulate(tabela_candidatos, headers="firstrow", tablefmt="grid"))

while True:
    try:
        voto = int(input("Digite o código do seu voto (ou 0 para encerrar): "))
        if voto == 0:
            break
        elif voto == 1:
            votosRenan += 1
        elif voto == 2:
            votosOsmar += 1
        elif voto == 3:
            votosLourdes += 1
        elif voto == 4:
            votosSara += 1
        elif voto == 5:
            votosNulo += 1
        elif voto == 6:
            votosBranco += 1
        else:
            print("Voto invalido! Tente novamente.")
    except ValueError:
        print("Voto invalida! Por favor, digite um numero.")

totalVotos = votosRenan + votosOsmar + votosLourdes + votosSara + votosNulo + votosBranco

if totalVotos > 0:
    percNulos = (votosNulo / totalVotos) * 100
    percBrancos = (votosBranco / totalVotos) * 100
else:
    percNulos = percBrancos = 0

votosCandidatos = {
    'Renan': votosRenan,
    'Osmar': votosOsmar,
    'Lourdes': votosLourdes,
    'Sara': votosSara
}
vencedor = max(votosCandidatos, key=votosCandidatos.get)

print("\nResultado da Eleiçao:\n")

print(f"Total de votos para Renan: {votosRenan}")
print(f"Total de votos para Osmar: {votosOsmar}")
print(f"Total de votos para Lourdes: {votosLourdes}")
print(f"Total de votos para Sara: {votosSara}")
print(f"\nTotal de votos nulos: {votosNulo}")
print(f"Total de votos em branco: {votosBranco}")
print(f"Percentagem de votos nulos: {percNulos:.2f}%")
print(f"Percentagem de votos em branco: {percBrancos:.2f}%")

if totalVotos > 0:
    print(f"\nO candidato que ganhou a eleição foi: {vencedor} com {votosCandidatos[vencedor]} votos.")
else:
    print("\nNenhum voto foi registrado.")
