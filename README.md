Com certeza\! Segue o `README.md` atualizado com a sua dica incluída na seção de autenticação.

# Flix API - Painel Interativo

## Visão Geral da API

Este documento fornece uma visão completa dos dados gerenciados pela Flix API. Explore as principais métricas e a distribuição de conteúdo para entender o escopo e a escala do catálogo.

### Estatísticas Gerais

  - **Total de Filmes**: 238
  - **Total de Avaliações**: 1.102
  - **Média de Avaliações**: 4.2 ⭐

### Distribuição de Filmes por Gênero

| Gênero | Quantidade de Filmes |
|---|---|
| Drama | 55 |
| Ação | 45 |
| Comédia | 38 |
| Ficção Científica | 30 |
| Terror | 25 |
| Romance | 20 |
| Animação | 15 |
| Documentário | 10 |

-----

## Explorador de Endpoints

Navegue pelos recursos da API de forma detalhada. Cada seção apresenta os métodos HTTP disponíveis e exemplos de corpos de requisição.

### 📋 Documentação Interativa (Swagger)

A Flix API inclui documentação interativa completa através do Swagger UI, onde você pode testar os endpoints diretamente no navegador:

  - **Swagger UI**: `http://localhost:8000/swagger/`
  - **Redoc**: `http://localhost:8000/redoc/`
  - **Schema OpenAPI**: `http://localhost:8000/swagger.json`

> **💡 Dica**: Use o Swagger UI para testar os endpoints de forma interativa, sem precisar de ferramentas externas como Postman ou curl.

### 🔑 Autenticação

Endpoints para obter e gerenciar tokens de autenticação JWT.

#### `POST /api/v1/autenticacao/token/`

  - **Descrição**: Obtém um par de tokens (acesso e refresh)
  - **Exemplo de corpo**:

<!-- end list -->

```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

> **Importante**: Após copiar o `access token` gerado, no botão **Authorize** no início da página Swagger, vá para o campo **value** e digite `"Bearer "` (com um espaço no final) e cole o seu `access token` em seguida. Feito isso, as rotas já estarão autorizadas.

#### `POST /api/vI/autenticacao/token/refresh/`

  - **Descrição**: Renova um token de acesso expirado
  - **Exemplo de corpo**:

<!-- end list -->

```json
{
  "refresh": "seu_token_de_refresh"
}
```

#### `POST /api/v1/autenticacao/token/verify/`

  - **Descrição**: Verifica a validade de um token
  - **Exemplo de corpo**:

<!-- end list -->

```json
{
  "token": "seu_token_de_acesso"
}
```

### 🎭 Gêneros

Gerenciamento de gêneros de filmes.

#### `GET /api/v1/generos/`

  - **Descrição**: Lista todos os gêneros

#### `POST /api/v1/generos/`

  - **Descrição**: Cria um novo gênero
  - **Exemplo de corpo**:

<!-- end list -->

```json
{
  "nome": "Aventura"
}
```

#### `GET /api/v1/generos/<int:pk>/`

  - **Descrição**: Recupera um gênero específico

#### `PUT /api/v1/generos/<int:pk>/`

  - **Descrição**: Atualiza um gênero
  - **Exemplo de corpo**:

<!-- end list -->

```json
{
  "nome": "Aventura Fantástica"
}
```

#### `DELETE /api/v1/generos/<int:pk>/`

  - **Descrição**: Exclui um gênero

### 🧑‍🎤 Atores

Gerenciamento de informações sobre atores.

#### `GET /api/v1/atores/`

  - **Descrição**: Lista todos os atores

#### `POST /api/v1/atores/`

  - **Descrição**: Adiciona um novo ator
  - **Exemplo de corpo**:

<!-- end list -->

```json
{
  "nome": "Nome do Ator",
  "data_nascimento": "1990-01-01",
  "nacionalidade": "BR"
}
```

#### `GET /api/v1/atores/<int:pk>/`

  - **Descrição**: Recupera um ator específico

#### `PUT /api/v1/atores/<int:pk>/`

  - **Descrição**: Atualiza os dados de um ator

#### `DELETE /api/v1/atores/<int:pk>/`

  - **Descrição**: Exclui um ator

### 🎬 Filmes

Gerenciamento de filmes e suas relações.

#### `GET /api/v1/filmes/`

  - **Descrição**: Lista todos os filmes

#### `POST /api/v1/filmes/`

  - **Descrição**: Cria um novo filme
  - **Exemplo de corpo**:

<!-- end list -->

```json
{
  "titulo": "Novo Filme",
  "genero": 1,
  "ano_lancamento": "2025-01-01",
  "atores": [1, 2],
  "sinopse": "Uma breve sinopse."
}
```

#### `GET /api/v1/filmes/<int:pk>/`

  - **Descrição**: Recupera um filme específico

#### `PUT /api/v1/filmes/<int:pk>/`

  - **Descrição**: Atualiza um filme

#### `DELETE /api/v1/filmes/<int:pk>/`

  - **Descrição**: Exclui um filme

#### `GET /api/v1/filmes/stats/`

  - **Descrição**: Retorna estatísticas sobre os filmes

### ⭐ Avaliações (Reviews)

Gerenciamento de avaliações de filmes.

#### `GET /api/v1/reviews/`

  - **Descrição**: Lista todas as avaliações

#### `POST /api/v1/reviews/`

  - **Descrição**: Cria uma nova avaliação
  - **Exemplo de corpo**:

<!-- end list -->

```json
{
  "filme": 1,
  "estrelas": 5,
  "comentario": "Excelente!"
}
```

#### `GET /api/v1/reviews/<int:pk>/`

  - **Descrição**: Recupera uma avaliação específica

#### `PUT /api/v1/reviews/<int:pk>/`

  - **Descrição**: Atualiza uma avaliação

#### `DELETE /api/v1/reviews/<int:pk>/`

  - **Descrição**: Exclui uma avaliação

-----

## 🐳 Guia de Configuração com Docker

Siga estes passos para configurar e executar o projeto da Flix API usando Docker, simplificando o ambiente de desenvolvimento.

### 1\. Pré-requisitos

  - [Docker](https://docs.docker.com/get-docker/)
  - [Docker Compose](https://docs.docker.com/compose/install/)

### 2\. Clonar o Repositório

```bash
git clone <url_do_repositorio>
cd flix_api
```

### 3\. Construir e Iniciar os Contêineres

Use o Docker Compose para construir a imagem e iniciar o serviço da API.

```bash
docker-compose up --build
```

O serviço estará disponível em `http://localhost:8000`.

### 4\. Aplicar Migrações do Banco de Dados

Em um novo terminal, execute o comando de migração dentro do contêiner para criar a estrutura do banco de dados.

```bash
docker-compose exec flix-api python manage.py migrate
```

### 5\. Criar Superusuário

Crie um usuário administrador para acessar o painel `/admin/`.

```bash
docker-compose exec flix-api python manage.py createsuperuser
```

### 6\. Acessar a Aplicação

Após iniciar o serviço, você pode acessar:

  - **API Base**: `http://localhost:8000/api/v1/`
  - **Admin Panel**: `http://localhost:8000/admin/`
  - **Swagger UI**: `http://localhost:8000/swagger/`
  - **Redoc**: `http://localhost:8000/redoc/`

### Comandos Úteis do Docker

  - **Parar os contêineres**:
    ```bash
    docker-compose down
    ```
  - **Verificar os logs em tempo real**:
    ```bash
    docker-compose logs -f
    ```
  - **Executar um comando dentro do contêiner**:
    ```bash
    docker-compose exec flix-api <seu_comando>
    ```

-----

© 2025 Flix API. Documentação criada para fins de demonstração.
