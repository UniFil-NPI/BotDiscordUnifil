# Especificação de Caso de Uso: "Matérias"

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

Este caso de uso descreve o comando "Matérias" do bot no Discord, que tem como objetivo retornar todas as matérias cadastradas do aluno que estão ativas no momento.

## 2. Fluxo Básico de Eventos

1. O usuário faz login no Discord.
2. O usuário acessa o chat específico no servidor do Discord ou as mensagens privadas do Bot.
3. O usuário digita um comando iniciado por "/" no prompt de chat.
4. O usuário preenche o prompt com o comando `/Matérias`.
5. O bot responde ao usuário com uma lista de todas as matérias cadastradas que estão ativas.

## 3. Fluxos Alternativos

- **3a. Usuário não tem matérias ativas cadastradas**  
  - 3a.1. O bot informa ao usuário que não há matérias ativas cadastradas no momento.

## 4. Subfluxos

Não há subfluxos para este caso de uso.

## 5. Cenários Chave

Este caso de uso é acionado quando o usuário interage com o sistema para executar o comando de listagem de matérias ativas no bot.

## 6. Condições Prévias

- O usuário deve ter uma conta no Discord.
  - Consequentemente, o usuário deve estar logado no Discord em seu dispositivo.
- O usuário deve estar no mesmo ambiente que o bot, seja um servidor compartilhado ou nas mensagens privadas com o bot.
  - O bot pode estar presente em um ou mais servidores, e o usuário deve compartilhar um desses ambientes para poder interagir com ele.
- O usuário deve ter vinculado sua conta do Classroom com o Discord, para que o bot possa acessar suas informações de matérias.
  - Este vínculo será realizado através de um método a ser definido, possivelmente por um comando adicional.

## 7. Condições Posteriores

Não há condições posteriores específicas para este caso de uso.

## 8. Pontos de Extensão

Não há pontos de extensão para este caso de uso.

## 9. Requisitos Especiais

Os requisitos especiais estão disponíveis no documento [Especificação Suplementar](rup_supdoc.md).

## 10. Informações Adicionais

