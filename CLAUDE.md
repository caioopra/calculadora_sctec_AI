# exemplo_git

Repositório didático de uma calculadora simples em Python, usado em aulas do SENAI para demonstrar comandos de Git e workflows com agentes de IA.

## Stack

- Python 3 (stdlib)
- pytest para testes

## Estrutura

- `src/calculadora.py` — funções da calculadora
- `main.py` — entrypoint de demonstração
- `tests/test_calculadora.py` — suíte de testes
- `pyproject.toml` — configuração do pytest

## Comandos

```bash
python main.py            # executa a demo
python -m pytest          # roda os testes
python -m pytest -v       # roda os testes em modo verboso
```

## Convenções

- **Idioma**: nomes de funções, mensagens de commit e comentários em português.
- **Commits**: Conventional Commits (`feat:`, `fix:`, `test:`, `docs:`, `chore:`, `refactor:`). Mensagem curta, no imperativo, em minúsculas após o prefixo.
- **Branches**: `feature/<nome-curto>` para novas funcionalidades, `fix/<nome>` para correções.
- **Estilo**: Python idiomático e direto. Sem abstrações desnecessárias — o código é projetado em tela durante a aula, então clareza > engenharia.

## Workflow esperado para uma nova feature

Quando o usuário pedir uma feature nova, siga esta sequência:

1. Criar branch a partir de `main`: `git checkout -b feature/<nome>`
2. Implementar a função em `src/calculadora.py` e expor em `main.py` se fizer sentido
3. Adicionar testes em `tests/test_calculadora.py` cobrindo o caminho feliz e ao menos uma edge case
4. Rodar `python -m pytest` e garantir 100% verde antes de comitar
5. Commit semântico (ex.: `feat: adiciona <operação> à calculadora`)
6. Abrir PR com `gh pr create` (título = mensagem do commit; corpo descreve o que mudou e como testar)
7. Aguardar revisão antes de fazer merge

## Diretrizes para o agente

- **Não comite mudanças sem ser pedido explicitamente.** Se o usuário pedir "gere uma mensagem de commit" ou "sugira um commit", devolva apenas o texto da mensagem — não execute `git commit`.
- Sempre rode os testes depois de mexer em `src/` ou `tests/` e reporte o resultado antes de pedir merge.
- Mantenha as alterações mínimas e focadas no escopo do pedido — nada de refactor oportunista.
