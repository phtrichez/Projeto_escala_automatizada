# Escala Automática GVC

Sistema de geração automática de escala com:

## ✅ Features

- Distribuição equilibrada entre GVC
- Balanceamento por tipo (NC, CM, CV)
- Restrições por dia:
  - Não pode trabalhar (R)
  - Só CM
  - Só CV
- Fallback automático quando falta pessoas

---

## 📊 Lógica

1. Quem trabalhou menos (quantidade total)
2. Equilíbrio entre quantidade trabalhada em NC e CM/CV
3. Aleatoriedade (desempate) pode ser mudado para a nota

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
