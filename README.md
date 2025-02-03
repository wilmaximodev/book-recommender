# 📚 Book Recommender

## Descrição

O **Book Recommender** é uma aplicação web desenvolvida com Flask e integração com a API Gemini para recomendar livros com base no histórico de compras do usuário. A IA analisa o histórico e sugere livros de categorias como ficção, não ficção, ciência, terror e romance.

## Funcionalidades

- 📖 Recomenda livros com base no histórico de compras do usuário.
- ⚙️ Integrado com a **API Gemini** para utilizar IA em decisões de recomendação.
- 🌐 Web interface simples para interagir com o sistema e ver as recomendações.

## Como Testar o Projeto

### Pré-requisitos

1. **Python** (recomenda-se a versão 3.8 ou superior)
2. **Flask**
3. **Gemini API Key** (Obtido ao se cadastrar na [plataforma Gemini](https://cloud.google.com/)

### Passo 1: Clone o Repositório
Clone este repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/book-recommender.git
cd book-recommender
```
### Passo 2: Instale as Dependências
Crie um ambiente virtual para o projeto e instale as dependências necessárias:

```bash
# Criar o ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt

```

### Passo 3: Configuração da API Key
O projeto usa a API Gemini para gerar as recomendações. Para isso, é necessário configurar a chave de API:

Crie uma variável de ambiente chamada GEMINI_API_KEY com sua chave de API:
No Linux/macOS:

```bash
export GEMINI_API_KEY="sua_chave_api_aqui"
No Windows:
set GEMINI_API_KEY="sua_chave_api_aqui"
```
### Passo 4: Execute o Servidor
Inicie o servidor Flask para rodar a aplicação localmente:

```bash
python app.py
```
A aplicação estará acessível em http://127.0.0.1:5000/.

### Passo 5: Testando as Funcionalidades
Para testar as funcionalidades do sistema, basta acessar os seguintes endpoints na sua aplicação:

Página Inicial
A página principal do projeto:

```nginx
GET http://127.0.0.1:5000/
```

Recomendação de Livros
Substitua user_id por um ID de usuário válido (exemplo: 1, 2, 3, etc.) para ver a recomendação personalizada.

```nginx
GET http://127.0.0.1:5000/recommend/<user_id>
```

Exemplo de URL:

```arduino
http://127.0.0.1:5000/recommend/1
```
Esse endpoint irá exibir uma recomendação de livro com base no histórico de compras do usuário.

### Passo 6: Verificando o Histórico do Usuário
O histórico do usuário é simulado pela função get_user_history. Você pode alterar ou adicionar dados simulados em Utils/user_data.py para testar diferentes cenários.

### Estrutura de Diretórios
```bash
book-recommender/
│
├── app.py               # Arquivo principal da aplicação Flask
├── static/              # Arquivos estáticos (CSS, JS, etc.)
│   └── style.css
├── templates/           # Templates HTML do Flask
│   └── recommendation.html
├── Utils/               # Funções auxiliares
│   └── user_data.py
├── Functions/           # Funções de recomendação de livros
│   └── book_recommendations.py
└── requirements.txt     # Dependências do projeto
```

### Contribuição
Se você deseja contribuir para o projeto, fique à vontade para enviar um pull request. Para qualquer sugestão ou correção, crie uma issue para discutirmos.
