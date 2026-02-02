import pandas as pd

def main():
    print("Projeto de Análise Logística Iniciado")

    dados = {
        "Entrega": [1, 2, 3, 4],
        "Atraso_dias": [0, 1, 3, 0],
        "Custo": [120, 200, 150, 180]
    }

    df = pd.DataFrame(dados)

    print("\nDados das entregas:")
    print(df)

    media_atraso = df["Atraso_dias"].mean()
    custo_medio = df["Custo"].mean()

    print("\nMédia de atraso:", media_atraso)
    print("Custo médio:", custo_medio)


if __name__ == "__main__":
    main()
