

![O Diagrama de Clase](https://upload.wikimedia.org/wikipedia/commons/6/61/Logo_UniFil.png)

# CURSO DE BACHARELADO EM ENGENHARIA DE SOFTWARE

## GABRIEL ZANONI HERCULANO  
## MARIO HENRIQUE AKIHIKO DA COSTA

# INTEGRAÇÃO CLASSROOM DISCORD

**Londrina**  
**2024**

---

## SUMÁRIO

1. [INTRODUÇÃO](#1-introdução)
   1.1 [PROPOSTA E OBJETIVOS](#11-proposta-e-objetivos)  
   1.2 [JUSTIFICATIVA](#12-justificativa)
2. [DIAGRAMA DE CASO DE USO](#2-diagrama-de-caso-de-uso)
3. [DIAGRAMA DE CLASSE](#3-diagrama-de-classe)
4. [WORKFLOW (AS IS) NA NOTAÇÃO BPMN](#4-workflow-as-is-na-notação-bpmn)
5. [DIAGRAMA DE ENTIDADE RELACIONAMENTO](#5-diagrama-de-entidade-relacionamento)
6. [DIAGRAMA DE SEQUÊNCIA](#6-diagrama-de-sequência)
7. [DIAGRAMA DE IMPLANTAÇÃO](#7-diagrama-de-implantação)
8. [ESPECIFICAÇÃO DO CASO DE USO](#8-especificação-do-caso-de-uso)
9. [ESPECIFICAÇÃO SUPLEMENTAR](#9-especificação-suplementar)
10. [DOCUMENTO DE VISÃO](#10-documento-de-visão)
11. [PEDIDO DO INVESTIDOR](#11-pedido-do-investidor)
12. [RECURSOS E AMBIENTE DE DESENVOLVIMENTO](#12-recursos-e-ambiente-de-desenvolvimento)  
   12.1 [Linguagem de Programação](#121-linguagem-de-programação)
13. [CRONOGRAMA](#13-cronograma)
14. [GLOSSÁRIO](#14-glossário)
15. [REFERÊNCIAS](#15-referências)

---

## 1. INTRODUÇÃO

Ao se deparar com os desafios contemporâneos da educação mediada por tecnologias digitais, surge a necessidade de explorar soluções inovadoras para promover uma experiência de aprendizagem mais eficiente e acessível. Nesse contexto, a proposta de desenvolvimento do estágio supervisionado se apresenta como uma resposta às demandas emergentes dos estudantes e educadores.

A trajetória que conduziu à concepção deste projeto teve como ponto de partida a observação da crescente utilização do Discord entre os estudantes como uma plataforma de comunicação e colaboração. Diante dessa realidade, surgiu a reflexão sobre como essa ferramenta poderia ser aproveitada de forma mais abrangente no contexto educacional, visando aprimorar a interação dos alunos com os recursos acadêmicos.

A partir dessa análise, é possível entender uma oportunidade de integrar o Discord com o Google Classroom, uma plataforma amplamente adotada pelas instituições, utilizada no gerenciamento de diversos cursos e atividades acadêmicas. O Classroom oferece uma ampla variedade de ferramentas para se trabalhar, tanto para os professores quanto para os alunos.

A proposta de desenvolver um Bot para Discord, capaz de oferecer funcionalidades similares às do Google Classroom, mas dentro do ambiente familiar e amigável do Discord, surgiu como uma maneira de potencializar o uso dessa ferramenta e proporcionar uma experiência mais integrada aos estudantes.

Ao continuar o projeto, tenho estes planos em mente, fornecendo uma análise detalhada do processo de desenvolvimento do Bot para Discord integrado ao Google Classroom, desde a sua concepção até a implementação e testes práticos.

Serão abordadas as etapas de pesquisa, planejamento, desenvolvimento de código, integração de APIs, além de considerações sobre usabilidade, eficiência e impacto esperado na experiência educacional dos usuários. O objetivo final é apresentar uma solução inovadora e adaptada às demandas atuais do ensino digital, contribuindo para uma aprendizagem mais dinâmica, colaborativa e acessível.

### 1.1 PROPOSTA E OBJETIVOS

**Objetivo Geral:**

- Desenvolver um Bot para a plataforma Discord integrado ao Google Classroom, proporcionando aos alunos uma experiência mais integrada e acessível no gerenciamento de suas atividades acadêmicas com as funcionalidades presentes no Google Classroom.

**Objetivos Específicos:**

1. Integrar o Bot ao Google Classroom, permitindo o acesso e a visualização das tarefas, notificações de turma, materiais e calendários diretamente no Discord.
2. Implementar funcionalidades de ligamento e autenticação de usuários no Bot para Discord para o Classroom, garantindo a segurança e a privacidade das informações dos alunos.
3. Desenvolver recursos de notificação e lembretes automatizados no Bot, para manter os alunos informados sobre prazos, eventos e atualizações relevantes.
4. Criar um sistema intuitivo e fácil de modificar para uma melhor utilidade dos alunos, providenciando suporte para todas as faixas etárias, mas com foco no público geral.
5. Avaliar o impacto do Bot no engajamento dos alunos e na gestão acadêmica das instituições de ensino, por meio de métricas de utilização, satisfação e desempenho.

### 1.2 JUSTIFICATIVA

A proposta do sistema é desenvolver um Bot para a plataforma Discord integrado ao Google Classroom, oferecendo aos alunos da UniFil uma ferramenta prática e eficiente para gerenciamento de suas atividades acadêmicas. O sistema permitirá aos estudantes acessar e acompanhar suas tarefas, notificações de turma, materiais de estudo, pendências e calendários diretamente no ambiente familiar do Discord.

Essa proposta se justifica como válida e importante para a UniFil por diversos motivos:

- **Facilidade de acesso:** O Discord é uma ferramenta amplamente utilizada pelos estudantes, tornando-se uma escolha natural para disponibilizar os recursos do Google Classroom. Isso facilita o acesso e a utilização por parte dos alunos, reduzindo possíveis barreiras de uso.
- **Melhoria na comunicação:** O Bot desenvolvido possibilitará a automatização de notificações e lembretes, garantindo que os alunos estejam sempre atualizados sobre suas obrigações acadêmicas. Isso contribuirá para uma comunicação mais eficaz entre os estudantes e a instituição.
- **Acompanhamento do engajamento:** A integração entre o Discord e o Google Classroom permitirá o rastreamento do engajamento dos alunos nas atividades acadêmicas, fornecendo insights valiosos para ajustes e melhorias no processo educacional.

Dessa forma, a proposta do sistema não apenas atende às necessidades dos alunos em termos de praticidade e acessibilidade, mas também contribui para uma gestão mais eficiente e eficaz por parte da UniFil, promovendo uma experiência acadêmica mais integrada e satisfatória para todos os envolvidos.

---

## 2. DIAGRAMA DE CASO DE USO

Na UML, os diagramas de caso de uso modelam o comportamento de um sistema e ajudam a capturar os requisitos do sistema. Segue abaixo o Diagrama de Caso de Uso do projeto:

![O Diagrama de Caso de Uso Atualizado](https://i.imgur.com/b1B9MXq.png)
---

## 3. DIAGRAMA DE CLASSE

O diagrama de classe é uma representação da estrutura e relações das classes que servem de modelo para objetos. A seguir, apresentamos o Diagrama de Classe do projeto:

![O Diagrama de Clase](https://i.imgur.com/fICzfTd.png)
---

## 4. WORKFLOW (AS IS) NA NOTAÇÃO BPMN

AS-IS é a visão dos processos atuais de uma organização, que mostra como uma empresa realiza suas atividades em um determinado momento. Segue na Figura abaixo o diagrama de workflow AS-IS:

![AS-IS](https://i.imgur.com/9qVxWZm.png)
---

## 5. DIAGRAMA DE ENTIDADE RELACIONAMENTO

O Diagrama de Entidade e Relacionamento (DER) auxilia na identificação das relações entre os elementos de seu banco de dados e como a informação flui através de seu sistema ou processo empresarial. A seguir, apresentamos o Diagrama de Entidade Relacionamento:

![Conc](https://i.imgur.com/GMI4wYI.png)
![Logic](https://i.imgur.com/6SEwTM7.png)


---

## 6. DIAGRAMA DE SEQUÊNCIA

O Diagrama de Sequência é um diagrama usado em UML que representa a sequência de processos num programa de computador. Segue abaixo o Diagrama de Sequência do projeto:

![DER](https://i.imgur.com/MZbVbSL.png)

---

## 7. DIAGRAMA DE IMPLANTAÇÃO

O Diagrama de Implantação demonstra a execução da arquitetura de um sistema. A seguir, apresentamos o Diagrama de Implantação:

![Deployment](https://i.imgur.com/dor1N8o.png)

---

## 8. ESPECIFICAÇÃO DO CASO DE USO

A Especificação do Caso de Uso elabora um caso de uso específico em um conjunto, detalhando sua função, requisitos e importância. Segue abaixo a Especificação do Caso de Uso:

[Especificação do Caso de Uso: Realizar Comando](uc_spec/rup_ucspec_realizar_comando.md)

---

## 9. ESPECIFICAÇÃO SUPLEMENTAR

A Especificação Suplementar captura os requisitos de sistema que não são capturados imediatamente nos Casos de Uso do Modelo de Casos de Uso. Entre os requisitos estão incluídos: Requisitos legais e reguladores, incluindo padrões de aplicativo.

[Especificação Suplementar](rup_ssspec.md)

---

## 10. DOCUMENTO DE VISÃO

O Documento de Visão fornece uma visão geral do produto a ser desenvolvido, incluindo o escopo, as funcionalidades principais e os objetivos do projeto. Segue abaixo o Documento de Visão:

[Documento de Visão](visao.md)

---

## 11. PEDIDO DO INVESTIDOR

O Pedido do Investidor reúne as solicitações e expectativas do investidor ou cliente em relação ao projeto. Segue abaixo o Pedido do Investidor:

[Pedido do Investidor](rup_stkreq.md)

---

## 12. RECURSOS E AMBIENTE DE DESENVOLVIMENTO

### 12.1 Linguagem de Programação

A linguagem de programação que será utilizada é o Python 3.12.2. Para saber mais sobre as linguagens acesse [Documentação do Python](https://docs.python.org/pt-br/3/tutorial/).

---

## 13. CRONOGRAMA

O cronograma detalha as etapas e prazos do projeto, garantindo que todas as atividades sejam concluídas dentro do tempo previsto. Segue abaixo o cronograma do projeto:

![Cronograma](cronograma.png)

---

## 14. GLOSSÁRIO

O Glossário fornece uma lista de termos e definições relevantes para o projeto, ajudando a esclarecer conceitos importantes. Segue abaixo o Glossário:

[Glossário](rup_gloss.md)

---

## 15. REFERÊNCIAS

- DISCORD. Discord. 2024. <https://discord.com/>. Acesso em: 21 mar. 2024.
- EUAX. EUAX WorkFlow AS-IS TO-BE. 2024. <https://www.euax.com.br/2018/10/as-is-to-be-na-melhoria-de-processos/>. Acesso em: 21 mar. 2024.
- FOUNDATION, P. S. Documentação do Python. 2024. <https://docs.python.org/pt-br/3/tutorial/>. Acesso em: 21 mar. 2024.
- GOOGLE. Google Classroom. 2024. <https://classroom.google.com/u/0/>. Acesso em: 21 mar. 2024.
