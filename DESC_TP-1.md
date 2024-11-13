# Trabalho Prático 1: Arquivos e Serialização de Objetos

## Objetivo
Este trabalho prático tem como objetivo o desenvolvimento de habilidades práticas em serialização de objetos e manipulação de arquivos utilizando Python e FastAPI para criar uma API REST que gerencia dados armazenados em um arquivo CSV.

## Descrição das Tarefas

### 1. Definição de uma Entidade
- **Entidade Escolhida**: Descrever uma entidade com no mínimo 5 atributos distintos da entidade "Cliente" para representação dos dados manipulados.
- **Atributos da Entidade**: Incluir atributos como `id`, `nome`, `categoria`, `preço`, `estoque`, etc.

### 2. Desenvolvimento da API REST com FastAPI
Implementar os seguintes endpoints para manipulação da entidade:
- **F1: Inserção de Dados**
  - `POST /entidade`: Recebe dados em JSON e os adiciona ao arquivo CSV.
- **F2: Listagem de Dados**
  - `GET /entidade`: Retorna todos os dados armazenados no arquivo CSV.
- **F3: Operações CRUD**
  - `GET /entidade/{id}`, `PUT /entidade/{id}`, `DELETE /entidade/{id}`: Endpoints para leitura, atualização e remoção de dados específicos.
- **F4: Contagem de Entidades**
  - `GET /entidade/count`: Retorna o total de entidades no CSV.
- **F5: Compactação do Arquivo CSV**
  - `GET /entidade/download-zip`: Compacta o CSV em um arquivo ZIP e retorna para o usuário.
- **F6: Hash do Arquivo CSV**
  - `GET /entidade/hash`: Calcula e retorna o hash SHA256 do arquivo CSV.

### 3. Divisão de Tarefas
Documentar em um arquivo `divisao_tarefas.txt` as responsabilidades específicas de cada membro da dupla.

## Requisitos de Entrega
- **Código-Fonte e Arquivo CSV**: Enviar o código-fonte e um arquivo CSV contendo pelo menos 10 entidades pré-cadastradas.
- **Apresentação**: Obrigatória e presencial para ambos os membros da dupla, com 5 minutos para cada um.

## Dados
- Utilizar dados realistas ao preencher o arquivo CSV para evitar conteúdos genéricos.

## Observações
- A falta de apresentação resultará em nota zero.
- Não serão permitidas apresentações remotas.
- As notas podem ser diferenciadas com base na qualidade da apresentação e contribuição ao projeto.
