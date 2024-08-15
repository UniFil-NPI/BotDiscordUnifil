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
   12.2 [Tecnologias Utilizadas](#122-tecnologias-utilizadas)
13. [CRONOGRAMA](#13-cronograma)
14. [GLOSSÁRIO](#14-glossário)
15. [REFERÊNCIAS](#15-referências)

---

## 1. INTRODUÇÃO

A necessidade deste projeto surgiu a partir de uma demanda clara do stakeholder: criar uma ferramenta que permita a interação entre o Discord e o Google Classroom. A ideia não é substituir o Classroom, mas sim facilitar a vida dos usuários ao integrar as funcionalidades das duas plataformas, tornando possível receber notificações e realizar algumas operações do Classroom diretamente pelo Discord.

O ponto de partida foi a observação de que muitos estudantes já usam o Discord como uma ferramenta de comunicação e colaboração. Isso levou à pergunta: "Por que não integrar essa ferramenta, já tão popular, com o Google Classroom, que é amplamente utilizado nas atividades acadêmicas?"

Dessa reflexão nasceu a proposta de desenvolver um bot para o Discord que permite acessar certas funcionalidades do Google Classroom, tudo sem precisar sair do ambiente familiar do Discord. Com essa integração, a interação dos alunos com os recursos acadêmicos se tornaria mais simples e conveniente.

O projeto se concentra em criar essa integração de forma prática e direta. O desenvolvimento do bot envolverá etapas como pesquisa, planejamento, desenvolvimento de código e integração de APIs. O foco é sempre na usabilidade e na eficiência, para que a ferramenta realmente faça a diferença no dia a dia dos estudantes.

O objetivo final é entregar uma solução que torne o uso do Google Classroom mais acessível e dinâmico para quem já usa o Discord, ajudando a tornar o processo de aprendizagem mais integrado e colaborativo.

### 1.1 PROPOSTA E OBJETIVOS

**Objetivo Geral:**

- Desenvolver um Bot para a plataforma Discord integrado ao Google Classroom, proporcionando aos alunos uma experiência mais integrada e acessível no gerenciamento de suas atividades acadêmicas com as funcionalidades presentes no Google Classroom.

**Objetivos Específicos:**

1. Integrar o Bot ao Google Classroom, permitindo o acesso e a visualização das tarefas, notificações de turma, materiais e calendários diretamente no Discord.
2. Desenvolver recursos de notificação e lembretes automatizados no Bot, para manter os alunos informados sobre prazos, eventos e atualizações relevantes.
3. Desenvolver meios que promovem o uso contínuo da ferramenta, que melhoram a qualidade de vida das features presentes no Google Classroom.

### 1.2 JUSTIFICATIVA

A proposta do sistema é desenvolver um Bot para a plataforma Discord integrado ao Google Classroom, oferecendo aos alunos da UniFil uma ferramenta prática e eficiente para gerenciamento de suas atividades acadêmicas. O sistema permitirá aos estudantes acessar e acompanhar suas tarefas, notificações de turma, materiais de estudo, pendências e calendários diretamente no ambiente familiar do Discord.

Essa proposta se justifica como válida e importante para a UniFil por diversos motivos:

- **Facilidade de acesso:** O Discord é uma ferramenta amplamente utilizada pelos estudantes, tornando-se uma escolha natural para disponibilizar os recursos do Google Classroom. Isso facilita o acesso e a utilização por parte dos alunos, reduzindo possíveis barreiras de uso.
- **Melhoria na comunicação:** O Bot desenvolvido possibilitará a automatização de notificações e lembretes, garantindo que os alunos estejam sempre atualizados sobre suas obrigações acadêmicas. Isso contribuirá para uma comunicação mais eficaz entre os estudantes e a instituição.

Dessa forma, a proposta do sistema não apenas atende às necessidades dos alunos em termos de praticidade e acessibilidade, mas também contribui para uma gestão mais eficiente e eficaz por parte da UniFil, promovendo uma experiência acadêmica mais integrada e satisfatória para todos os envolvidos.

---

## 2. DIAGRAMA DE CASO DE USO

Na UML, os diagramas de caso de uso modelam o comportamento de um sistema e ajudam a capturar os requisitos do sistema. Segue abaixo o Diagrama de Caso de Uso do projeto:

![O Diagrama de Caso de Uso Atualizado](https://i.imgur.com/04khoTt.png)

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

A linguagem de programação que será utilizada é o Python 3.12.2. Para saber mais sobre as linguagens acesse [Documentação do Python](https://docs.python.org/pt-br/3/tutorial/) .

### 12.2 Tecnologias Utilizadas

As seguintes tecnologias serão utilizadas no desenvolvimento do projeto:

- **Python 3.10**: Linguagem de programação principal. [Python Documentation](https://docs.python.org/pt-br/3/tutorial/) .
- **Requests**: Para realizar chamadas HTTP. [Requests Documentation](https://docs.python-requests.org/en/latest/) .
- **discord.py**: Biblioteca para integração com o Discord. [discord.py Documentation](https://discordpy.readthedocs.io/en/stable/) .
- **python-dotenv**: Para gerenciar variáveis de ambiente. [python-dotenv Documentation](https://saurabhdaware.github.io/python-dotenv/) .
- **discord-py-slash-command**: Para criar comandos de barra no Discord. [discord-py-slash-command Documentation](https://discord-py-slash-command.readthedocs.io/en/latest/) .
- **discord-py-interactions**: Para gerenciar interações no Discord. [discord-py-interactions Documentation](https://discord-py-interactions.readthedocs.io/en/latest/) .
- **Google Auth**: Para autenticação com o Google. [Google Auth Documentation](https://google-auth.readthedocs.io/en/latest/) .
- **Google API Python Client**: Para acessar a API do Google Classroom. [Google API Python Client Documentation](https://googleapis.github.io/google-api-python-client/docs/) .
- **pytz**: Para manipulação de fuso horário. [pytz Documentation](https://pythonhosted.org/pytz/) .

## 13. CRONOGRAMA

O cronograma detalha as etapas e prazos do projeto, garantindo que todas as atividades sejam concluídas dentro do tempo previsto. Segue abaixo o cronograma do projeto:

![Cronograma](https://i.imgur.com/poqPykN.png)

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
- DOCUMENTAÇÃO DO PYTHON. Requests. 2024. <https://docs.python-requests.org/en/latest/>. Acesso em: 21 mar. 2024.
- DISCORD. discord.py Documentation. 2024. <https://discordpy.readthedocs.io/en/stable/>. Acesso em: 21 mar. 2024.
- DOCUMENTAÇÃO DO PYTHON. python-dotenv. 2024. <https://saurabhdaware.github.io/python-dotenv/>. Acesso em: 21 mar. 2024.
- DISCORD. discord-py-slash-command Documentation. 2024. <https://discord-py-slash-command.readthedocs.io/en/latest/>. Acesso em: 21 mar. 2024.
- DISCORD. discord-py-interactions Documentation. 2024. <https://discord-py-interactions.readthedocs.io/en/latest/>. Acesso em: 21 mar. 2024.
- GOOGLE. Google Auth Documentation. 2024. <https://google-auth.readthedocs.io/en/latest/>. Acesso em: 21 mar. 2024.
- GOOGLE. Google API Python Client Documentation. 2024. <https://googleapis.github.io/google-api-python-client/docs/>. Acesso em: 21 mar. 2024.
- DOCUMENTAÇÃO DO PYTHON. pytz Documentation. 2024. <https://pythonhosted.org/pytz/>. Acesso em: 21 mar. 2024.
