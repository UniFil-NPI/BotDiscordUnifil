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
4. [NOTAÇÃO BPMN](#4-workflow-as-is-na-notação-bpmn)
   - 4.1 [WORKFLOW AS-IS](#41-workflow-as-is)
   - 4.2 [WORKFLOW TO-BE](#42-workflow-to-be)
5. [RECURSOS E AMBIENTE DE DESENVOLVIMENTO](#5-recursos-e-ambiente-de-desenvolvimento)
   - 5.1 [Linguagem de Programação](#51-linguagem-de-programação)
   - 5.2 [Ambiente de Desenvolvimento](#52-ambiente-de-desenvolvimento)
6. [CRONOGRAMA](#6-cronograma)
7. [CONCLUSÕES E TRABALHOS FUTUROS](#7-conclusões-e-trabalhos-futuros)
   - 7.1 [Conclusões](#71-conclusões)
   - 7.2 [Trabalhos Futuros](#72-trabalhos-futuros)
8. [REFERÊNCIAS](#8-referências)
9. [APÊNDICE](#8-apêndice)

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

### 3.2.1 Classe 1: `GoogleClassroomManager`

- **Descrição:** 
  - A classe `GoogleClassroomManager` é responsável por gerenciar as interações de alto nível com a API do Google Classroom. Ela utiliza a `GoogleClassroomAuthenticator` para autenticar as credenciais e cria uma instância de `GoogleClassroomService` para realizar as operações na API. Essa classe fornece métodos para listar cursos (`get_courses()`) e listar trabalhos de curso (`get_coursework(course_id)`), entre outras operações. 

### 3.2.2 Classe 2: `GoogleClassroomService`

- **Descrição:** 
  - A classe `GoogleClassroomService` serve como um intermediário para realizar chamadas específicas à API do Google Classroom. Ela contém métodos que permitem listar cursos (`list_courses(page_size)`), listar trabalhos de curso (`list_coursework(course_id)`), listar estudantes (`list_students(course_id)`), e listar submissões de estudantes (`list_student_submissions(course_id, coursework_id)`). Esta classe utiliza as credenciais autenticadas para realizar essas operações.

### 3.2.3 Classe 3: `GoogleClassroomAuthenticator`

- **Descrição:** 
  - A classe `GoogleClassroomAuthenticator` é responsável por autenticar o usuário com a API do Google Classroom. Ela carrega as credenciais do usuário a partir de um arquivo token e verifica se as credenciais são válidas ou se precisam ser atualizadas. Se necessário, a classe renova o token de autenticação.

### 3.2.4 Classe 4: `Course`

- **Descrição:** 
  - A classe `Course` representa um curso no Google Classroom. Ela encapsula as propriedades básicas de um curso, como o ID do curso (`id`), o nome (`name`), a seção (`section`), o código de inscrição (`enrollment_code`), e outros dados relacionados ao curso (`course_data`). Além disso, possui um método `__str__()` para fornecer uma representação em string do curso, facilitando a exibição de informações.

### 3.2.5 Classe 5: `Paginator`

- **Descrição:** 
  - A classe `Paginator` é utilizada para paginar e formatar os dados que serão exibidos no Discord, especialmente em mensagens que podem conter listas longas, como a de cursos ou tarefas. Ela gerencia a navegação entre as páginas de itens (`items`), mantendo o controle da página atual (`page`) e gerando os embeds do Discord para exibição. A classe também inclui métodos para atualizar os botões de navegação e lidar com interações do usuário.

### Resumo das Conexões entre as Classes

- **`GoogleClassroomManager`**:
  - **Utiliza** `GoogleClassroomService` para acessar a API do Google Classroom.
  - **Utiliza** `GoogleClassroomAuthenticator` para autenticar as credenciais.
  - **Gera** instâncias da classe `Course` quando lista cursos.

- **`GoogleClassroomService`**:
  - **Utiliza** credenciais fornecidas por `GoogleClassroomAuthenticator` para se comunicar com a API do Google Classroom.

- **`Paginator`**:
  - **Gerencia** a paginação e a formatação dos dados para exibição no Discord.

### 3.3 Diagrama de Sequência


![GERAL](https://i.imgur.com/jOaM0os.png)

O Diagrama de Sequência é um diagrama usado em UML que representa a sequência de processos num programa de computador. Abaixo, segue uma descrição da ordem em que os eventos ocorrem no Diagrama de Sequência do projeto.

### Overview do Diagrama de Sequência

Este diagrama de sequência descreve a interação entre um usuário, um bot (provavelmente no Discord), o gerenciador do Google Classroom (`Gerenciador`), e a API do Google Classroom através de diversos componentes, como o `Autenticador` e os `Serviços`. Ele demonstra como as requisições fluem através do sistema desde o momento em que o usuário solicita informações até o momento em que as informações são retornadas e exibidas.

#### 1. **Solicitação de Cursos** (`/cursos`)

- **Usuário -> Bot:** O processo inicia quando o usuário solicita a lista de cursos disponíveis utilizando o comando `/cursos`.
- **Bot -> Gerenciador:** O bot encaminha essa solicitação ao `Gerenciador`, chamando o método `get_courses()`.
- **Gerenciador -> Autenticador:** O `Gerenciador` verifica as credenciais e solicita autenticação através do método `authenticate()`.
- **Autenticador -> Autenticador:** O `Autenticador` verifica o token existente, assegurando que ainda é válido.
- **Autenticador -> GoogleClassroomAPI:** Se o token estiver expirado ou não existir, o `Autenticador` faz uma requisição à API do Google Classroom para gerar ou renovar o token.
- **GoogleClassroomAPI -> Autenticador:** A API retorna o token atualizado.
- **Autenticador -> Gerenciador:** O `Autenticador` retorna as credenciais autenticadas para o `Gerenciador`.
- **Gerenciador -> Serviços:** Com as credenciais em mãos, o `Gerenciador` cria uma nova instância de `GoogleClassroomService` e solicita a lista de cursos usando o método `list_courses()`.
- **Serviços -> GoogleClassroomAPI:** O `Serviços` faz uma requisição para obter a lista de cursos diretamente da API do Google Classroom.
- **GoogleClassroomAPI -> Serviços:** A API retorna a lista de cursos.
- **Serviços -> Gerenciador:** O `Serviços` repassa a lista de cursos para o `Gerenciador`.
- **Gerenciador -> Bot:** O `Gerenciador` retorna a lista de cursos para o Bot.
- **Bot -> Usuário:** O bot exibe a lista de cursos para o usuário.

#### 2. **Solicitação de Tarefas** (`/tarefas <course_id>`)

- **Usuário -> Bot:** O usuário solicita a lista de tarefas de um curso específico utilizando o comando `/tarefas <course_id>`.
- **Bot -> Gerenciador:** O bot encaminha a solicitação ao `Gerenciador` chamando o método `get_coursework(course_id)`.
- **Gerenciador -> Serviços:** O `Gerenciador` solicita ao `Serviços` a lista de tarefas do curso específico através do método `list_coursework(course_id)`.
- **Serviços -> GoogleClassroomAPI:** O `Serviços` faz a requisição para obter as tarefas diretamente da API do Google Classroom.
- **GoogleClassroomAPI -> Serviços:** A API retorna a lista de tarefas para o curso especificado.
- **Serviços -> Gerenciador:** O `Serviços` repassa a lista de tarefas para o `Gerenciador`.
- **Gerenciador -> Bot:** O `Gerenciador` retorna a lista de tarefas para o Bot.
- **Bot -> Usuário:** O bot exibe a lista de tarefas para o usuário.

#### 3. **Solicitação de Calendário** (`/calendario`)

- **Usuário -> Bot:** O usuário solicita o calendário de atividades utilizando o comando `/calendario`.
- **Bot -> Gerenciador:** O bot encaminha a solicitação ao `Gerenciador` chamando o método `get_courses()` novamente para listar todos os cursos.
- **Gerenciador -> Serviços:** O `Gerenciador` solicita ao `Serviços` a lista de cursos através do método `list_courses()`.
- **Serviços -> GoogleClassroomAPI:** O `Serviços` faz a requisição para obter os cursos diretamente da API do Google Classroom.
- **GoogleClassroomAPI -> Serviços:** A API retorna a lista de cursos.
- **Serviços -> Gerenciador:** O `Serviços` repassa a lista de cursos para o `Gerenciador`.
- **Gerenciador -> Bot:** O `Gerenciador` retorna a lista de cursos para o Bot.
- **Bot -> Gerenciador:** O Bot então solicita todas as tarefas associadas a esses cursos chamando o método `get_coursework(course_id)` para cada curso.
- **Gerenciador -> Serviços:** O `Gerenciador` chama `list_coursework(course_id)` para cada curso.
- **Serviços -> GoogleClassroomAPI:** O `Serviços` faz requisições à API do Google Classroom para obter as tarefas de cada curso.
- **GoogleClassroomAPI -> Serviços:** A API retorna as listas de tarefas.
- **Serviços -> Gerenciador:** O `Serviços` repassa as listas de tarefas para o `Gerenciador`.
- **Gerenciador -> Bot:** O `Gerenciador` retorna todas as tarefas para o Bot.
- **Bot -> Usuário:** O bot exibe o calendário de atividades com todas as tarefas para o usuário.

### Diagramas de Sequência

### 1. **CALENDARIO**
   - ![CALENDARIO](https://i.imgur.com/pBkye7Y.png)
   - **Descrição**: Descreve a sequência de ações para obter e exibir o calendário de atividades de todos os cursos. O usuário solicita o calendário, e o bot faz chamadas à API para listar cursos e seus respectivos trabalhos, exibindo os dados de forma consolidada.

### 2. **API**
   - ![API](https://i.imgur.com/eJ40r8L.png)
   - **Descrição**: Este diagrama foca nas interações detalhadas com a API do Google Classroom. Mostra como o sistema autentica e usa as credenciais para realizar várias operações, como obter listas de cursos ou trabalhos de curso.

### 3. **MATERIAS**
   - ![MATERIAS](https://i.imgur.com/cYXEQHn.png)
   - **Descrição**: Detalha o processo de listagem de matérias (cursos) disponíveis. O usuário solicita as matérias, o bot consulta o gerenciador, que por sua vez interage com a API do Google Classroom para recuperar a lista de cursos, que é então exibida ao usuário.

### 4. **NOTIFICAR**
   - ![NOTIFICAR](https://i.imgur.com/rfaRhgL.png)
   - **Descrição**: Descreve o processo de notificação do usuário. O bot verifica se as notificações estão ativas e, caso estejam, envia as notificações apropriadas ao usuário com base em eventos específicos, como a conclusão de um comando.

### 5. **OBTER_ALUNO**
   - ![OBTER_ALUNO](https://i.imgur.com/brqvb6l.png)
   - **Descrição**: Mostra como o sistema recupera informações de um aluno específico com base em seu email. O processo envolve verificar a lista de alunos em um curso específico através da API para identificar o aluno correspondente.

### 6. **REALIZAR_COMANDO**
   - ![REALIZAR_COMANDO](https://i.imgur.com/bAnJ9bh.png)
   - **Descrição**: Foca no fluxo de execução de um comando genérico pelo usuário. Dependendo do comando, o bot pode realizar uma ação diretamente ou envolver a API do Google Classroom para obter os dados necessários.

### 7. **TAREFAS**
   - ![TAREFAS](https://i.imgur.com/rCIM9ef.png)
   - **Descrição**: Representa a sequência para listar as tarefas de um curso específico. O usuário solicita as tarefas para um determinado curso, e o bot interage com a API para recuperar e apresentar as tarefas associadas ao curso especificado.

### 8. **VERIFICAR_PENDENCIA**
   - ![VERIFICAR_PENDENCIA](https://i.imgur.com/NXaecr3.png)
   - **Descrição**: Mostra o processo de verificação de pendências de tarefas de um aluno. O bot consulta a API do Google Classroom para identificar tarefas que ainda não foram entregues pelo aluno e então informa o usuário sobre essas pendências.

---

## 4. WORKFLOW NA NOTAÇÃO BPMN

### 4.1 WORKFLOW AS-IS 
AS-IS é a visão dos processos atuais de uma organização, que mostra como uma empresa realiza suas atividades em um determinado momento. Segue na Figura abaixo o diagrama de workflow AS-IS:

![Workflow AS-IS na Notação BPMN](https://i.imgur.com/9qVxWZm.png)


### 4.2 WORKFLOW TO-BE 
TO-BE é a visão dos processos futuros de uma organização, que mostra como uma empresa gostaria que suas atividades em um determinado momento ficassem idealizadas. Segue na Figura abaixo o diagrama de workflow TO-BE:

![Workflow TO-BE na Notação BPMN](https://i.imgur.com/aTUGJwE.png)

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


## 9. APÊNDICE

### Diagramas

- [Diagrama de Caso de Uso](rup_uc.md)
- [Diagrama de Classe](rup_class.md) 
- [Diagrama de Sequência](seq/rup_seq.md)
- [Diagrama de Implantação](rup_imp.md)
- [Diagrama de Workflow (AS-IS)](as_is.md)

### Documentação 

- [Especificação Complementar](rup_ssspec.md)   
- [Visão](visao.md)
- [Pedido do Investidor](rup_stkreq.md)
- [Glossário](rup_gloss.md)