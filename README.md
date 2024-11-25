 Academic Event Manager

## **Descrição**

O **Academic Event Manager** é uma aplicação para gerenciar eventos acadêmicos utilizando **FastAPI**. A aplicação oferece funcionalidades de CRUD (Create, Read, Update e Delete) para eventos, utilizando um arquivo CSV como banco de dados, além de funcionalidades adicionais como contagem de eventos, cálculo de hash SHA256 e compactação do arquivo CSV.

Este projeto foi desenvolvido como parte do **Trabalho Prático 1 (TP1)**, aplicando conceitos de manipulação de arquivos e APIs RESTful.

---

## **Tecnologias Utilizadas**

- **Python 3.10+**: Linguagem de programação principal.
- **FastAPI**: Framework para construção de APIs REST.
- **Uvicorn**: Servidor ASGI utilizado para desenvolvimento e execução.
- **Pydantic**: Validação e tipagem de dados.
- **CSV**: Armazenamento persistente dos dados dos eventos.
- **Hashlib**: Geração do hash SHA256 para validação de integridade.
- **Zipfile**: Compactação do arquivo CSV.

---

## **Funcionalidades**

1. **CRUD de Eventos**:
   - **C**: Criar um novo evento.
   - **R**: Listar todos os eventos.
   - **U**: Atualizar um evento existente.
   - **D**: Remover um evento.

2. **Contagem de Eventos**:
   - Retorna o número total de eventos registrados no arquivo CSV.

3. **Cálculo do Hash SHA256**:
   - Calcula e retorna o hash SHA256 do arquivo CSV.

4. **Compactação do Arquivo CSV**:
   - Compacta o arquivo CSV em um ZIP e permite o download.

---

## **Instalação**

### **Pré-requisitos**
- Python 3.10 ou superior.
- Ferramenta de gerenciamento de ambientes virtuais (recomendado).
- Gerenciador **UV** configurado para executar o projeto.

### **Passos para Instalação**

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/moglylima/academic-event-manager.git
   cd academic-event-manager

2. **Com o UV no seu ambiente, basta executar o comando a seguir**
    ```bash
    uv run fastapi dev

3. Acesse a documentação:
    + Acesse http://127.0.0.1:8000/docs para visualizar a documentação interativa da API via Swagger.

4. Caso queira conferir a versão em cloud:
   + Acesse [Link Projeto doc](http://tp-persistencia.moglydev.com.br/docs)


## Estrutura do Projeto
```plaintext
    academic_event_manager/
    │
    ├── app/
    │   ├── data/
    │   │   ├── event.csv          # Arquivo CSV contendo os eventos
    │   │   ├── event.zip          # Arquivo ZIP gerado ao compactar o CSV
    │   ├── routes/
    │   │   ├── event_router.py    # Rotas da API
    │   ├── schemas/
    │   │   ├── event_schema.py    # Schemas para validação de eventos
    │   ├── services/
    │   │   ├── event_service.py   # Lógica para manipulação do CSV
    │   ├── utils/
    │   │   ├── file_utils.py      # Utilitários para hash e compactação
    │   ├── config.py              # Configurações gerais
    │   ├── main.py                # Inicialização da aplicação
    │
    ├── .gitignore                 # Arquivos ignorados pelo Git
    ├── README.md                  # Documentação do projeto
    ├── requirements.txt           # Dependências do projeto

```


# Endpoints

**CRUD**

| **Método** | **Endpoint**           | **Descrição**                               | **Status Code** |
|------------|-------------------------|---------------------------------------------|-----------------|
| `GET`      | `/api/v1/events/`       | Lista todos os eventos.                    | 200             |
| `POST`     | `/api/v1/events/`       | Cria um novo evento.                       | 201             |
| `PUT`      | `/api/v1/events/{id}/`  | Atualiza um evento existente pelo ID.      | 200, 404        |
| `DELETE`   | `/api/v1/events/{id}/`  | Remove um evento existente pelo ID.        | 200, 404        |

---

## **Utilitários**

| **Método** | **Endpoint**                | **Descrição**                               | **Status Code** |
|------------|------------------------------|---------------------------------------------|-----------------|
| `GET`      | `/api/v1/events/count/`      | Retorna a contagem de eventos no CSV.       | 200             |
| `GET`      | `/api/v1/events/hash/`       | Retorna o hash SHA256 do arquivo CSV.       | 200             |
| `GET`      | `/api/v1/events/compress/`   | Compacta e retorna o arquivo CSV como ZIP.  | 200             |
