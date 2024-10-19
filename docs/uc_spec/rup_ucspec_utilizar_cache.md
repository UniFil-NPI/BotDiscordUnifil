# Especificação de Caso de Uso: Utilizar Cache

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

O caso de uso **"Utilizar Cache"** descreve o processo pelo qual o sistema armazena e recupera dados no cache Redis para otimizar o desempenho e reduzir o número de chamadas à API do Google Classroom. O Redis Cache é utilizado para armazenar dados de cursos, alunos, tarefas e pendências, permitindo que essas informações sejam recuperadas rapidamente nas consultas subsequentes.

## 2. Fluxo Básico de Eventos

### Utilização do Cache em Diferentes Cenários:

1. **Cache de Cursos**:
   - O sistema tenta recuperar a lista de cursos do cache.
   - Se os dados estiverem no cache, o sistema os utiliza diretamente.
   - Caso contrário, faz uma chamada à API do Google Classroom, obtém a lista de cursos e armazena o resultado no cache.

2. **Cache de Alunos por Curso**:
   - Para cada curso, o sistema tenta recuperar a lista de alunos associados no cache.
   - Se os dados dos alunos estiverem no cache, eles são utilizados diretamente.
   - Se os dados não estiverem no cache, o sistema faz uma chamada à API do Google Classroom para obter os dados e os armazena no cache.

3. **Cache de Tarefas por Curso**:
   - O sistema tenta recuperar as tarefas associadas a um curso específico do cache.
   - Se os dados estiverem disponíveis no cache, eles são utilizados diretamente.
   - Caso contrário, o sistema consulta a API do Google Classroom, obtém as tarefas e armazena no cache para futuras consultas.

4. **Cache de Pendências por Aluno**:
   - O sistema tenta recuperar as pendências (tarefas não concluídas) de um aluno de um curso específico usando o cache.
   - Se as pendências estiverem disponíveis, elas são retornadas diretamente.
   - Se não estiverem no cache, o sistema faz uma consulta à API e atualiza o cache com as pendências do aluno.

5. **Validade dos Dados no Cache**:
   - O cache é atualizado periodicamente ou quando os dados são modificados.
   - Cada entrada de cache tem um tempo de expiração configurado (por exemplo, 30 minutos ou 1 hora), garantindo que os dados não fiquem desatualizados.

## 3. Fluxos Alternativos

- **Cache Vazio ou Expirado**:
   - Se os dados não estiverem no cache (ou tiverem expirado), o sistema faz uma chamada à API do Google Classroom e armazena os novos dados no cache.

- **Falha no Acesso ao Cache**:
   - Caso o Redis Cache não esteja acessível, o sistema faz uma chamada direta à API para garantir a continuidade das operações, mas sem armazenar os dados em cache até que o problema seja resolvido.

## 4. Subfluxos

1. **Armazenar Dados no Cache**:
   - Sempre que os dados são obtidos da API do Google Classroom, o sistema armazena esses dados no Redis Cache, com um tempo de expiração configurado.

2. **Recuperar Dados do Cache**:
   - Antes de fazer qualquer requisição à API, o sistema verifica se os dados estão disponíveis no cache e, se estiverem, evita fazer uma nova chamada à API.

3. **Remover Dados do Cache**:
   - O sistema pode remover entradas específicas do cache (por exemplo, ao finalizar um curso ou tarefa) ou limpar o cache completamente em casos de manutenção.

## 5. Cenários Chave

- **Melhorar Desempenho**:
   - O uso de cache melhora o desempenho geral do sistema, evitando chamadas excessivas à API e proporcionando respostas mais rápidas aos usuários.

- **Minimizar Chamadas à API**:
   - O cache reduz a necessidade de chamadas repetidas à API do Google Classroom para dados que não mudam com frequência, como cursos e tarefas.

## 6. Condições Prévias

- O sistema deve estar conectado ao servidor Redis e o cache deve estar funcional.
- O sistema deve estar corretamente configurado para realizar operações de leitura e escrita no Redis Cache.

## 7. Condições Posteriores

- Os dados recuperados da API do Google Classroom devem ser armazenados no cache para consultas futuras.
- O cache deve estar pronto para ser utilizado nas próximas requisições.

## 8. Pontos de Extensão

- **Atualização Proativa do Cache**:
   - O sistema pode ser configurado para atualizar proativamente os dados em cache antes que eles expirem, prevenindo a necessidade de chamadas à API quando os dados estão próximos de expirar.

- **Cache Distribuído**:
   - O sistema pode ser estendido para usar caches distribuídos em vários servidores, melhorando a escalabilidade e a tolerância a falhas.

## 9. Requisitos Especiais

- Disponíveis no documento [Especificação Suplementar](rup_supdoc.md).

## 10. Informações Especiais

- O Redis Cache é uma ferramenta essencial para garantir que o sistema mantenha um desempenho eficiente, minimizando a latência das respostas e reduzindo a carga nas APIs externas. Todas as operações de leitura e escrita no cache são monitoradas para garantir que os dados estejam sempre atualizados.
