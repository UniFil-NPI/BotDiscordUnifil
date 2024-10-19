# Especificação de Caso de Uso: Notificar

#### Histórico da Revisão
| Data       | Versão | Descrição                   | Autor                             |
|------------|--------|-----------------------------|-----------------------------------|
| 19/10/2024 | 1.0    | Criação do Doc.              | Gabriel Zanoni (@GbrielZanoni)    |

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

O caso de uso **"Notificar"** descreve o processo pelo qual o usuário pode habilitar ou desabilitar as notificações periódicas enviadas pelo bot sobre pendências acadêmicas, como tarefas e prazos. As preferências de notificação são salvas em um arquivo de configuração local chamado `notifications.json`, que armazena o status de ativação/desativação por usuário.

## 2. Fluxo Básico de Eventos

1. **Solicitar Mudança de Notificação**:
   - O usuário usa um comando específico no bot para habilitar ou desabilitar as notificações periódicas.

2. **Obter Preferência Atual**:
   - O bot acessa o arquivo de configuração local `notifications.json` para verificar o estado atual das notificações do usuário (habilitadas ou desabilitadas).

3. **Alterar Status de Notificação**:
   - O bot inverte o status atual do usuário:
     - Se as notificações estiverem desabilitadas, o bot as habilita.
     - Se as notificações estiverem habilitadas, o bot as desabilita.

4. **Salvar Preferência no Arquivo**:
   - O bot atualiza o arquivo `notifications.json` com o novo status de notificação do usuário.

5. **Confirmar Alteração ao Usuário**:
   - O bot envia uma mensagem ao usuário confirmando que as notificações foram habilitadas ou desabilitadas com sucesso.

## 3. Fluxos Alternativos

- **Arquivo de Configuração Indisponível**:
   - Se o arquivo `notifications.json` estiver corrompido ou inacessível, o bot deve informar o usuário sobre o erro e tentar criar um novo arquivo ou corrigir o arquivo corrompido.

## 4. Subfluxos

1. **Verificar Preferência no Arquivo**:
   - O bot carrega o arquivo `notifications.json` e verifica se há uma entrada correspondente ao Discord ID do usuário. Se não houver, assume que as notificações estão desabilitadas por padrão.

2. **Atualizar ou Criar Preferência**:
   - Se o Discord ID do usuário ainda não existir no arquivo `notifications.json`, o bot cria uma nova entrada para esse usuário com o status de notificação atualizado (habilitado ou desabilitado).

## 5. Cenários Chave

- O usuário pode usar o comando para ativar ou desativar as notificações a qualquer momento, e o bot ajustará essa preferência no arquivo `notifications.json`.

## 6. Condições Prévias

- O arquivo de configuração `notifications.json` deve existir e estar acessível para leitura e escrita.
- O usuário deve estar registrado no sistema com um Discord ID válido.

## 7. Condições Posteriores

- A preferência de notificação do usuário é salva no arquivo `notifications.json`.
- O status de notificações periódicas do bot é atualizado de acordo com a preferência do usuário (habilitado/desabilitado).

## 8. Pontos de Extensão

- **Personalização de Notificações**:
   - Em futuras implementações, o usuário poderá configurar as notificações para recebê-las em horários ou dias específicos, ou apenas para determinados tipos de atividades (tarefas urgentes, por exemplo).

## 9. Requisitos Especiais

- Disponíveis no documento [Especificação Suplementar](rup_supdoc.md).

## 10. Informações Especiais

- O arquivo `notifications.json` armazena as preferências de notificação de cada usuário. Cada entrada contém o Discord ID do usuário e o status de notificação (habilitado ou desabilitado). Esse arquivo é essencial para que o sistema saiba se deve enviar ou não as notificações periódicas a cada usuário.
