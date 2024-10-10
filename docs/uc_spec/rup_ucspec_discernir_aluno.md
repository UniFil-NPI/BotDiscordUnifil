# Especificação de Caso de Uso: Discernir Aluno

#### Histórico da Revisão
| Data       | Versão | Descrição           | Autor                            |
|------------|--------|---------------------|----------------------------------|
| 10/10/2024 | 1.0    | Criação e Importação| Gabriel Zanoni (@GbrielZanoni)   |

# Índice

- [1. Breve Descrição](#introducao)	
- [2. Fluxo Básico de Eventos](#fluxo-basico) 
- [3. Fluxos Alternativos](#fluxos-alternativos)
- [4. Subfluxos](#subfluxos)	
- [5. Cenários Chave](#cenarios-chave) 
- [6. Condições Prévias](#condicoes-previas)
- [7. Condições Posteriores](#condicoes-posteriores)
- [8. Pontos de Extensão](#pontos-de-extensao)
- [9. Requisitos Especiais](#requisitos-especiais)
- [10. Informações Especiais](#informacoes-especiais)

## <a name="introducao"></a> 1. Breve Descrição 

Este Caso de Uso tem como objetivo permitir que o Bot de Discord receba comandos do usuário e retorne as informações desejadas. Especificamente, ele inclui a funcionalidade de obter o email estudantil de um usuário baseado em seu Discord ID, utilizando um endpoint de API fornecido pelo stakeholder.

## <a name="fluxo-basico"></a> 2. Fluxo Básico de Eventos

1. O usuário loga no Discord.
2. O usuário entra no chat específico do servidor do Discord ou nas mensagens privadas do Bot.
3. O usuário usa o prompt de chat e digita um comando começado com "/".
4. O usuário preenche o prompt com o comando desejado.
5. O bot faz uma chamada ao endpoint da API utilizando o Discord ID do usuário para obter o email estudantil associado.
6. O bot responde ao usuário com as informações adicionais ou com a mensagem desejada.

## <a name="fluxos-alternativos"></a> 3. Fluxos Alternativos

- **Verificar Materias**
  - O aluno verifica todas as suas matérias disponíveis.
  
- **Verificar Atividade**
  - O aluno verifica TODOS os trabalhos disponíveis para ele entregar. O Bot disponibiliza apenas os que estão pendentes, não os que já foram entregues ou que já tiveram seu tempo expirado.
  
- **Verificar Agenda**
  - O aluno verifica uma visão ampla da agenda de atividades de uma unidade curricular específica, ou de todas as unidades curriculares que estão disponíveis para o aluno naquele momento.

## <a name="subfluxos"></a> 4. Subfluxos
Não há

## <a name="cenarios-chave"></a> 5. Cenários Chave

Este caso de uso é acionado no momento em que o ator (usuário) interage com o sistema, com a intenção de realizar um comando no bot. 

## <a name="condicoes-previas"></a> 6. Condições Prévias

- É necessário que o usuário tenha uma conta de Discord.
  - Automaticamente, que esteja logado nela em seu dispositivo tecnológico (mobile ou desktop).
- É necessário que o usuário esteja no mesmo ambiente que o Bot, seja ele um servidor compartilhado ou nas mensagens privadas do Bot.
  - O bot pode estar distribuído em um ou mais servidores. O usuário deve compartilhar um ambiente com ele para poder usá-lo.
- É necessário que o usuário tenha vinculado sua conta do Classroom com a do Discord, para que o Bot saiba exatamente quais informações exibir.
  - A vinculação será feita através de um endpoint de API fornecido pelo stakeholder, onde o Discord ID do usuário será utilizado para recuperar o email estudantil.

## <a name="condicoes-posteriores"></a> 7. Condições Posteriores

> Não há

## <a name="pontos-de-extensao"></a> 8. Pontos de Extensão

> Não há

## <a name="requisitos-especiais"></a> 9. Requisitos Especiais

> Disponíveis no documento [Especificação Suplementar](rup_supdoc.md)

## <a name="informacoes-especiais"></a> 10. Informações Especiais

![O fluxograma do Caso de Uso](https://i.imgur.com/7NNdZcd.png)
