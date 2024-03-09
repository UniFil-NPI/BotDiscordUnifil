# Visão

#### Histórico da Revisão
| Data   | Versão       | Descrição  |  Autor  |
| :---------- | :--------- | :-------------------------------- | :-------------------------------- |
| 05/03/2024 | 1.0 | Criação do Doc.| Gabriel Zanoni |
| 09/03/2024 | 1.1 | Conversão para M.D| Gabriel Zanoni |

## 1.Introdução

## 2.Posicionamento


## 2.1 Instrução do Problema

| O problema de   | afeta       | o impacto do qual é  |  uma solção bem-sucedidade  |
| :---------- | :--------- | :-------------------------------- | :-------------------------------- |
| Falta de comunicação entre plataforma e aluno | Alunos   | Imprevistos por  parte dos alunos, que por sua vez não usam seu e-mail tanto assim.| Uma maneira do aluno ser notificado via Discord automaticamente, lembrando-lhe de suas atividades e enviando mensagens de professores sobre materiais ou aviso. |



## 2.2 Instrução sobre a Posição do Produto		
Para	Aluno usuário de Discord
Que	Estudantes da UniFil, usuários do Google Sala-de-Aula 
O Bot	 é um sistema de conciliação do usuário do Discord e do Sala-de-Aula
Que	faz a conciliação automática entre o Google Sala de Aula e o Discord.
Diferente de	Uma API que se conecta com o classroom e notifica o usuário no discord
Nosso produto	O diferencial de conectar diretamente o aluno específico com o seu nome e matrícula, para deixar explícito para o professor e outros alunos. 
## 3.Descrições do Envolvido

## 3.1 Resumo do Envolvido

 Nome	Descrição	Responsabilidades
Aluno	O aluno é o usuário do bot, ele será notificado quando o professor realiza algum envio, além de ser lembrado das datas de envio e das pendências	Ele deverá linkar o seu usuário do discord com as credênciais do classroom para ser identificado pelo sistema.
Professor	O professor que usa o bot indiretamente após enviar ou utilizar o classoom	Responsável pelo envio das tarefas, avisos e notícias para o aluno
Desenvolvedor	Desenvolve os sistemas necessários pelo BOT	Responsável pela correção dos erros encontrados, pela criação dos sistemas, pelo desenvolvimento do BOT em geral

## 3.2 Ambiente do Usuário

A plataforma web estará acessível através de uma URL, permitindo que os usuários acessem de qualquer computador com conexão à internet. O aplicativo mobile estará disponível para download na Play Store e Apple Store, garantindo acesso conveniente em smartphones, com suporte para versões mais recentes do Android.

## 4.Visão Geral do Produto
## 4.1Perspectiva do Produto

O produto é inteiramente autônomo, não-dependente de uma intervenção da empresa ou coisa assim. Ele se relacionará com um banco de dados para a verificação de dados do usuário junto a uma API que se comunica com o google Classroom

## 4.2 Premissas e Dependências

O sistema dependen apenas de uma internet e um dispositivo tecnológico, qualquer Sistema Operacional com acesso ao aplicativo Discord e a um navegador Web conseguirá utilizar o bot, tendo em vista que o usuário compartilha um servidor junto ao bot.

## 4.3 Necessidades e Recursos

Necessidade	Prioridade	Recursos	Liberação Planejada
Notificar Usuário	Alta	Interface em Python	Primeira Versão
API interativa	Alta	JavaScript ou Python	Primeira Versão
Interface do BOT	Alta	Python	Primeira Versão
Cadastro de Estudante	Alta	Interface SQL	Primeira versão

## 4.4 Alternativas e Competição
Como se trata de uma interface única com integração aos alunos de uma determinada empresa, não existe nada parecido no mercado. Apenas APIs interativas que juntam Discord & Classroom.

https://pipedream.com/apps/google-classroom/integrations/discord-bot

## 5.Outros Requisitos do Produto
### Para o desenvolvimento do sistema foram adotados frameworks estáveis e que possuem desenvolvimento contínuo.
#### O projeto é apenas acessado no Aplicativo ‘Discord’, por qualquer pessoa que, além de ter acesso direto ao servidor, possuir uma conta institucional e ser aluno. 
#### Disponibilidade: 
- O sistema deverá estar disponível em qualquer horário, todos os dias da semana.
#### Usabilidade: 
- O Bot será disponível através do aplicativo, a comunicação entre usuário aplicativo será através de prompts visuais e comandos feitos no bate-papo.
#### Manutenção: 
- O sistema será documentado, seguindo alguns artefatos da UML. Bem como a utilização de documentos acessórios para o fácil entendimento das funcionalidades e decisões de arquitetura.