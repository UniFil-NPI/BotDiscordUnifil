# Especificação de Caso de Uso: Realizar Comando

#### Histórico da Revisão
| Data       | Versão | Descrição                              | Autor                             |
|------------|--------|----------------------------------------|-----------------------------------|
| 18/03/2024 | 1.0    | Criação do Documento                   | Gabriel Zanoni (@GbrielZanoni)    |
| 09/03/2024 | 1.1    | Conversão para Markdown                | Gabriel Zanoni (@GbrielZanoni)    |
| 24/10/2024 | 1.2    | Atualização com centralização de comandos | Gabriel Zanoni (@GbrielZanoni) |

# Índice

- [1. Breve Descrição](#introducao)	
- [2. Fluxo Básico de Eventos](#fluxo-basico-de-eventos) 
- [3. Fluxos Alternativos](#fluxos-alternativos)
- [4. Subfluxos](#subfluxos)	
- [5. Cenários Chave](#cenarios-chave) 
- [6. Condições Prévias](#condicoes-previas)
- [7. Condições Posteriores](#condicoes-posteriores)
- [8. Pontos de Extensão](#pontos-de-extensao)
- [9. Requisitos Especiais](#requisitos-especiais)
- [10. Informações Especiais](#informacoes-especiais)

# Especificação Complementar

## <a name="introducao"></a> 1. Breve Descrição

Este Caso de Uso descreve a funcionalidade do comando geral "Realizar Comando", que centraliza e abrange os seguintes comandos do bot no Discord:
- **Notificar**: liga ou desliga as notificações de pendências acadêmicas.
- **Calendário**: exibe uma visão ampla das atividades do usuário.
- **Tarefas**: exibe as atividades recentes e pendentes do usuário.
- **Matérias**: lista todas as matérias cadastradas e ativas do usuário.

O objetivo é permitir que o usuário utilize esses comandos de forma unificada e eficiente.

## <a name="fluxo-basico-de-eventos"></a> 2. Fluxo Básico de Eventos

1. O usuário faz login no Discord.
2. O usuário acessa o chat específico do servidor ou mensagens privadas do bot.
3. O usuário digita um comando iniciado por "/" seguido de um dos seguintes comandos: `/Notificar`, `/Calendário`, `/Tarefas`, ou `/Matérias`.
4. O bot processa o comando e responde ao usuário com as informações solicitadas.

## <a name="fluxos-alternativos"></a> 3. Fluxos Alternativos

### 3.1. Comando Notificar
   - O usuário utiliza o comando `/Notificar` para ativar ou desativar as notificações de pendências acadêmicas.
   - O bot confirma se as notificações foram ativadas ou desativadas com sucesso.

### 3.2. Comando Calendário
   - O usuário utiliza o comando `/Calendário` para exibir uma visão ampla das atividades de uma unidade curricular específica ou de todas as unidades disponíveis.
   - O bot retorna a agenda com as atividades organizadas por data.

### 3.3. Comando Tarefas
   - O usuário utiliza o comando `/Tarefas` para visualizar todas as atividades pendentes.
   - O bot exibe as atividades que ainda não foram concluídas ou que estão com o prazo próximo.

### 3.4. Comando Matérias
   - O usuário utiliza o comando `/Matérias` para listar todas as matérias em que está inscrito.
   - O bot exibe uma lista com as matérias ativas do usuário.

## <a name="subfluxos"></a> 4. Subfluxos

Não há subfluxos adicionais.

## <a name="cenarios-chave"></a> 5. Cenários Chave

Este caso de uso é acionado quando o usuário interage com o sistema para executar qualquer um dos quatro comandos: Notificar, Calendário, Tarefas ou Matérias. Dependendo do comando, o bot realiza a ação solicitada e retorna a resposta apropriada ao usuário.

## <a name="condicoes-previas"></a> 6. Condições Prévias

- O usuário deve ter uma conta no Discord.
  - Consequentemente, o usuário deve estar logado no Discord.
- O usuário deve estar no mesmo ambiente que o bot (um servidor compartilhado ou nas mensagens privadas com o bot).
- O usuário deve ter vinculado sua conta do Classroom com o Discord, para que o bot possa acessar suas informações acadêmicas.

## <a name="condicoes-posteriores"></a> 7. Condições Posteriores

- O bot deve atualizar as preferências do usuário, se aplicável (por exemplo, no caso de ativação/desativação de notificações).

## <a name="pontos-de-extensao"></a> 8. Pontos de Extensão

- Futuramente, o bot poderá ter comandos adicionais, como personalização de notificações ou novos comandos para informações acadêmicas mais detalhadas.

## <a name="requisitos-especiais"></a> 9. Requisitos Especiais

Os requisitos especiais estão disponíveis no documento [Especificação Suplementar](rup_supdoc.md).

## <a name="informacoes-especiais"></a> 10. Informações Especiais

### Comando: **/Notificar**
- **Descrição**: Liga ou desliga as notificações automáticas do bot, informando o usuário sobre suas pendências acadêmicas, como atividades próximas do vencimento.
- **Funcionalidade**:
  - Quando ativado, o usuário recebe notificações periódicas sobre prazos importantes e tarefas pendentes.
  - Quando desativado, o usuário não recebe notificações até que ative novamente.
- **Resultado**: O bot atualiza o status de notificação do usuário e confirma a alteração através de uma mensagem, informando se as notificações foram habilitadas ou desabilitadas.

### Comando: **/Calendário**
- **Descrição**: Exibe uma visão ampla das atividades programadas no calendário acadêmico do usuário, agrupadas por unidade curricular ou por todas as matérias.
- **Funcionalidade**:
  - O usuário pode consultar atividades futuras, como prazos de entrega, provas e eventos acadêmicos.
  - O comando pode ser utilizado com uma unidade curricular específica ou para exibir todas as atividades relacionadas às matérias inscritas.
- **Resultado**: O bot retorna uma lista detalhada de todas as atividades, incluindo datas e descrições, organizadas por ordem cronológica.

### Comando: **/Tarefas**
- **Descrição**: Lista todas as tarefas pendentes do usuário, priorizando aquelas com prazos mais próximos.
- **Funcionalidade**:
  - O usuário visualiza as atividades que ainda estão dentro do prazo para entrega.
  - O foco é em tarefas recentes, ajudando o usuário a gerenciar suas pendências de curto prazo.
- **Resultado**: O bot exibe uma lista de tarefas pendentes com datas de vencimento e o status atual (não entregue, próxima do prazo, etc.).

### Comando: **/Matérias**
- **Descrição**: Lista todas as matérias cadastradas e ativas do usuário, conforme suas inscrições no Classroom.
- **Funcionalidade**:
  - O usuário pode visualizar as matérias em que está matriculado no momento.
  - Isso ajuda o usuário a ter uma visão clara das disciplinas ativas que ele está cursando.
- **Resultado**: O bot retorna uma lista com todas as matérias ativas, incluindo nome e detalhes das unidades curriculares.

![O fluxograma do Caso de Uso](https://i.imgur.com/tgMEn1J.png)
