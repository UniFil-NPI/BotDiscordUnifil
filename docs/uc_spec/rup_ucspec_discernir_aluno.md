# Bot de Discord

# Especificação de Caso de Uso: Realizar Comando

#### Histórico da Revisão
| Data       | Versão | Descrição           | Autor                            |
|------------|--------|---------------------|----------------------------------|
| 18/03/2024 | 1.0    | Criação do Doc.      | Gabriel Zanoni (@GbrielZanoni)   |
| 09/03/2024 | 1.1    | Conversão para M.D   | Gabriel Zanoni (@GbrielZanoni)   |
| 15/03/2024 | 1.2    | Integração API de ID | Gabriel Zanoni (@GbrielZanoni)   |

# Índice

- [1. Breve Descrição](#introducao)	
- [2. Fluxo Básico de Eventos](#perfil) 
- [3. Fluxos Alternativos](#avaliandoproblema)
- [4. Subfluxos](#ambiente)	
- [5. Cenários Chave](#recapitulacao) 
- [6. Condições Prévias](#entradas)
- [7. Condições Posteriores](#avaliandosolucao)
- [8. Pontos de Extensão](#avaliandooportunidade)
- [9. Requisitos Especiais](#avaliandoconfiabilidade)
- [10. Informações Especiais](#resumoanalista)

# Especificação Complementar

## <a name="introducao"></a> 1. Breve Descrição 

Este Caso de Uso tem como objetivo permitir que o Bot de Discord receba comandos do usuário e retorne as informações desejadas. Especificamente, ele inclui a funcionalidade de obter o email estudantil de um usuário baseado em seu Discord ID, utilizando um endpoint de API fornecido pelo stakeholder.

## <a name="perfil"></a> 2. Fluxo Básico de Eventos

1. O usuário loga no Discord.
2. O usuário entra no chat específico do servidor do Discord ou nas mensagens privadas do Bot.
3. O usuário usa o prompt de chat e digita um comando começado com "/".
4. O usuário preenche o prompt com o comando desejado.
5. O bot faz uma chamada ao endpoint da API utilizando o Discord ID do usuário para obter o email estudantil associado.
6. O bot responde ao usuário com as informações adicionais ou com a mensagem desejada.

## <a name="avaliandoproblema"></a> 3. Fluxos Alternativos

- **Verificar Materias**
  - O aluno verifica todas as suas matérias disponíveis.
  
- **Verificar Atividade**
  - O aluno verifica TODOS os trabalhos disponíveis para ele entregar. O Bot disponibiliza apenas os que estão pendentes, não os que já foram entregues ou que já tiveram seu tempo expirado.
  
- **Verificar Agenda**
  - O aluno verifica uma visão ampla da agenda de atividades de uma unidade curricular específica, ou de todas as unidades curriculares que estão disponíveis para o aluno naquele momento.

## <a name="ambiente"></a> 4. Subfluxos
Não há

## <a name="recapitulacao"></a> 5. Cenários Chave

Este caso de uso é acionado no momento em que o ator (usuário) interage com o sistema, com a intenção de realizar um comando no bot. 

## <a name="entradas"></a> 6. Condições Prévias

- É necessário que o usuário tenha uma conta de Discord.
  - Automaticamente, que esteja logado nela em seu dispositivo tecnológico (mobile ou desktop).
- É necessário que o usuário esteja no mesmo ambiente que o Bot, seja ele um servidor compartilhado ou nas mensagens privadas do Bot.
  - O bot pode estar distribuído em um ou mais servidores. O usuário deve compartilhar um ambiente com ele para poder usá-lo.
- É necessário que o usuário tenha vinculado sua conta do Classroom com a do Discord, para que o Bot saiba exatamente quais informações exibir.
  - A vinculação será feita através de um endpoint de API fornecido pelo stakeholder, onde o Discord ID do usuário será utilizado para recuperar o email estudantil.

## <a name="avaliandosolucao"></a> 7. Condições Posteriores

> Não há

## <a name="avaliandooportunidade"></a> 8. Pontos de Extensão

> Não há

## <a name="avaliandoconfiabilidade"></a> 9. Requisitos Especiais

> Disponíveis no documento [Especificação Suplementar](rup_supdoc.md)

## <a name="resumoanalista"></a> 10. Informações Especiais

![O fluxograma do Caso de Uso](https://i.imgur.com/7NNdZcd.png)
