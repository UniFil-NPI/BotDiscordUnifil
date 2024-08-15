# Especificação de Caso de Uso: Verificar Pendência

#### Histórico da Revisão
| Data       | Versão | Descrição                   | Autor                             |
|------------|--------|-----------------------------|-----------------------------------|
| 20/03/2024 | 1.0    | Criação do Doc.              | Gabriel Zanoni (@GbrielZanoni)    |

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

O caso de uso "Verificar Pendência" tem como objetivo verificar as pendências acadêmicas de um aluno, como atividades e tarefas que ainda precisam ser entregues. O processo é baseado no email estudantil do aluno, que é obtido através de um endpoint fornecido pelo stakeholder. Este caso de uso é executado automaticamente por uma tarefa agendada que roda diariamente.

## 2. Fluxo Básico de Eventos

1. **Pegar ID:**
   - O sistema obtém o Discord ID do aluno.

2. **Obter Email Estudantil:**
   - O sistema envia o Discord ID para o endpoint da API fornecido pelo stakeholder.
   - O sistema recebe o email estudantil associado ao Discord ID.

3. **Verificar Email:**
   - O sistema verifica se o email estudantil retornado é válido e está associado a uma conta do Google Classroom.

4. **Verificar Classrooms:**
   - O sistema consulta as salas de aula (classrooms) associadas ao email do aluno.

5. **Verificar Matérias:**
   - O sistema recupera a lista de matérias (disciplinas) em que o aluno está inscrito dentro das salas de aula encontradas.

6. **Verificar Atividades e Pendências:**
   - O sistema verifica todas as atividades associadas às matérias.
   - O sistema identifica as atividades que ainda não foram entregues e as que estão próximas da data limite.
   - As pendências são compiladas e preparadas para notificação ou consulta pelo aluno.

## 3. Fluxos Alternativos

- **Erro ao Obter Email:**
  - Se o endpoint não conseguir retornar o email estudantil, o sistema deve registrar o erro e tentar novamente na próxima execução da tarefa agendada.

- **Aluno Não Inscrito em Nenhuma Matéria:**
  - Se o aluno não estiver inscrito em nenhuma matéria, o sistema deve registrar essa informação e notificar o aluno, se possível, informando que não há pendências devido à ausência de inscrição em disciplinas.

## 4. Subfluxos

1. **Validar Email:**
   - Verificação adicional para garantir que o email pertence a um aluno registrado e que está associado ao Google Classroom.

2. **Compilar Pendências:**
   - Organizar as atividades pendentes em uma lista estruturada para notificação ou exibição ao aluno.

## 5. Cenários Chave

Este caso de uso é acionado diariamente por uma tarefa agendada, que verifica automaticamente as pendências acadêmicas de cada aluno com base em seu email estudantil associado ao Discord ID.

## 6. Condições Prévias

- O aluno deve ter um Discord ID associado ao seu email estudantil.
- O endpoint da API fornecido pelo stakeholder deve estar operacional e capaz de retornar o email estudantil corretamente.
- O aluno deve estar registrado no Google Classroom com o email fornecido.

## 7. Condições Posteriores

- As pendências do aluno serão compiladas e notificadas ou estarão disponíveis para consulta.
- O sistema estará pronto para a próxima execução da tarefa agendada.

## 8. Pontos de Extensão

- Possibilidade de notificar o aluno automaticamente sobre pendências críticas (atividades com prazos muito próximos).

## 9. Requisitos Especiais

- Disponíveis no documento [Especificação Suplementar](rup_supdoc.md)

## 10. Informações Especiais

- Este caso de uso é parte de uma tarefa automatizada que roda diariamente para garantir que os alunos estejam sempre informados sobre suas pendências acadêmicas.
