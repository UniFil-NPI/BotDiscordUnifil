# Especificação de Caso de Uso: Autenticar API

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

O caso de uso **"Autenticar API"** descreve o processo pelo qual o sistema se autentica na API do Google Classroom. Este processo é necessário para garantir que as requisições feitas ao Google Classroom sejam autorizadas, permitindo a recuperação de dados sobre cursos, alunos, tarefas e pendências. A autenticação é baseada em um token OAuth 2.0 que deve ser renovado quando expirado.

## 2. Fluxo Básico de Eventos

1. **Verificar Token Existente**:
   - O sistema verifica se já existe um token de autenticação armazenado no arquivo `token.json`.

2. **Validar Token**:
   - O sistema verifica se o token existente ainda é válido.
   - Se o token estiver válido, o sistema o utiliza para continuar as requisições à API.

3. **Renovar Token Expirado**:
   - Se o token estiver expirado, o sistema verifica se há um `refresh_token` disponível para renovar a autenticação automaticamente.
   - O sistema renova o token de acesso utilizando o `refresh_token` e atualiza o arquivo `token.json`.

4. **Solicitar Nova Autenticação (Se Necessário)**:
   - Caso não haja um `refresh_token` ou o token não seja renovável, o sistema solicita ao administrador uma nova autenticação OAuth 2.0.
   - O administrador deve seguir o processo de autenticação via navegador para gerar um novo token.

5. **Armazenar Novo Token**:
   - Após a autenticação bem-sucedida, o sistema armazena o novo token no arquivo `token.json` para uso futuro.

6. **Autenticação Completa**:
   - Uma vez autenticado, o sistema permite que as requisições à API do Google Classroom sejam feitas com o token autorizado.

## 3. Fluxos Alternativos

- **Falha na Renovação do Token**:
   - Caso a tentativa de renovação do token falhe, o sistema notifica o administrador que será necessária uma nova autenticação manual.

- **Token Inválido ou Ausente**:
   - Se o arquivo `token.json` não estiver presente ou o token estiver inválido, o sistema solicitará uma nova autenticação manual por parte do administrador.

## 4. Subfluxos

1. **Verificar Validade do Token**:
   - Antes de cada requisição à API, o sistema verifica a validade do token para garantir que ele esteja autorizado a realizar a ação.

2. **Renovar Token Automaticamente**:
   - O sistema tenta renovar automaticamente o token se houver um `refresh_token` disponível e o token de acesso estiver expirado.

## 5. Cenários Chave

- A autenticação é necessária quando o sistema precisa acessar ou consultar dados da API do Google Classroom. Sem uma autenticação válida, nenhuma requisição poderá ser feita.

## 6. Condições Prévias

- O sistema deve ter as credenciais corretas do Google Classroom e um token de autenticação armazenado no arquivo `token.json`.

## 7. Condições Posteriores

- O sistema estará autenticado e autorizado a fazer chamadas à API do Google Classroom.
- O token de autenticação será armazenado ou renovado, e pronto para uso nas futuras requisições.

## 8. Pontos de Extensão

- **Manter Sessão Ativa**:
   - O sistema pode implementar uma função para verificar o tempo restante do token em intervalos regulares e renová-lo proativamente, antes de ele expirar.

## 9. Requisitos Especiais

- Disponíveis no documento [Especificação Suplementar](rup_supdoc.md).

## 10. Informações Especiais

- Este caso de uso depende de um token OAuth 2.0 gerado pelo Google, que é armazenado no arquivo `token.json`. A renovação automática com `refresh_token` reduz a necessidade de repetidas autenticações manuais.
