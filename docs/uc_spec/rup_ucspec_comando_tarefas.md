# Especificação de Caso de Uso: "Atividades"

#### Histórico da Revisão
| Data       | Versão | Descrição       | Autor                          |
|------------|--------|-----------------|--------------------------------|
| 10/08/2024 | 1.0    | Criação do Documento | Gabriel Zanoni (@GbrielZanoni) |

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

Este caso de uso descreve o comando "Atividades" do bot no Discord, que tem como função listar as atividades pendentes do usuário, destacando aquelas que estão próximas de sua data de expiração.

## 2. Fluxo Básico de Eventos

1. O usuário faz login no Discord.
2. O usuário acessa o chat específico no servidor do Discord ou as mensagens privadas do Bot.
3. O usuário digita um comando iniciado por "/" no prompt de chat.
4. O usuário preenche o prompt com o comando `/Atividades`.
6. O usuário preenche o campo extra do prompt com o ID da matéria que deseja visualizar.
7. O bot responde ao usuário com uma lista de suas atividades pendentes, priorizando aquelas com prazos mais próximos.

## 3. Fluxos Alternativos

Não há fluxos alternativos para este caso de uso.

## 4. Subfluxos

Não há subfluxos para este caso de uso.

## 5. Cenários Chave

Este caso de uso é acionado quando o usuário interage com o sistema para executar o comando de listagem de atividades no bot.

## 6. Condições Prévias

- O usuário deve ter uma conta no Discord.
  - Consequentemente, o usuário deve estar logado no Discord em seu dispositivo.
- O usuário deve estar no mesmo ambiente que o bot, seja um servidor compartilhado ou nas mensagens privadas com o bot.
  - O bot pode estar presente em um ou mais servidores, e o usuário deve compartilhar um desses ambientes para poder interagir com ele.
- O usuário deve ter vinculado sua conta do Classroom com o Discord, para que o bot possa acessar suas informações de atividades.
  - Este vínculo será realizado através de um método a ser definido, possivelmente por um comando adicional.

## 7. Condições Posteriores

Não há condições posteriores específicas para este caso de uso.

## 8. Pontos de Extensão

Não há pontos de extensão para este caso de uso.

## 9. Requisitos Especiais

Os requisitos especiais estão disponíveis no documento [Especificação Suplementar](rup_supdoc.md).

## 10. Informações Adicionais

Não há informações adicionais para este caso de uso.
