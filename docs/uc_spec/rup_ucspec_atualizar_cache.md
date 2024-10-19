# Especificação de Caso de Uso: Atualizar Cache

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

O caso de uso **"Atualizar Cache"** descreve o processo de atualização periódica do cache de dados relacionados aos cursos, tarefas, alunos e pendências do Google Classroom. Esta tarefa é executada automaticamente por um sistema agendado que garante que o cache mantenha dados atualizados para reduzir o número de chamadas à API e melhorar o desempenho.

## 2. Fluxo Básico de Eventos

1. **Iniciar Atualização**:
   - O bot ou sistema inicia automaticamente a tarefa de atualização do cache em intervalos regulares.

2. **Obter Cursos**:
   - O sistema tenta recuperar a lista de cursos do cache.
   - Se os cursos não estiverem no cache ou estiverem desatualizados, o sistema solicita os dados da API do Google Classroom.

3. **Obter Alunos de Cada Curso**:
   - Para cada curso obtido, o sistema verifica os alunos associados no cache.
   - Se as informações dos alunos estiverem desatualizadas ou ausentes, a API do Google Classroom é consultada para obter a lista de alunos.

4. **Obter Tarefas de Cada Curso**:
   - O sistema verifica se as tarefas de cada curso estão no cache.
   - Se as informações estiverem desatualizadas ou ausentes, as tarefas são obtidas diretamente da API.

5. **Atualizar Pendências**:
   - O sistema verifica as pendências de atividades associadas a cada aluno e curso.
   - Caso não estejam presentes ou atualizadas no cache, o sistema faz a requisição para a API e armazena os resultados no cache.

6. **Salvar Dados no Cache**:
   - Os dados obtidos (cursos, alunos, tarefas e pendências) são armazenados ou atualizados no cache com um tempo de expiração pré-definido.

7. **Finalizar Atualização**:
   - O sistema finaliza o processo e se prepara para a próxima execução agendada.

## 3. Fluxos Alternativos

- **Falha ao Acessar a API do Google Classroom**:
   - Caso a API do Google Classroom não esteja acessível, o sistema deve registrar o erro e tentar novamente na próxima execução.
   - O sistema pode optar por manter os dados antigos no cache por mais tempo, até que a conexão com a API seja restabelecida.

- **Cache Cheio ou Inacessível**:
   - Se o cache estiver indisponível ou cheio, o sistema deve registrar a falha e continuar o processo sem cache até que a situação seja resolvida.

## 4. Subfluxos

1. **Validar Dados no Cache**:
   - Verificar se os dados no cache estão dentro do tempo de validade antes de fazer uma nova solicitação à API.
   
2. **Consultar API em Caso de Falha no Cache**:
   - Quando os dados não estão disponíveis no cache, o sistema consulta diretamente a API do Google Classroom para obter as informações mais recentes.

## 5. Cenários Chave

- O caso de uso é executado periodicamente (por exemplo, a cada 30 minutos) para garantir que o cache esteja sempre atualizado com as informações mais recentes do Google Classroom.

## 6. Condições Prévias

- O sistema deve estar autenticado com sucesso na API do Google Classroom.
- O cache deve estar funcional e disponível para leitura e escrita de dados.

## 7. Condições Posteriores

- O cache é atualizado com os dados mais recentes sobre cursos, alunos, tarefas e pendências.
- O sistema estará pronto para responder às consultas de dados diretamente do cache, minimizando o número de chamadas à API.

## 8. Pontos de Extensão

- **Notificação de Erro**:
   - Caso a atualização do cache falhe, o sistema pode enviar uma notificação ao administrador ou tentar novamente em um intervalo mais curto.

## 9. Requisitos Especiais

- Disponíveis no documento [Especificação Suplementar](rup_supdoc.md).

## 10. Informações Especiais

- Este caso de uso é parte de um processo automatizado que roda periodicamente, garantindo que o cache contenha sempre dados atualizados do Google Classroom, otimizando o tempo de resposta do sistema e evitando sobrecarga de requisições à API.
