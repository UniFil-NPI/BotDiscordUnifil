# Especificação de Caso de Uso: Notificar Usuário

#### Histórico da Revisão
| Data       | Versão | Descrição                   | Autor                             |
|------------|--------|-----------------------------|-----------------------------------|
| 22/08/2024 | 1.0    | Criação do Doc.              | Gabriel Zanoni (@GbrielZanoni)    |

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

O caso de uso "Notificar Usuário" tem como objetivo enviar notificações para o usuário sobre suas pendências ou eventos importantes relacionados ao Google Classroom. O envio das notificações é condicionado pelas preferências de notificações do usuário, que podem estar ativadas ou desativadas nas configurações do bot.

## 2. Fluxo Básico de Eventos

1. **Verificar Preferências de Notificação:**
   - O sistema verifica as preferências de notificações do usuário armazenadas no bot.

2. **Notificações Ativadas:**
   - Se as notificações estiverem ativadas, o sistema prepara e envia uma notificação ao usuário sobre suas pendências ou eventos importantes.
   - A notificação é enviada via mensagem privada (DM) no Discord.

3. **Notificações Desativadas:**
   - Se as notificações estiverem desativadas, o sistema não envia nenhuma notificação e finaliza o processo.

## 3. Fluxos Alternativos

- **Erro ao Enviar Notificação:**
  - Se ocorrer um erro ao tentar enviar a notificação (por exemplo, o usuário bloqueou o bot), o sistema registra o erro e tenta novamente na próxima execução ou de acordo com a política de reenvio definida.

## 4. Subfluxos

1. **Preparar Notificação:**
   - Se as notificações estiverem ativadas, o sistema compila as informações relevantes (como pendências ou eventos) em uma mensagem formatada para ser enviada ao usuário.

## 5. Cenários Chave

Este caso de uso é acionado quando o sistema detecta eventos importantes ou pendências acadêmicas que precisam ser notificadas ao usuário e verifica se as notificações estão ativadas nas preferências do bot.

## 6. Condições Prévias

- O usuário deve ter interagido previamente com o bot e configurado suas preferências de notificações.
- O bot deve ter permissão para enviar mensagens privadas ao usuário no Discord.

## 7. Condições Posteriores

- Se as notificações forem enviadas, o usuário será informado das pendências ou eventos importantes.
- Se as notificações estiverem desativadas, o sistema não tomará nenhuma ação adicional até a próxima verificação.

## 8. Pontos de Extensão

- Implementação de notificações personalizadas, onde o usuário pode escolher o tipo de eventos ou pendências que deseja ser notificado.

## 9. Requisitos Especiais

- Disponíveis no documento [Especificação Suplementar](rup_supdoc.md)

## 10. Informações Especiais

- Este caso de uso depende diretamente das preferências de notificação configuradas pelo usuário no bot. É importante garantir que essas preferências sejam fáceis de configurar e alterar.
