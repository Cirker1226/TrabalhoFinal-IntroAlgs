# Código-fonte (`src`)

Esta pasta contém todos os módulos do jogo, cada um responsável por uma parte específica do funcionamento.

## Arquivos

- `config.py`: centraliza todas as constantes do projeto, como dimensões da tela, velocidades, tamanhos dos personagens, configurações de física, cores e pontuação.
- `cenario.py`: controla o fundo infinito do jogo, atualizando e desenhando o loop de movimento do cenário.
- `personagem.py`: gerencia o personagem principal, incluindo carregamento dos sprites, animações de corrida e agachamento, física de pulo com gravidade, hitbox e movimentação na cena de vitória.
- `alien.py`: controla o spawn, movimentação, animação e remoção dos obstáculos, incluindo aliens terrestres de diferentes tamanhos e OVNIs. Também gerencia a detecção de colisão com o personagem e o aumento progressivo de dificuldade.
- `pontos.py`: gerencia a pontuação em tempo real, o recorde persistido em arquivo local, os quatro níveis de dificuldade progressiva e a renderização dos textos de pontuação na tela.
- `telas.py`: renderiza as telas de início, game over e vitória, além de controlar a animação de entrada da nave na cena final.

## Dica de evolução

Quando o projeto crescer, mantenha módulos pequenos e separados por responsabilidade.
