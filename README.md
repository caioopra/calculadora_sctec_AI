# Exemplo Git

Repositório de exemplo para aulas de Git e workflows com agentes de IA. Implementa uma calculadora simples em Python.

## Operações disponíveis

- `somar(a, b)`
- `subtrair(a, b)`
- `multiplicar(a, b)`
- `dividir(a, b)` — lança `ValueError` ao dividir por zero
- `potencia(base, expoente)`
- `fatorial(n)` — lança `ValueError` para número negativo
- `media(numeros)` — calcula a média de uma lista e lança `ValueError` se ela estiver vazia

## Como executar

```bash
uv run python main.py
```

## Como rodar os testes

```bash
uv run python -m pytest
```
