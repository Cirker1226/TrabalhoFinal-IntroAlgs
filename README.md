# Alien Escape

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Matheus Henrique
- Diego Ribeiro
- Eduardo Dias

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

> Alien Escape é um jogo do gênero runner infinito em que o jogador controla um militar em uma missão de sobrevivência. Durante o percurso, aliens terrestres e OVNIs aparecem como obstáculos, e o jogador deve reagir rapidamente para sobreviver e acumular pontos.

## Objetivo do jogador

> O objetivo é sobreviver o maior tempo possível, evitando colisões com os aliens que surgem no solo e com os OVNIs que voam pelo céu, alcançando a maior pontuação possível.

## Regras do jogo

- O militar corre automaticamente pelo cenário.
- Aliens aparecem no chão como obstáculos terrestres.
- OVNIs aparecem no céu como obstáculos aéreos.
- O jogador deve pular ou agachar para evitar colisões.
- A pontuação aumenta conforme o tempo de sobrevivência.
- A velocidade do jogo aumenta gradativamente.
- A partida termina quando ocorre uma colisão com um alien ou OVNI.

## Controles

- **Espaço:** pular.
- **Seta para baixo (↓):** agachar.
- **ENTER:** reiniciar a partida.

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