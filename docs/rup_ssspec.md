# Bot de Discord - Especificação Complementar

**Versão:** 1.0

---

## Histórico da Revisão

| Data       | Versão | Descrição              | Autor                  |
|------------|--------|------------------------|------------------------|
| 02/04/2024 | 1.0    | Criação do Documento   | Gabriel Zanoni Herculano |
| 03/04/2024 | 1.1   | Conversão para M.D   | Gabriel Zanoni Herculano |

---

## Índice

- [1. Introdução](#introducao)
  - [1.1 Objetivo](#objetivo)
  - [1.2 Escopo](#escopo)
  - [1.3 Definições, Acrônimos e Abreviações](#definicoes-acronimos-e-abreviacoes)
  - [1.4 Referências](#referencias)
  - [1.5 Visão Geral](#visao-geral)
- [2. Funcionalidades](#funcionalidades)
- [3. Utilidade](#utilidade)
- [4. Confiabilidade](#confiabilidade)
- [5. Desempenho](#desempenho)
- [6. Suportabilidade](#suportabilidade)
- [7. Restrições de Design](#restricoes-de-design)
- [8. Documentação do Usuário e Sistema de Ajuda](#documentacao-do-usuario-e-sistema-de-ajuda)
- [9. Componentes Comprados](#componentes-comprados)
- [10. Interfaces](#interfaces)
- [11. Requisitos de Licença](#requisitos-de-licenca)
- [12. Observações Legais e Direitos Autorais](#observacoes-legais-e-direitos-autorais)
- [13. Padrões Aplicáveis](#padroes-aplicaveis)

---

## Especificação Complementar

### 1. Introdução

A Especificação Complementar abaixo oferece uma visão detalhada dos requisitos do sistema para o Bot de Discord, com foco na integração com o Google Sala de Aula. Esta documentação captura os elementos essenciais não diretamente abordados pelos casos de uso do modelo de caso de uso, incluindo requisitos legais, atributos de qualidade do sistema e outras considerações relevantes.

#### 1.1 Objetivo

Esta Especificação Complementar define os requisitos adicionais e complementares para o sistema de desenvolvimento e pedidos do Bot, abrangendo aspectos como requisitos legais, atributos de qualidade, restrições de design e considerações operacionais.

#### 1.2 Escopo

O escopo desta especificação abrange todas as funcionalidades relacionadas ao sistema de desenvolvimento do bot e à plataforma. Isso inclui todas as funcionalidades e processos necessários para o término do projeto.

#### 1.3 Definições, Acrônimos e Abreviações

- **Bot:** Um bot da Plataforma Discord é um usuário não-humano que responde de forma automatizada aos inputs entregues pelo usuário do Bot. Ele é hospedado em um servidor centralizado e realiza a comunicação com a plataforma Google Classroom para interação das informações do usuário.
- **Discord:** Plataforma de comunicação que permite acesso a chatrooms com múltiplos usuários, interação por voz e envio de imagens, arquivos, etc.
- **Classroom:** Plataforma da Google para interação entre alunos e professores, onde materiais e atividades podem ser entregues e realizados pelos alunos e vistoriados pelos professores.

#### 1.4 Referências

Refira-se ao Documento Glossário e outros documentos disponíveis para o Projeto.

#### 1.5 Visão Geral

Esta especificação centraliza todos os requisitos necessários para o desenvolvimento e funcionamento do Bot.

### 2. Funcionalidades

Esta seção apresenta os requisitos funcionais do sistema do Bot, estruturados com base nas principais áreas de funcionalidade do sistema.

#### Integração com o Google Classroom

- Permitir que os usuários vinculem suas contas do Google Classroom com o Discord.
- Visualização das salas de aula, tarefas pendentes, materiais e notificações especiais dentro do Discord.
- Sincronização com o Calendário.
- Envio de notificações no Discord para novas atribuições, materiais adicionados ou outras atualizações relevantes no Google Classroom.
- Interatividade para marcar tarefas como concluídas, solicitar informações sobre tarefas específicas, etc.

### 3. Utilidade

- **Organização:** Permite a organização das tarefas dos alunos para fácil acesso através do Discord, sendo regularmente utilizada por estudantes.
- **Eficiência:** Economiza tempo e otimiza a entrega de materiais.

### 4. Confiabilidade

- **Segurança:** Garante a segurança das informações dos usuários, não armazenando dados sensíveis. A autenticação com o Google Classroom segue as melhores práticas de segurança.
- **Disponibilidade:** O aplicativo está disponível 24 horas, 7 dias por semana.

### 5. Desempenho

- **Múltiplos Usuários:** Permite a interação de múltiplos usuários simultaneamente.

### 6. Suportabilidade

- **Diferentes Servidores:** Permite a utilização em diversos servidores conforme necessário.

### 7. Restrições de Design

- **Necessidade de Internet:** Requer conexão com a internet.
- **Necessidade do Discord:** Requer acesso à plataforma Discord.

### 8. Documentação do Usuário e Sistema de Ajuda

O bot deve ser amigável para os usuários, com foco na acessibilidade para pessoas de todas as idades, especialmente jovens.

### 9. Componentes Comprados

O bot será hospedado em um servidor disponibilizado pelo Centro de Ensino UniFil.

### 10  Interfaces

- **Interfaces com o Usuário:** Comandos disponíveis para o usuário.
- **Interfaces de Hardware:** Acesso à internet.
- **Interfaces de Software:** Servidor para hospedar o Bot.
- **Interfaces de Comunicações:** API para interagir com o Google Classroom.

### 11. Requisitos de Licença

Não existe uma licença de uso, pois será restrito APENAS ao servidor disponibilizado pela UniFil.

### 12.. Observações Legais e Direitos Autorais

Toda autoria legal será disponibilizada para a Empresa UniFil, que hospedará o Bot e terá todos os direitos legais para sua distribuição e utilização.

### 13. Padrões Aplicáveis

O único padrão aplicável será a Segurança da Informação do usuário, que não será armazenada pelo Bot ou pelo aplicativo para impedir vazamentos e má distribuição.

---

Se precisar de mais alguma coisa, estou à disposição!
