# Especificação de Caso de Uso: "Obter Aluno"

#### Histórico da Revisão
| Data       | Versão | Descrição               | Autor                          |
|------------|--------|-------------------------|--------------------------------|
| 10/08/2024 | 1.0    | Criação do Documento    | Gabriel Zanoni (@GbrielZanoni) |

# Índice

- [1. Breve Descrição](#1-breve-descricao)	
- [2. Fluxo Básico de Eventos](#2-fluxo-basico-de-eventos) 
- [3. Fluxos Alternativos](#3-fluxos-alternativos)
- [4. Subfluxos](#4-subfluxos)	
- [5. Cenários Chave](#5-cenarios-chave) 
- [6. Condições Prévias](#6-condicoes-previas)
- [7. Condições Posteriores](#7-condicoes-posteriores)
- [8. Pontos de Extensão](#8-pontos-de-extensao)
- [9. Requisitos Especiais](#9-requisitos-especiais)
- [10. Informações Adicionais](#10-informacoes-adicionais)

# Especificação Complementar

## 1. Breve Descrição 

Este caso de uso descreve a funcionalidade "Obter Aluno" do bot no Discord, que é responsável por identificar o usuário que está interagindo com o bot, verificar seu ID do Discord, comparar com um banco de dados definido pelo stakeholder, verificar o e-mail do aluno, comparar com os e-mails presentes no Classroom, e obter as informações do aluno, como suas matérias e tarefas pendentes. Esta funcionalidade é automaticamente acionada quando o usuário executa comandos relacionados às suas informações acadêmicas, como "Atividades", "Matérias" ou "Calendário".

## 2. Fluxo Básico de Eventos

1. O bot recebe uma interação do usuário para um comando relacionado a informações acadêmicas (e.g., Atividades, Matérias, Calendário).
2. O bot verifica o ID do usuário no Discord.
3. O bot compara o ID do usuário com o banco de dados fornecido pelo stakeholder.
4. O bot obtém o e-mail associado ao ID do usuário.
5. O bot compara o e-mail do usuário com os e-mails presentes no Classroom.
6. O bot obtém as informações do aluno, como matérias e tarefas pendentes.
7. O bot continua a execução do comando original do usuário (e.g., listar atividades pendentes, matérias ativas, calendário acadêmico).

## 3. Fluxos Alternativos

- **3a. E-mail do usuário não encontrado no banco de dados**
  - 3a.1. O bot informa ao usuário que o e-mail não foi encontrado no banco de dados e solicita uma verificação manual ou instruções adicionais.
  
- **3b. ID do usuário não corresponde a nenhum aluno**
  - 3b.1. O bot informa ao usuário que seu ID do Discord não foi encontrado no banco de dados e solicita uma verificação manual ou instruções adicionais.

## 4. Subfluxos

Não há subfluxos para este caso de uso.

## 5. Cenários Chave

Este caso de uso é acionado automaticamente quando o bot recebe um comando relacionado a informações acadêmicas e precisa identificar o usuário para obter os dados relevantes.

## 6. Condições Prévias

- O usuário deve ter uma conta no Discord.
  - Consequentemente, o usuário deve estar logado no Discord em seu dispositivo.
- O usuário deve estar no mesmo ambiente que o bot, seja um servidor compartilhado ou nas mensagens privadas com o bot.
  - O bot pode estar presente em um ou mais servidores, e o usuário deve compartilhar um desses ambientes para poder interagir com ele.
- Um banco de dados contendo as informações de usuários, como ID do Discord e e-mails, deve estar configurado e acessível pelo bot.
- O usuário deve ter vinculado sua conta do Classroom com o Discord, para que o bot possa acessar suas informações acadêmicas.

## 7. Condições Posteriores

Não há condições posteriores específicas para este caso de uso.

## 8. Pontos de Extensão

Não há pontos de extensão para este caso de uso.

## 9. Requisitos Especiais

Os requisitos especiais estão disponíveis no documento [Especificação Suplementar](rup_supdoc.md).

## 10. Informações Adicionais

Não há informações adicionais para este caso de uso.
