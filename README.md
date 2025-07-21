
# Flix API - Visão Geral

A Flix API é uma interface de programação de aplicações construída com Django e Django REST Framework, projetada para gerenciar filmes, gêneros, atores, e avaliações. Ela inclui autenticação JWT para proteger seus endpoints.

## Endpoints da API

A API está organizada em módulos e segue uma estrutura RESTful. Todos os endpoints são prefixados com `/api/v1/`.

### Autenticação

Estes endpoints são utilizados para a gestão de tokens de autenticação JWT.

* **`POST /api/v1/autenticacao/token/`**
    * **Descrição:** Obtém um par de tokens (acesso e refresh).
    * **Método:** `POST`
    * **Corpo da Requisição (JSON):**
        ```json
        {
            "username": "seu_usuario",
            "password": "sua_senha"
        }
        ```
    * **Resposta (JSON):**
        ```json
        {
            "access": "...",
            "refresh": "..."
        }
        ```

* **`POST /api/v1/autenticacao/token/refresh/`**
    * **Descrição:** Renova um token de acesso expirado usando um token de refresh.
    * **Método:** `POST`
    * **Corpo da Requisição (JSON):**
        ```json
        {
            "refresh": "seu_token_refresh"
        }
        ```
    * **Resposta (JSON):**
        ```json
        {
            "access": "novo_token_de_acesso"
        }
        ```

* **`POST /api/v1/autenticacao/token/verify/`**
    * **Descrição:** Verifica a validade de um token de acesso.
    * **Método:** `POST`
    * **Corpo da Requisição (JSON):**
        ```json
        {
            "token": "seu_token_de_acesso"
        }
        ```
    * **Resposta:** Status 200 OK se válido, ou erro 401/403 se inválido.

### Gêneros

Gerenciamento de gêneros de filmes.

* **`GET /api/v1/generos/`**
    * **Descrição:** Lista todos os gêneros.
    * **Método:** `GET`
    * **Permissões:** Autenticado, `view_genero`
* **`POST /api/v1/generos/`**
    * **Descrição:** Cria um novo gênero.
    * **Método:** `POST`
    * **Corpo da Requisição (JSON):**
        ```json
        {
            "nome": "Nome do Gênero"
        }
        ```
    * **Permissões:** Autenticado, `add_genero`
* **`GET /api/v1/generos/<int:pk>/`**
    * **Descrição:** Recupera os detalhes de um gênero específico.
    * **Método:** `GET`
    * **Permissões:** Autenticado, `view_genero`
* **`PUT /api/v1/generos/<int:pk>/`**
    * **Descrição:** Atualiza um gênero existente.
    * **Método:** `PUT`
    * **Corpo da Requisição (JSON):**
        ```json
        {
            "nome": "Novo Nome do Gênero"
        }
        ```
    * **Permissões:** Autenticado, `change_genero`
* **`PATCH /api/v1/generos/<int:pk>/`**
    * **Descrição:** Atualiza parcialmente um gênero existente.
    * **Método:** `PATCH`
    * **Corpo da Requisição (JSON):**
        ```json
        {
            "nome": "Nome Parcial"
        }
        ```
    * **Permissões:** Autenticado, `change_genero`
* **`DELETE /api/v1/generos/<int:pk>/`**
    * **Descrição:** Exclui um gênero.
    * **Método:** `DELETE`
    * **Permissões:** Autenticado, `delete_genero`

### Atores

Gerenciamento de informações sobre atores.

* **`GET /api/v1/atores/`**
    * **Descrição:** Lista todos os atores.
    * **Método:** `GET`
    * **Permissões:** Autenticado, `view_atores`
* **`POST /api/v1/atores/`**
    * **Descrição:** Cria um novo ator.
    * **Método:** `POST`
    * **Corpo da Requisição (JSON):**
        ```json
        {
            "nome": "Nome do Ator",
            "data_nascimento": "AAAA-MM-DD",
            "nacionalidade": "BR"
        }
        ```
    * **Permissões:** Autenticado, `add_atores`
* **`GET /api/v1/atores/<int:pk>/`**
    * **Descrição:** Recupera os detalhes de um ator específico.
    * **Método:** `GET`
    * **Permissões:** Autenticado, `view_atores`
* **`PUT /api/v1/atores/<int:pk>/`**
    * **Descrição:** Atualiza um ator existente.
    * **Método:** `PUT`
    * **Corpo da Requisição (JSON):** Os mesmos campos do POST.
    * **Permissões:** Autenticado, `change_atores`
* **`PATCH /api/v1/atores/<int:pk>/`**
    * **Descrição:** Atualiza parcialmente um ator existente.
    * **Método:** `PATCH`
    * **Corpo da Requisição (JSON):** Os mesmos campos do POST, mas apenas os que deseja atualizar.
    * **Permissões:** Autenticado, `change_atores`
* **`DELETE /api/v1/atores/<int:pk>/`**
    * **Descrição:** Exclui um ator.
    * **Método:** `DELETE`
    * **Permissões:** Autenticado, `delete_atores`

### Filmes

Gerenciamento de filmes e estatísticas.

* **`GET /api/v1/filmes/`**
    * **Descrição:** Lista todos os filmes.
    * **Método:** `GET`
    * **Permissões:** Autenticado, `view_filme`
* **`POST /api/v1/filmes/`**
    * **Descrição:** Cria um novo filme.
    * **Método:** `POST`
    * **Corpo da Requisição (JSON):**
        ```json
        {
            "titulo": "Título do Filme",
            "genero": 1, // ID do Gênero
            "ano_lancamento": "AAAA-MM-DD",
            "atores": [1, 2], // IDs dos Atores
            "sinopse": "Sinopse do filme"
        }
        ```
        * **Validações:**
            * `ano_lancamento`: Não pode ser uma data futura.
            * `sinopse`: Não pode ter mais de 500 caracteres.
    * **Permissões:** Autenticado, `add_filme`
* **`GET /api/v1/filmes/<int:pk>/`**
    * **Descrição:** Recupera os detalhes de um filme específico. Inclui a média de avaliações (rating).
    * **Método:** `GET`
    * **Permissões:** Autenticado, `view_filme`
* **`PUT /api/v1/filmes/<int:pk>/`**
    * **Descrição:** Atualiza um filme existente.
    * **Método:** `PUT`
    * **Corpo da Requisição (JSON):** Os mesmos campos do POST.
    * **Permissões:** Autenticado, `change_filme`
* **`PATCH /api/v1/filmes/<int:pk>/`**
    * **Descrição:** Atualiza parcialmente um filme existente.
    * **Método:** `PATCH`
    * **Corpo da Requisição (JSON):** Os mesmos campos do POST, mas apenas os que deseja atualizar.
    * **Permissões:** Autenticado, `change_filme`
* **`DELETE /api/v1/filmes/<int:pk>/`**
    * **Descrição:** Exclui um filme.
    * **Método:** `DELETE`
    * **Permissões:** Autenticado, `delete_filme`
* **`GET /api/v1/filmes/stats/`**
    * **Descrição:** Retorna estatísticas gerais sobre filmes e avaliações.
    * **Método:** `GET`
    * **Resposta (JSON):**
        ```json
        {
            "total_filmes": 0,
            "filmes_por_genero": [],
            "total_reviews": 0,
            "media_avaliacoes": 0.0
        }
        ```
    * **Permissões:** Autenticado, `view_filme`

### Avaliações (Reviews)

Gerenciamento de avaliações de filmes.

* **`GET /api/v1/reviews/`**
    * **Descrição:** Lista todas as avaliações.
    * **Método:** `GET`
    * **Permissões:** Autenticado, `view_review`
* **`POST /api/v1/reviews/`**
    * **Descrição:** Cria uma nova avaliação para um filme.
    * **Método:** `POST`
    * **Corpo da Requisição (JSON):**
        ```json
        {
            "filme": 1, // ID do Filme
            "estrelas": 4, // 0 a 5 estrelas
            "comentario": "Ótimo filme!"
        }
        ```
        * **Validações:**
            * `estrelas`: Deve ser entre 0 e 5.
    * **Permissões:** Autenticado, `add_review`
* **`GET /api/v1/reviews/<int:pk>/`**
    * **Descrição:** Recupera os detalhes de uma avaliação específica.
    * **Método:** `GET`
    * **Permissões:** Autenticado, `view_review`
* **`PUT /api/v1/reviews/<int:pk>/`**
    * **Descrição:** Atualiza uma avaliação existente.
    * **Método:** `PUT`
    * **Corpo da Requisição (JSON):** Os mesmos campos do POST.
    * **Permissões:** Autenticado, `change_review`
* **`PATCH /api/v1/reviews/<int:pk>/`**
    * **Descrição:** Atualiza parcialmente uma avaliação existente.
    * **Método:** `PATCH`
    * **Corpo da Requisição (JSON):** Os mesmos campos do POST, mas apenas os que deseja atualizar.
    * **Permissões:** Autenticado, `change_review`
* **`DELETE /api/v1/reviews/<int:pk>/`**
    * **Descrição:** Exclui uma avaliação.
    * **Método:** `DELETE`
    * **Permissões:** Autenticado, `delete_review`

## Como Utilizar

1.  **Configuração do Ambiente:**
    * Certifique-se de ter Python e pip instalados.
    * Crie e ative um ambiente virtual:
        ```bash
        python -m venv venv
        source venv/bin/activate  # Linux/macOS
        # venv\Scripts\activate  # Windows
        ```
    * Instale as dependências:
        ```bash
        pip install -r requirements.txt
        pip install -r requirements_dev.txt # Para dependências de desenvolvimento, como flake8
        ```
2.  **Configuração do Banco de Dados:**
    * O projeto usa SQLite por padrão. O arquivo `db.sqlite3` será criado na primeira migração.
    * Aplique as migrações:
        ```bash
        python manage.py migrate
        ```
3.  **Criação de Superusuário (Admin):**
    * Crie um superusuário para acessar o painel administrativo e gerenciar permissões:
        ```bash
        python manage.py createsuperuser
        ```
4.  **Importação de Atores (Opcional):**
    * Se você tem um arquivo CSV com dados de atores (como `Lista_atores.csv`), pode importá-los usando o comando personalizado:
        ```bash
        python manage.py import_atores Lista_atores.csv
        ```
        * O CSV deve ter as colunas `nome`, `data_nascimento` (formato AAAA-MM-DD) e `nacionalidade` (ex: "Brasileiro", "Americano").
5.  **Execução do Servidor:**
    * Inicie o servidor de desenvolvimento Django:
        ```bash
        python manage.py runserver
        ```
    * A API estará disponível em `http://127.0.0.1:8000/`.

6.  **Autenticação e Uso da API:**
    * Para acessar os endpoints protegidos, primeiro obtenha um token de acesso através do endpoint de autenticação.
    * Inclua o token de acesso no cabeçalho `Authorization` de suas requisições, no formato `Bearer <seu_token_de_acesso>`. Ex:
        ```
        Authorization: Bearer seu_token_de_acesso
        ```
