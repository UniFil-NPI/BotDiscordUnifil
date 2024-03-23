									Bot de Discord
# Especificação de Caso de Uso: Realizar Comando
 
#### Histórico da Revisão
| Data   | Versão       | Descrição  |  Autor  |
| :---------- | :--------- | :-------------------------------- | :-------------------------------- |
| 18/03/2024 | 1.0 | Criação do Doc.| Gabriel Zanoni(@GbrielZanoni) |
| 19/03/2024 | 1.1 | Conversão para M.D| Gabriel Zanoni(@GbrielZanoni)|


# Índice

- [1. Breve Descrição](#brevedesc)	
- [2. Fluxo Básico de Eventos](#fluxo) 
- [3. Fluxos Alternativos](#fluxoa)
- [4. Subfluxos](#subfluxos)	
- [5. Cenários Chave](#cenarios) 
- [6. Condições Prévias](#condicoes)
- [7. Condições Posteriores](#condicoespos)
- [8. Pontos de Extensão](#pontosext)
- [9. Requisitos Especiais](#requisitos)
- [10. Informações Especiais](#informacoes)


# Espécificação Complementar

## <a name="brevedesc"></a> 1. Breve Descrição 

Este Caso de uso tem como seu objetivo o prompt inicial para o Bot retornar as informações desejadas pelo usuário

## <a name="fluxo"></a> 2. Fluxo Básico de Eventos

1. O usuário loga no Discord
2. O usuário entra no chat específico do servidor do Discord ou em uma conversa particular com o Bot
3. O usuário usa o prompt de chat e digita um comando, que se inicia com "/"
4. O usuário preenche o prompt com o comando desejado. 
5. O bot responde o usuário com as informações adicionais da mensagem desejada. 

## <a name="avaliandoproblema"></a> 3. Fluxos Alternativos

- Verificar Nota
  - O Aluno verifica uma nota de uma matéria específica. Para isto deverá especificar (selecionando de uma lista providenciada pelo Bot, além das atividades já retornadas pelos professores com nota)
- Verificar Material
  - O Aluno verifica um material específico de uma matéria. Para isto deverá especificar (selecionando qual matéria deseja acessar)
- Verificar Posts
  - O aluno verifica as notícias no Quadro de Notícias de uma matéria específica (após o Bot disponibilizar as Matérias disponíveis do Aluno que não estão arquivadas e que ele faz parte)
- Verificar Trabalho
  - O aluno verifica TODOS os trabalhos disponíveis para ele entregar. O Bot irá disponibilizar apenas os que estão pendentes, não os que não foram entregues ou que já tiveram seu tempo expirado.
- Verificar Agenda
  - O aluno verifica uma visão ampla da agenda de atividades de uma unidade curricular específica, disponibilizada pelo Bot, ou de todas as unidades curriculares que estão disponíveis para o aluno naquele momento.

## <a name="subfluxos"></a> 4. Subfluxos
> Não há
## <a name="cenarios"></a> 5. Cenários Chave

> Este caso de uso é acionado no momento em que o Ator (usuário) interage com o sistema, com a intenção de realizar um comando no bot para interagir com o google sala de aula. 

## <a name="condicoes"></a> 6. Condições Prévias
-  É Necessário que o usuário tenha uma conta de Discord
   - Automáticamente, que esteja logado nela em seu dispositivo tecnológico (mobile ou não)
-  É necessário que o usuário esteja no mesmo ambiente que o Bot, seja ele um servidor compartilhado ou 		esteja nas mensagens particulares do Bot
   - O bot poderá ser distribuido em um ou mais servidores. O usuário deverá compartilhar um ambiente com ele para poder usa-lo
-  É necessário que o 	usuário tenha linkado a sua conta do Classroom com a do Discord, para que o 	Bot saiba exatamente das suas informações.
    - Isto será feito utilizando um método não-definido, que provavelmente será um comando adicional.
## <a name="condicoespos"></a>  7. Condições Posteriores

> Não há

## <a name="pontosext"></a>  8. Pontos de Extensão

> Não há

## <a name="requisitos"></a> 9. Requisitos Especiais
> Disponíveis no documento [Especificação Suplementar](rup_supdoc.md)

## <a name="informacoes"></a> 10. Informaçõse Adicionais

![O fluxograma do Caso de Uso](https://i.imgur.com/7NNdZcd.png)