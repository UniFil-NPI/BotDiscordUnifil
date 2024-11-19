# Especificação de Caso de Uso: Notificar Usuário

#### Histórico da Revisão
| Data       | Versão | Descrição                   | Autor                             |
|------------|--------|-----------------------------|-----------------------------------|
| 22/08/2024 | 1.0    | Criação do Doc.             | Gabriel Zanoni (@GbrielZanoni)    |
| 19/10/2024 | 1.0    | Correção                    | Gabriel Zanoni (@GbrielZanoni)    |

# Índice

- [1. Breve Descrição](#1-breve-descrição)
- [2. Fluxo Básico de Eventos](#2-fluxo-básico-de-eventos)
- [3. Fluxos Alternativos](#3-fluxos-alternativos)
- [4. Subfluxos](#4-subfluxos)
- [5. Cenários Chave](#5-cenários-chave)
- [6. Condições Prévias](#6-condições-prévias)
- [7. Condições Posteriores](#7-condições-posteriores)
- [8. Pontos de Extensão](#8-pontos-de-extensão)
- [9. Requisitos Especiais](#9-requisitos-especiais)
- [10. Informações Especiais](#10-informações-especiais)

---

## 1. Breve Descrição

O caso de uso "Notificar Usuário" tem como objetivo enviar notificações para o usuário sobre suas pendências, matérias e outros assuntos relacionados ao Google Classroom. O caso de uso levará em consideração que ele irá enviar uma mensagem formatada para o usuário com base no conteúdo, formulando diferentes páginas com o meio para a sua navegação. 

# Especificação de Caso de Uso: Notificar Usuário

## Fluxo Básico de Eventos

1. **Obter Informação**
   - O sistema identifica o contexto da notificação (ex.: pendências, calendário de atividades ou matérias disponíveis).
   - As informações são recuperadas e processadas.
   - A classe `Paginator` é utilizada para formatar os dados em uma mensagem estruturada e legível para o usuário.
   - Exemplos de conteúdos formatados:
     - **Matérias**: Lista de matérias disponíveis e suas descrições.
     - **Pendências**: Atividades pendentes com título, descrição e prazos formatados.
     - **Calendário**: Eventos e tarefas ordenados por data.

2. **Notificar Usuário com Base no Conteúdo**
   - A mensagem é preparada com base no conteúdo recuperado.
   - O sistema verifica o método de notificação apropriado (mensagem efêmera ou DM no Discord).

3. **Enviar uma Notificação Efêmera ou DM**
   - **Notificação Efêmera**:
     - Se o comando foi executado diretamente pelo usuário em um canal público, uma mensagem efêmera é enviada (visível apenas para o usuário).
   - **Mensagem Direta (DM)**:
     - Se o fluxo de notificação é automático ou acionado por outro contexto, a mensagem é enviada diretamente como DM ao usuário.
   - Caso ocorra erro ao enviar a DM (ex.: o usuário bloqueou o bot), o erro é registrado, e o sistema tentará reenviar posteriormente.

## 3. Fluxos Alternativos

- **Erro ao Enviar Notificação:**
  - Se ocorrer um erro ao tentar enviar a notificação (por exemplo, o usuário bloqueou o bot), o sistema registra o erro e tenta novamente na próxima execução ou de acordo com a política de reenvio definida.

## 4. Subfluxos

1. **Preparar Notificação:**
   - Se as notificações estiverem ativadas, o sistema compila as informações relevantes (como pendências ou eventos) em uma mensagem formatada para ser enviada ao usuário.

## 5. Cenários Chave

Este caso de uso é acionado por outros casos de uso que precisam do envio da informação para o usuário, enviando para ele o conteúdo bruto que será formatado por sí e pela classe do Paginator.

## 6. Condições Prévias

- O usuário deve ter interagido previamente com o bot e utilizado um de seus comandos
- O usuário poderá ter configurado suas preferências de notificações para receber uma notificação automática.
- O Bot deverá ter acesso ao canal ou meio na qual o usuário realizou o comando
- O bot deve ter permissão para enviar mensagens privadas ao usuário no Discord caso ele deseje receber uma notificação automática.

## 7. Condições Posteriores

- Se as notificações forem enviadas, o usuário será informado das pendências ou eventos importantes.
- Se as notificações estiverem desativadas, o sistema não tomará nenhuma ação adicional até a próxima verificação.

## 8. Pontos de Extensão

- Implementação de notificações personalizadas, onde o usuário pode escolher o tipo de eventos ou pendências que deseja ser notificado.

## 9. Requisitos Especiais

- Disponíveis no documento [Especificação Suplementar](rup_supdoc.md)

## 10. Informações Especiais

- Este caso de uso abrange tanto o envio de mensagens formatadas para o bot como qualquer notificação. Que será formatada devidamente e enviada, tanto automáticamente como pelo resultado de um comando do usuário, indiferente do conteúdo.