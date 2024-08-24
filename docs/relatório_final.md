# INTEGRAÇÃO CLASSROOM DISCORD

**Gabriel Zanoni Herculano**  
**Mario Henrique Akihiko da Costa**  
**Centro Universitário Filadélfia**  
**Londrina, 2024**

---

## SUMÁRIO

1. [INTRODUÇÃO](#1-introdução)
   - 1.1 [PROPOSTA E OBJETIVOS](#11-proposta-e-objetivos)
   - 1.2 [JUSTIFICATIVA](#12-justificativa)
2. [DESCRIÇÃO DO SISTEMA](#2-descrição-do-sistema)
   - 2.1 [Tecnologias Utilizadas](#21-tecnologias-utilizadas)
   - 2.2 [Requisitos Funcionais](#22-requisitos-funcionais)
   - 2.3 [Requisitos Não Funcionais](#23-requisitos-não-funcionais)
3. [MODELAGEM DO SISTEMA](#3-modelagem-do-sistema)
   - 3.1 [Diagrama de Caso de Uso](#31-diagrama-de-caso-de-uso)
   - 3.2 [Diagrama de Classe](#32-diagrama-de-classe)
   - 3.3 [Diagrama de Sequência](#33-diagrama-de-sequência)
4. [WORKFLOW AS-IS NA NOTAÇÃO BPMN](#4-workflow-as-is-na-notação-bpmn)
5. [RECURSOS E AMBIENTE DE DESENVOLVIMENTO](#5-recursos-e-ambiente-de-desenvolvimento)
   - 5.1 [Linguagem de Programação](#51-linguagem-de-programação)
   - 5.2 [Ambiente de Desenvolvimento](#52-ambiente-de-desenvolvimento)
6. [CRONOGRAMA](#6-cronograma)
7. [CONCLUSÕES E TRABALHOS FUTUROS](#7-conclusões-e-trabalhos-futuros)
   - 7.1 [Conclusões](#71-conclusões)
   - 7.2 [Trabalhos Futuros](#72-trabalhos-futuros)
8. [REFERÊNCIAS](#8-referências)

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
3. Desenvolver meios que promovam o uso contínuo da ferramenta, melhorando a qualidade de vida das funcionalidades presentes no Google Classroom.

### 1.2 JUSTIFICATIVA

A proposta do sistema é desenvolver um Bot para a plataforma Discord integrado ao Google Classroom, oferecendo aos alunos da UniFil uma ferramenta prática e eficiente para gerenciamento de suas atividades acadêmicas. O sistema permitirá aos estudantes acessar e acompanhar suas tarefas, notificações de turma, materiais de estudo, pendências e calendários diretamente no ambiente familiar do Discord.

Essa proposta se justifica como válida e importante para a UniFil por diversos motivos:

- **Facilidade de acesso:** O Discord é uma ferramenta amplamente utilizada pelos estudantes, tornando-se uma escolha natural para disponibilizar os recursos do Google Classroom. Isso facilita o acesso e a utilização por parte dos alunos, reduzindo possíveis barreiras de uso.
- **Melhoria na comunicação:** O Bot desenvolvido possibilitará a automatização de notificações e lembretes, garantindo que os alunos estejam sempre atualizados sobre suas obrigações acadêmicas. Isso contribuirá para uma comunicação mais eficaz entre os estudantes e a instituição.

Dessa forma, a proposta do sistema não apenas atende às necessidades dos alunos em termos de praticidade e acessibilidade, mas também contribui para uma gestão mais eficiente e eficaz por parte da UniFil, promovendo uma experiência acadêmica mais integrada e satisfatória para todos os envolvidos.

---

## 2. DESCRIÇÃO DO SISTEMA

### 2.1 Tecnologias Utilizadas

As seguintes tecnologias serão utilizadas no desenvolvimento do projeto:

- **Python 3.10**: Linguagem de programação principal. [Python Documentation](https://docs.python.org/pt-br/3/tutorial/).
- **Requests**: Para realizar chamadas HTTP. [Requests Documentation](https://docs.python-requests.org/en/latest/).
- **discord.py**: Biblioteca para integração com o Discord. [discord.py Documentation](https://discordpy.readthedocs.io/en/stable/).
- **python-dotenv**: Para gerenciar variáveis de ambiente. [python-dotenv Documentation](https://saurabhdaware.github.io/python-dotenv/).
- **discord-py-slash-command**: Para criar comandos de barra no Discord. [discord-py-slash-command Documentation](https://discord-py-slash-command.readthedocs.io/en/latest/).
- **discord-py-interactions**: Para gerenciar interações no Discord. [discord-py-interactions Documentation](https://discord-py-interactions.readthedocs.io/en/latest/).
- **Google Auth**: Para autenticação com o Google. [Google Auth Documentation](https://google-auth.readthedocs.io/en/latest/).
- **Google API Python Client**: Para acessar a API do Google Classroom. [Google API Python Client Documentation](https://googleapis.github.io/google-api-python-client/docs/).
- **pytz**: Para manipulação de fuso horário. [pytz Documentation](https://pythonhosted.org/pytz/).

### 2.2 Requisitos Funcionais

Os requisitos funcionais descrevem as funcionalidades específicas que o sistema deve ter para atender às necessidades dos usuários e stakeholders.

1. **Autenticação com o Google Classroom:**
   - O sistema deve permitir que os usuários façam login usando suas credenciais do Google para acessar suas contas do Google Classroom.

2. **Recebimento de Notificações:**
   - O bot deve ser capaz de enviar notificações no Discord sobre novas tarefas, atualizações de turmas e eventos programados no Google Classroom.

3. **Listagem de Tarefas:**
   - O bot deve listar as tarefas pendentes de uma turma específica no Google Classroom.

4. **Consulta a Materiais:**
   - O bot deve permitir que os usuários consultem materiais de estudo postados no Google Classroom diretamente no Discord.

5. **Lembretes Automáticos:**
   - O bot deve enviar lembretes automáticos sobre prazos de entrega e eventos programados.

### 2.3 Requisitos Não Funcionais

Os requisitos não funcionais descrevem os atributos de qualidade que o sistema deve possuir.

1. **Usabilidade:**
   - O bot deve ser fácil de usar, com comandos claros e intuitivos para os usuários.

2. **Desempenho:**
   - O bot deve responder às solicitações dos usuários em tempo hábil, sem atrasos perceptíveis.

3. **Segurança:**
   - As credenciais dos usuários e outras informações sensíveis devem ser armazenadas e transmitidas de forma segura, utilizando criptografia.

4. **Escalabilidade:**
   - O sistema deve ser capaz de lidar com um número crescente de usuários sem perda de desempenho.

5. **Manutenibilidade:**
   - O código deve ser escrito de forma clara e documentado adequadamente, facilitando futuras manutenções e atualizações.

---

## 3. MODELAGEM DO SISTEMA

### 3.1 Diagrama de Caso de Uso

Na UML, os diagramas de caso de uso modelam o comportamento de um sistema e ajudam a capturar os requisitos do sistema. Segue abaixo o Diagrama de Caso de Uso do projeto:

![Diagrama de Caso de Uso](https://i.imgur.com/04khoTt.png)

### 3.1.1 Obter Aluno

- **Descrição:** Este caso de uso permite ao sistema obter informações de um aluno específico com base no seu Discord ID. O sistema faz uma chamada a um endpoint de uma API para recuperar os dados do aluno correspondente. Essa funcionalidade é essencial para personalizar a interação do bot com os usuários, garantindo que as informações acadêmicas exibidas estejam corretamente associadas ao aluno correto.
- **Especificação:** [Especificação do Caso de Uso: Obter Aluno](uc_spec/rup_ucspec_discernir_aluno.md)

### 3.1.2 Verificar Pendências

- **Descrição:** Este caso de uso permite ao sistema verificar todas as pendências de um aluno, como trabalhos que ainda não foram realizados e que precisam ser entregues até a data limite. A funcionalidade é crucial para ajudar os alunos a manterem-se organizados e informados sobre suas responsabilidades acadêmicas, evitando esquecimentos e atrasos na entrega de trabalhos.
- **Especificação:** [Especificação do Caso de Uso: Verificar Pendência](uc_spec/rup_ucspec_verificar_pendencias.md)

### 3.1.3 Notificar Usuário

- **Descrição:** Este caso de uso permite ao sistema notificar um usuário de forma privada sobre eventos acadêmicos, como prazos de entrega e atualizações de turma, desde que o usuário tenha ativado as notificações com o bot. A notificação é enviada diretamente ao usuário através do Discord, ajudando-o a manter-se atualizado e organizado.
- -**Especificação:** [Especificação do Caso de Uso: Verificar Pendência](uc_spec/rup_ucspec_notificar.md)

### 3.2 Diagrama de Classe

O diagrama de classe é uma representação da estrutura e relações das classes que servem de modelo para objetos. A seguir, apresentamos o Diagrama de Classe do projeto:

![Diagrama de Classe](https://i.imgur.com/fICzfTd.png)

### 3.3 Diagrama de Sequência

O Diagrama de Sequência é um diagrama usado em UML que representa a sequência de processos num programa de computador. Segue abaixo o Diagrama de Sequência do projeto:

### Diagramas de Sequência

![GERAL](https://i.imgur.com/jOaM0os.png)
![CALENDARIO](https://i.imgur.com/pBkye7Y.png)
![API](https://i.imgur.com/eJ40r8L.png)
![MATERIAS](https://i.imgur.com/cYXEQHn.png)
![NOTIFICAR](https://i.imgur.com/rfaRhgL.png)
![OBTER_ALUNO](https://i.imgur.com/brqvb6l.png)
![REALIZAR_COMANDO](https://i.imgur.com/bAnJ9bh.png)
![TAREFAS](https://i.imgur.com/rCIM9ef.png)
![VERIFICAR_PENDENCIA](https://i.imgur.com/NXaecr3.png)

---

## 4. WORKFLOW AS-IS NA NOTAÇÃO BPMN

AS-IS é a visão dos processos atuais de uma organização, que mostra como uma empresa realiza suas atividades em um determinado momento. Segue na Figura abaixo o diagrama de workflow AS-IS:

![Workflow AS-IS na Notação BPMN](https://i.imgur.com/9qVxWZm.png)

---

## 5. RECURSOS E AMBIENTE DE DESENVOLVIMENTO

### 5.1 Linguagem de Programação

A linguagem de programação que será utilizada é o Python 3.12.2. Para saber mais sobre as linguagens, acesse [Documentação do Python](https://docs.python.org/pt-br/3/tutorial/).

### 5.2 Ambiente de Desenvolvimento

O ambiente de desenvolvimento será configurado utilizando as seguintes ferramentas e tecnologias:

- **IDE:** Visual Studio Code
- **Versionamento de Código:** Git e GitHub
- **Ambiente Virtual:** Poetry para gerenciamento de dependências e ambiente

---

## 6. CRONOGRAMA

O cronograma detalha as etapas e prazos do projeto, garantindo que todas as atividades sejam concluídas dentro do tempo previsto. Segue abaixo o cronograma do projeto:

![Cronograma](https://i.imgur.com/poqPykN.png)

---

## 7. CONCLUSÕES E TRABALHOS FUTUROS

### 7.1 Conclusões

Neste trabalho, foi possível observar a importância da integração entre plataformas educacionais e ferramentas amplamente utilizadas pelos estudantes, como o Discord. A criação do bot para Discord que interage com o Google Classroom não só facilita o acesso às informações acadêmicas, mas também melhora a comunicação e a organização dos alunos.

### 7.2 Trabalhos Futuros

Para aprimorar ainda mais o bot, planejo adicionar novas features de acordo com o ciclo de feedback entregue pelos usuários. Aprimorando cada vez mais o sistema.

---

## 8. REFERÊNCIAS

- DISCORD. Discord. 2024. <https://discord.com/>. Acesso em: 21 mar. 2024.
- EUAX. EUAX WorkFlow AS-IS TO-BE. 2024. <https://www.euax.com.br/2018/10/as-is-to-be-na-melhoria-de-processos/>. Acesso em: 21 mar. 2024.
- FOUNDATION, P. S. Documentação do Python. 2024. <https://docs.python.org/pt-br/3/tutorial/>. Acesso em: 21 mar. 2024.
- GOOGLE. Google Classroom. 2024. <https://classroom.google.com/u/0/>. Acesso em: 21 mar. 2024.
- DOCUMENTAÇÃO DO PYTHON. Requests. 2024. <https://docs.python-requests.org/en/latest/>. Acesso em: 21 mar. 2024.
- DISCORD. discord.py Documentation. 2024. <https://discordpy.readthedocs.io/en/stable/>. Acesso em: 21 mar. 2024.
- DOCUMENTAÇÃO DO PYTHON. python-dot
