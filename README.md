# Pedra, Papel, Tesoura
## Descrição

Este é um jogo simples de **Pedra, Papel e Tesoura** em que o jogador compete contra o computador. O objetivo é escolher entre Pedra, Papel ou Tesoura e tentar vencer o adversário. O jogo mantém um placar e permite que o jogador continue jogando até decidir sair.

## Funcionalidades

- **Escolha do Jogador**: O jogador escolhe entre Pedra, Papel ou Tesoura.
- **Escolha do Computador**: O computador escolhe aleatoriamente entre Pedra, Papel ou Tesoura.
- **Placar**: O jogo mantém o placar de vitórias do jogador e do adversário.
- **Validação de Entrada**: O jogo valida as escolhas do jogador e garante que apenas as opções válidas sejam aceitas.
- **Reinício ou Saída**: O jogador pode optar por continuar jogando ou sair a qualquer momento.

## Como Jogar

1. **Iniciar o Jogo**: Ao iniciar o jogo, o jogador deve escolher entre Pedra, Papel ou Tesoura digitando o número correspondente:
    - **1** para Pedra
    - **2** para Papel
    - **3** para Tesoura
2. O computador escolhe aleatoriamente uma das opções.
3. O jogo compara as escolhas:
    - Pedra vence Tesoura.
    - Tesoura vence Papel.
    - Papel vence Pedra.
4. O placar é atualizado após cada rodada.
5. O jogador pode continuar jogando ou sair a qualquer momento.

## Como Usar

1. Clone ou baixe o código do repositório.
2. Execute o script Python.
3. Siga as instruções no terminal para jogar.

## Exemplo de Uso

```bash
* Menu *
1- Começar
2- Sair
R: 1

* Placar *
Você: 0
Adversario: 0

* Escolha *
1- Pedra
2- Papel
3- Tesoura
R: 1

Adversario escolheu Tesoura!
Você ganhou!

Digite "1" para voltar
R: 1

* Menu *
1- Começar
2- Sair
R: 2

Programa finalizado!
```

## Requisitos

- Python 3.x
- Biblioteca `random` (incluída no Python por padrão)

## Como Rodar o Código

1. **Clone ou baixe o projeto**:
    ```bash
    git clone <link-do-repositório>
    ```

2. **Execute o script**:
    ```bash
    python pedra_papel_tesoura.py
    ```
