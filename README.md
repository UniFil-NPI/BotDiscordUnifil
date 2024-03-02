
# Bot UniFil

> Um bot feito para o discord da UniFil, 

Desenvolvedor: [💻@GbrielZanoni](https://github.com/GbrielZanoni
)
![LOGO](https://web.unifil.br/eventos/intercursos/imagens/logo.png)
## FAQ

#### O que é isto?

Este repositório foi feito para o mantimento do Bot de Classroom com a intenção de ter uma interação direta com o Aluno da UniFil.


# Guia de instalação
## PRÉ-REQUISITOS
> É necessário Python 3.8 ou qualquer outra versão acima

### Para começar, é necessário clonar o repo localmente:
```
git clone https://github.com/UniFil-NPI/BotDiscordUnifil.git
```
É também recomendado a criação & uso de uma nova branch, para evitar qualquer erro indo diretamente para a `main` 
```
git checkout -b 'nome da branch'
```
# Criando o ambiente virtual
Após a criação de uma nova branch no seu repositório local, é necessário criar um ambiente virtual (.venv) e instalar as dependencias do projeto nesse ambiente.

### Para a criação do ambiente virtual utilizamos no cmd: 
```
$ cd path/do/seu/arquivo
$ python3 -m venv bot-env
```
Após isto, é necessário ativar o ambiente virtual:

Código Normal (CMD):
```
$ source bot-env/bin/activate
```
Código no PowerShell:

```
$ bot-env\Scripts\activate.bat
```
Certifique-se que o ambiente virtual está ativo. No seu prompt de comando ou powershell devem estar com o caminho:
```
(env) C:\Users\Usuário\Desktop\Bot\bot>
```
É então, necessário do **pip** para executar o bot. 
```
$ pip install -U discord.py
```

### Dependências

Pronto, agora que temos o nosso ambiente virtual, podemos instalar as dependencias do nosso projeto utilizando:
```
$ pip install -r requirements.txt
```
## Documentação da API

#### Retorna todos os itens

```http
  GET /api/items
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `api_key` | `string` | **Obrigatório**. A chave da sua API |

#### Retorna um item

```http
  GET /api/items/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Obrigatório**. O ID do item que você quer |

#### add(num1, num2)

Recebe dois números e retorna a sua soma.

