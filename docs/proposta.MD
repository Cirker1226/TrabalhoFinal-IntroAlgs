# Proposta Inicial do Jogo

Este documento foi preenchido pelo grupo na Semana 1 do projeto.

## 1. Nome provisório do jogo

> Alien Escape

## 2. Integrantes do grupo

- Matheus Henrique Castilho Ricoy Guerra
- Diego Ribeiro Barreira Gil
- Eduardo Henrique Rodrigues Dias
- Lucas Buratto

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> Jogo de sobrevivência e desvio de obstáculos (endless runner).

## 4. Descrição geral do jogo

Descrição:

> O jogador controla um militar que corre automaticamente por um cenário de fundo infinito. Durante a partida, aliens aparecem no chão e OVNIs aparecem no céu. O jogador deve pular ou agachar para evitar os obstáculos e sobreviver o maior tempo possível. A dificuldade aumenta gradativamente conforme a pontuação avança. Ao atingir uma pontuação sorteada aleatoriamente, uma nave aparece pelo lado direito da tela e o personagem caminha até ela, encerrando o jogo com uma tela de vitória.

## 5. Objetivo do jogador

Objetivo:

> Sobreviver desviando dos aliens e OVNIs, acumulando pontuação até alcançar a meta sorteada e escapar na nave.

## 6. Regras principais

Regras do grupo:

- O militar corre automaticamente durante toda a partida.
- Aliens aparecem no chão e devem ser evitados com pulos.
- OVNIs aparecem no céu e devem ser evitados ao se agachar.
- A pontuação aumenta automaticamente com o tempo de sobrevivência.
- A dificuldade aumenta conforme a pontuação aumenta.
- A partida termina ao colidir com qualquer obstáculo.
- Ao atingir a pontuação de vitoria(aleatoria), o jogo entra na cena de vitória.

## 7. Condição de vitória

Condição de vitória:

> O jogador vence ao atingir a pontuação sorteada aleatoriamente entre 500 e 800 pontos. Uma nave aparece pelo lado direito da tela e o personagem caminha automaticamente até ela. Ao chegar, a tela de vitória é exibida com a pontuação final e o recorde.

## 8. Condição de derrota ou encerramento

Condição de derrota ou encerramento:

> O jogo termina quando o jogador colide com um alien ou um OVNI, exibindo a tela de game over com a pontuação atual e o recorde salvo.

## 9. Elementos previstos no jogo

### Jogador ou elemento principal

Descrição:

> Um militar feito por sprite sheets, capaz de pular e agachar para evitar obstáculos. Possui animações distintas para corrida e agachamento, além de hitbox ajustável para colisão precisa.

### Obstáculos, inimigos ou desafios

Descrição:

> Aliens terrestres de diferentes tamanhos que aparecem no chão, e OVNIs que aparecem voando pelo céu. Cada tipo possui sprites e hitbox própria. A velocidade e o intervalo de spawn aumentam conforme a dificuldade.

### Itens, alvos ou objetos de interação

Descrição:

> Não há itens coletáveis. O foco é a sobrevivência e a pontuação baseada no tempo. A nave que aparece na cena final é o único elemento de interação não obstáculo.

### Pontuação, vidas, tempo ou progresso

Descrição:

> A pontuação aumenta automaticamente com o tempo de sobrevivência. O jogador possui apenas uma vida. O recorde é salvo em arquivo local e exibido tanto durante a partida quanto nas telas de game over e vitória. A dificuldade possui quatro níveis progressivos baseados na pontuação atual.

## 10. Controles previstos

Controles do grupo:

- Espaço: pular.
- Seta para baixo (↓) e o CTRL esquerdo: agachar.
- ENTER: iniciar a partida na tela de início.
- ENTER: reiniciar após game over.
- ENTER: fechar o jogo na tela de vitória.

## 11. Organização inicial do código

Organização planejada:

- `main.py`: loop principal e máquina de estados do jogo.
- `src/personagem.py`: controle, animação e física do militar.
- `src/alien.py`: spawn, movimentação e animação dos obstáculos.
- `src/pontos.py`: sistema de pontuação, recorde e dificuldade.
- `src/telas.py`: renderização das telas de início, game over e vitória.
- `src/cenario.py`: movimentação do fundo infinito.
- `src/config.py`: constantes e configurações gerais do jogo.
- `data/`: pasta com arquivos de persistência do recorde.
- `assets/`: pasta com imagens, fontes e sons do jogo.

## 12. Recursos externos previstos

Recursos previstos:

- Spritesheet do personagem militar com animações de corrida e agachamento.
- Sprites animados para aliens terrestres e OVNIs.
- Imagem de fundo do cenário em loop infinito.
- Fonte tipográfica customizada Eight-Bit Madness para os textos do jogo.
- Imagens de logo, vitória e nave para as telas especiais.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Implementação da colisão entre o jogador e os obstáculos com hitbox ajustável.
- Controle da física de pulo com gravidade e força configuráveis.
- Aumento da dificuldade com ajuste de velocidade e intervalo de spawn.
- Sincronização da cena da nave com a movimentação do personagem.

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo possui um militar com animações de corrida e agachamento, aliens e OVNIs surgindo como obstáculos com dificuldade progressiva, sistema de pontuação com recorde persistido, detecção de colisões com hitbox, telas de início, game over e vitória, e cena final com a nave.

## 15. Melhorias implementadas

Melhorias realizadas:

- Sistema de recorde salvo em arquivo local.
- Animações para o personagem e todos os obstáculos via sprite sheet.
- Tela de início com logo e tela de vitória com imagem customizada.
- Quatro níveis de dificuldade progressiva.
- Cena de vitória com nave entrando pela direita e personagem caminhando até ela.
- Meta de pontuação sorteada aleatoriamente a cada partida.
- Hitbox ajustável para colisão mais precisa e justa.