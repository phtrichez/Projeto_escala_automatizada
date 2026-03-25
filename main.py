from src.scheduler import Scheduler

INPUT_ESCALA = "data/input/Escala_gvc_red.csv"
INPUT_QTD = "data/input/QTD_ESCALA_DIA.csv"
OUTPUT = "data/output/escala_final.csv"


def main():
    scheduler = Scheduler(INPUT_ESCALA, INPUT_QTD)
    resultado = scheduler.run()
    scheduler.save(OUTPUT)

    print("✅ Escala gerada com sucesso!")


if __name__ == "__main__":
    main()