# Escala Automática GVC

Sistema de geração automática de escala com:

## ✅ Features

- Distribuição equilibrada de carga
- Balanceamento por tipo (NC, CM, CV)
- Restrições por dia:
  - Não pode trabalhar (R)
  - Só CM
  - Só CV
- Fallback automático quando falta pessoas

---

## 📊 Lógica

- Prioriza quem tem menor carga (score)
- NC prioriza quem tem menos NC
- Aleatoriedade controlada em empates

---

## 📂 Estrutura

- `scheduler.py` → motor principal
- `restrictions.py` → regras de restrição
- `models.py` → entidade Pessoa

---

## 🚀 Como rodar

```bash
pip install -r requirements.txt
python main.py