# Alien Escape

Projeto final da disciplina de Introdução a Algoritmos e Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Matheus Henrique Castilho Ricoy Guerra
- Diego Ribeiro Barreira Gil
- Eduardo Henrique Rodrigues Dias
- Lucas Buratto

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação, contém o loop principal e a máquina de estados do jogo.
- `src/`: módulos do jogo, separados por responsabilidade (personagem, aliens, pontuação, cenário, telas e configurações).
- `assets/`: imagens, fontes e sons utilizados no jogo.
- `data/`: arquivos persistentes de recorde.
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo a proposta inicial.

## Descrição do jogo

> Alien Escape é um endless runner em que o jogador controla um militar em uma missão de sobrevivência. Aliens terrestres e OVNIs aparecem como obstáculos, e o jogador deve reagir rapidamente para sobreviver e acumular pontos. Ao atingir uma meta de pontuação sorteada aleatoriamente, uma nave aparece pelo lado direito da tela e o personagem caminha até ela, encerrando o jogo com uma tela de vitória.

## Objetivo do jogador

> Sobreviver desviando dos aliens e OVNIs, acumulando pontuação até atingir a meta sorteada e escapar na nave.

## Regras do jogo

- O militar corre automaticamente pelo cenário.
- Aliens aparecem no chão e devem ser evitados com pulos.
- OVNIs aparecem no céu e devem ser evitados ao se agachar.
- A pontuação aumenta automaticamente com o tempo de sobrevivência.
- A dificuldade aumenta progressivamente conforme a pontuação avança, com quatro níveis distintos.
- A partida termina ao colidir com qualquer obstáculo.
- Ao atingir a meta de pontuação, o jogo entra na cena de vitória.

## Controles

- **Espaço:** pular.
- **Seta para baixo (↓) ou CTRL esquerdo:** agachar.
- **ENTER:** iniciar a partida na tela de início.
- **ENTER:** reiniciar após game over.
- **ENTER:** fechar o jogo na tela de vitória.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.