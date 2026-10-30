# Importa as classes principais do FastAPI e a exceção para erros HTTP
from fastapi import FastAPI, HTTPException

# Importa o middleware de CORS para permitir requisições de outras origens (como o React)
from fastapi.middleware.cors import CORSMiddleware

# Importa a classe base do Pydantic para validação e estruturação de dados
from pydantic import BaseModel

# Importa utilitários de tipagem do Python (Optional para campos opcionais e List para listas)
from typing import Optional, List

# Inicializa a aplicação FastAPI definindo um título e a versão da API
app = FastAPI(title="API de Clientes", version="1.0")

# Adiciona o middleware de CORS na aplicação para evitar bloqueios de segurança do navegador
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Permite apenas requisições vindas do projeto React (Vite)
    allow_credentials=True,                  # Permite o envio de credenciais (cookies, tokens)
    allow_methods=["*"],                     # Permite todos os métodos HTTP (GET, POST, DELETE, PUT, etc.)
    allow_headers=["*"],                     # Permite todos os cabeçalhos nas requisições
)

# Define o modelo de dados para a criação de um cliente usando Pydantic (valida o que chega do front-end)
class ClienteCreate(BaseModel):
    nome: str                  # Campo obrigatório do tipo texto
    email: str                 # Campo obrigatório do tipo texto
    telefone: Optional[str] = "" # Campo opcional do tipo texto, com valor padrão vazio
    empresa: Optional[str] = ""  # Campo opcional do tipo texto, com valor padrão vazio

# Define o modelo completo do Cliente herdando de 'ClienteCreate' e adicionando campos gerados pelo sistema
class Cliente(ClienteCreate):
    id: int                    # Identificador único numérico do cliente
    active: bool = True        # Status booleano indicando se está ativo (padrão é True)

# Simula um banco de dados  utilizando uma lista Python tipada com objetos 'Cliente'
clients_db: List[Cliente] = [
    Cliente(id=1, nome="Huguinho", email="huguinho@empresa.com", telefone="(11) 98765-4321", empresa="Tech Solutions", active=True),
    Cliente(id=2, nome="Zezinho", email="zezinho@inovacao.br", telefone="(21) 97654-3210", empresa="Raiz S.A.", active=True),
]

# Define a rota HTTP GET para o endpoint '/api/clients', que retorna a lista de todos os clientes
@app.get("/api/clients", response_model=List[Cliente])
def get_clients():
    return clients_db  # Retorna a lista completa armazenada 

# Define a rota HTTP POST para o endpoint '/api/clients' com código de status HTTP 201 (Created)
@app.post("/api/clients", response_model=Cliente, status_code=201)
def add_client(client: ClienteCreate):
    # Calcula o novo ID incrementando 1 com base no tamanho atual da lista
    novo_id = len(clients_db) + 1
    
    # Cria uma nova instância do modelo 'Cliente' combinando os dados recebidos e gerados
    novo_cliente = Cliente(
        id=novo_id,
        nome=client.nome,
        email=client.email,
        telefone=client.telefone,
        empresa=client.empresa,
        active=True
    )
    
    # Adiciona o novo cliente à lista simulada em memória
    clients_db.append(novo_cliente)
    
    # Retorna o objeto do cliente recém-criado
    return novo_cliente