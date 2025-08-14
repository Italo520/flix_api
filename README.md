# Flix API - Painel Interativo

## Visão Geral da API

Este documento fornece uma visão completa dos dados gerenciados pela Flix API. Explore as principais métricas e a distribuição de conteúdo para entender o escopo e a escala do catálogo.

### Estatísticas Gerais

- **Total de Filmes**: 238
- **Total de Avaliações**: 1.102
- **Média de Avaliações**: 4.2 ⭐

### Distribuição de Filmes por Gênero

| Gênero | Quantidade de Filmes |
|--------|---------------------|
| Drama | 55 |
| Ação | 45 |
| Comédia | 38 |
| Ficção Científica | 30 |
| Terror | 25 |
| Romance | 20 |
| Animação | 15 |
| Documentário | 10 |

---

## Explorador de Endpoints

Navegue pelos recursos da API de forma detalhada. Cada seção apresenta os métodos HTTP disponíveis e exemplos de corpos de requisição.

### 📋 Documentação Interativa (Swagger)

A Flix API inclui documentação interativa completa através do Swagger UI, onde você pode testar os endpoints diretamente no navegador:

- **Swagger UI**: `http://127.0.0.1:8000/swagger/`
- **Redoc**: `http://127.0.0.1:8000/redoc/`
- **Schema OpenAPI**: `http://127.0.0.1:8000/swagger.json`

> **💡 Dica**: Use o Swagger UI para testar os endpoints de forma interativa, sem precisar de ferramentas externas como Postman ou curl.

### 🔑 Autenticação

Endpoints para obter e gerenciar tokens de autenticação JWT.

#### `POST /autenticacao/token/`
- **Descrição**: Obtém um par de tokens (acesso e refresh)
- **Exemplo de corpo**:
```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

#### `POST /autenticacao/token/refresh/`
- **Descrição**: Renova um token de acesso expirado
- **Exemplo de corpo**:
```json
{
  "refresh": "seu_token_de_refresh"
}
```

#### `POST /autenticacao/token/verify/`
- **Descrição**: Verifica a validade de um token
- **Exemplo de corpo**:
```json
{
  "token": "seu_token_de_acesso"
}
```

### 🎭 Gêneros

Gerenciamento de gêneros de filmes.

#### `GET /generos/`
- **Descrição**: Lista todos os gêneros

#### `POST /generos/`
- **Descrição**: Cria um novo gênero
- **Exemplo de corpo**:
```json
{
  "nome": "Aventura"
}
```

#### `GET /generos/<int:pk>/`
- **Descrição**: Recupera um gênero específico

#### `PUT /generos/<int:pk>/`
- **Descrição**: Atualiza um gênero
- **Exemplo de corpo**:
```json
{
  "nome": "Aventura Fantástica"
}
```

#### `DELETE /generos/<int:pk>/`
- **Descrição**: Exclui um gênero

### 🧑‍🎤 Atores

Gerenciamento de informações sobre atores.

#### `GET /atores/`
- **Descrição**: Lista todos os atores

#### `POST /atores/`
- **Descrição**: Adiciona um novo ator
- **Exemplo de corpo**:
```json
{
  "nome": "Nome do Ator",
  "data_nascimento": "1990-01-01",
  "nacionalidade": "BR"
}
```

#### `GET /atores/<int:pk>/`
- **Descrição**: Recupera um ator específico

#### `PUT /atores/<int:pk>/`
- **Descrição**: Atualiza os dados de um ator

#### `DELETE /atores/<int:pk>/`
- **Descrição**: Exclui um ator

### 🎬 Filmes

Gerenciamento de filmes e suas relações.

#### `GET /filmes/`
- **Descrição**: Lista todos os filmes

#### `POST /filmes/`
- **Descrição**: Cria um novo filme
- **Exemplo de corpo**:
```json
{
  "titulo": "Novo Filme",
  "genero": 1,
  "ano_lancamento": "2025-01-01",
  "atores": [1, 2],
  "sinopse": "Uma breve sinopse."
}
```

#### `GET /filmes/<int:pk>/`
- **Descrição**: Recupera um filme específico

#### `PUT /filmes/<int:pk>/`
- **Descrição**: Atualiza um filme

#### `DELETE /filmes/<int:pk>/`
- **Descrição**: Exclui um filme

#### `GET /filmes/stats/`
- **Descrição**: Retorna estatísticas sobre os filmes

### ⭐ Avaliações (Reviews)

Gerenciamento de avaliações de filmes.

#### `GET /reviews/`
- **Descrição**: Lista todas as avaliações

#### `POST /reviews/`
- **Descrição**: Cria uma nova avaliação
- **Exemplo de corpo**:
```json
{
  "filme": 1,
  "estrelas": 5,
  "comentario": "Excelente!"
}
```

#### `GET /reviews/<int:pk>/`
- **Descrição**: Recupera uma avaliação específica

#### `PUT /reviews/<int:pk>/`
- **Descrição**: Atualiza uma avaliação

#### `DELETE /reviews/<int:pk>/`
- **Descrição**: Exclui uma avaliação

---

## Guia de Configuração

Siga estes passos para configurar e executar o projeto da Flix API em seu ambiente de desenvolvimento local.

### 1. Configurar Ambiente Virtual

Clone o repositório e crie um ambiente virtual para isolar as dependências.

```bash
git clone <url_do_repositorio>
cd flix_api
python -m venv venv
source venv/bin/activate  # Linux/macOS
```

### 2. Instalar Dependências

Instale todos os pacotes necessários para produção e desenvolvimento.

```bash
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

### 3. Aplicar Migrações do Banco de Dados

Crie a estrutura do banco de dados SQLite executando as migrações do Django.

```bash
python manage.py migrate
```

### 4. Criar Superusuário

Crie um usuário administrador para acessar o painel `/admin/`.

```bash
python manage.py createsuperuser
```

### 5. Executar o Servidor

Inicie o servidor de desenvolvimento. A API estará disponível em `http://127.0.0.1:8000`.

```bash
python manage.py runserver
```

### 6. Acessar a Documentação

Após iniciar o servidor, você pode acessar:

- **API Base**: `http://127.0.0.1:8000/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **Swagger UI**: `http://127.0.0.1:8000/swagger/`
- **Redoc**: `http://127.0.0.1:8000/redoc/`

---

© 2025 Flix API. Documentação criada para fins de demonstração.
