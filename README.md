# MC714 - Sistemas Distribuidos - Trabalho 2

### Grupo:

Daniel Yuji Hosomi &nbsp; - 248255

Lucas Francisco Silva Paiva &nbsp; - 248390

# Sobre o Projeto

## Introdução

**Descrição do Problema:**
O problema abordado neste projeto envolve a implementação de algoritmos distribuídos que são essenciais para a coordenação e sincronização em sistemas distribuídos. Especificamente, foram implementados três algoritmos: o Relógio Lógico de Lamport, Token Ring e Leader Election.

**Objetivos do Projeto:**
O principal objetivo do projeto é desenvolver uma solução que implemente eficientemente os algoritmos mencionados acima, utilizando técnicas de comunicação em sistemas distribuídos. O projeto visa demonstrar a aplicação prática desses algoritmos e validar seu funcionamento através de testes e experimentos.

---

## Algoritmos Escolhidos

**Relógio Lógico de Lamport:**
Este algoritmo é utilizado para ordenar eventos em sistemas distribuídos onde não existe um relógio global. Ele garante que se um evento A causou um evento B, então A será ordenado antes de B. Isso garante sincronização entre diferentes máquinas e processos durante o envio de mensagens.

**Token Ring:**
A exclusão mútua é necessária para evitar conflitos de acesso concorrente a recursos compartilhados. Implementamos o algoritmo token ring de exclusão mútua para garantir que apenas um processo possa acessar o recurso crítico por vez. Nesse algoritmo cada processo possuí uma variável informando 

**Bully Algorithm for Leader Election:**
A eleição de líder é crucial em sistemas distribuídos para coordenar ações e tomar decisões. Implementamos o algoritmo bully de eleição de líder que escolhe um líder entre os processos distribuídos, que será responsável por coordenar as operações. O líder escolhido é a partir da prioridade dos processos e dos computadores, que é definida quando subimos eles nas redes distribuídas.

---

## Detalhes da Implementação

**Bibliotecas Utilizadas:**
- Python: Utilizado como linguagem de programação principal.
- Paho-MQTT: Biblioteca utilizada para conexão e comunicação em redes de computadores.
- Docker: Para virtualização e simulação de várias máquinas em contribuição.


**Sistemas de Comunicação:**
Utilizamos comunicação baseada em troca de mensagens pelo paho-mqtt usando o broker message mosquitto para garantir a entrega confiável de mensagens entre os processos.

**Ambiente de Execução:**
O código foi executado em um ambiente de contêineres Docker para simular um sistema distribuído. Cada contêiner representa um nó no sistema distribuído.

**Descrição dos Arquivos de Código:**

- **device.py:**
  Este arquivo contém a definição da classe `Device`, que representa um nó no sistema distribuído. Ele inclui métodos para inicializar o dispositivo, enviar e receber mensagens, e processar eventos de acordo com o Relógio Lógico de Lamport.

- **message.py:**
  Define a estrutura das mensagens trocadas entre os dispositivos. Cada mensagem inclui informações como data, timestamp, remetente, e destinatário.

- **util.py:**
  Contém constantes utilitárias para suporte à comunicação e manipulação de mensagens.

---

## Testes Realizados

**Estratégia de Testes:**
Os testes foram realizados em um ambiente simulado utilizando múltiplos contêineres Docker. Cada contêiner executa uma instância do código do dispositivo, permitindo a comunicação entre os nós e a validação dos algoritmos. Todos os algoritmos são executados de maneira simultânea.

**Resultados dos Testes:**
Os algoritmos foram validados com sucesso através de uma série de testes. Cada algoritmo demonstrou o comportamento esperado:
- O Relógio Lógico de Lamport ordenou corretamente os eventos distribuídos.
- O algoritmo token ring de exclusão mútua garantiu acesso exclusivo ao recurso crítico.
- O algoritmo bully de eleição de líder selecionou corretamente um líder entre os nós distribuídos.

---

## Resultados de Experimentos

**Descrição dos Experimentos:**
Foram realizados experimentos para validar o comportamento dos algoritmos em diferentes cenários de carga e falhas. Testamos o sistema com diferentes números de nós e simulamos falhas de comunicação para avaliar a robustez dos algoritmos.

**Análise dos Resultados:**
Os resultados mostraram que os algoritmos são eficientes e robustos, mantendo a correção e a consistência do sistema mesmo em condições adversas. O Relógio Lógico de Lamport conseguiu ordenar corretamente eventos mesmo com alta concorrência. O algoritmo de exclusão mútua manteve a exclusividade do acesso ao recurso, e o algoritmo de eleição de líder conseguiu eleger um líder mesmo após falhas de comunicação.

---

## Comentários sobre a Experiência

**Dificuldades Enfrentadas:**
As principais dificuldades incluíram a configuração do ambiente de contêineres e a garantia de sincronização precisa entre os nós distribuídos. Além disso, a depuração de problemas de comunicação entre contêineres foi desafiadora.

**O que Poderia Ser Melhorado:**
A implementação poderia ser melhorada utilizando bibliotecas de comunicação mais avançadas, como gRPC, para simplificar a comunicação entre os nós. Além disso, a automação dos testes e a criação de um sistema de monitoramento para os nós distribuídos seriam benéficas.

**Aprendizados:**
Este projeto proporcionou uma compreensão profunda dos desafios e técnicas envolvidas na implementação de algoritmos distribuídos. Aprendemos sobre a importância da sincronização de tempo, a coordenação de processos e a tolerância a falhas em sistemas distribuídos. Além de aprender bastante sobre comunicação entre computadores e redes de computadores.

# Execução do Repositório 
Para a execuação e simulação do código em sua máquina é necessário possuir o Python na versão 3.7 ou acima e o Docker Desktop e rodar os seguintes comandos:

- docker build . -t "mc714-t2"
- docker compose up

# Vídeo do Projeto

[Link para o vídeo](https://drive.google.com/file/d/1Zofsu3KMBOMkX1eiI4DUZxyOu8TZybfB/view?usp=sharing)

# Referências

 - [Lamport Clock](https://www.geeksforgeeks.org/lamports-logical-clock/)

 - [Mutual Exclusion Algorithm](https://denninginstitute.com/workbenches/token/token.html#:~:text=Token%20Ring%20algorithm%20achieves%20mutual,next%20in%20line%20after%20itself.)

 - [Leader Election Algorithm](https://www.geeksforgeeks.org/bully-algorithm-in-distributed-system/)
