from src.scheduler import Scheduler

INPUT_ESCALA = "data/input/Escala_gvc_red_1.csv"
INPUT_QTD = "data/input/QTD_ESCALA_DIA.csv"
df_INPUT = "data/input/dados_completo_escala.xlsx"
OUTPUT = "data/output/escala_final.xlsx"


def main():
    scheduler = Scheduler(df_INPUT)
    resultado = scheduler.run()
    scheduler.save(OUTPUT)

    print("✅ Escala gerada com sucesso!")


if __name__ == "__main__":
    main()