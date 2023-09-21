def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (1922-2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("O ano deve estar entre 1922 e 2021.")
        except ValueError:
            print("Por favor, digite um número válido.")

def calcular_idade(ano_nascimento):
    ano_atual = 2022
    idade = ano_atual - ano_nascimento
    return idade

def main():
    nome_completo = input("Digite seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()

    idade = calcular_idade(ano_nascimento)

    print(f"\nNome: {nome_completo}")
    print(f"Idade em 2022: {idade} anos")

if __name__ == "__main__":
    main()
