# 19/08/2024 – PYTHON SQLAlchemy 

## 5683. INTRODUÇÃO

### O que é o SQLAlchemy?
SQLAlchemy é uma biblioteca em Python que facilita o trabalho com bancos de dados relacionais. Ela fornece uma camada de abstração que permite interagir com o banco de dados usando classes e objetos em vez de escrever SQL diretamente. Isso torna o código mais limpo, reutilizável e orientado a objetos.

#### Como Funciona?

**SQLAlchemy opera em dois níveis principais:**

1. **Core (Núcleo)**
Oferece uma interface que permite a construção de consultas SQL de forma programática e controlada.
Você pode escrever SQL de maneira declarativa, mas ainda tem acesso direto ao SQL gerado.
Ideal para desenvolvedores que precisam de controle detalhado sobre as operações do banco de dados.

2. **ORM (Object-Relational Mapping)**
Mapeia tabelas do banco de dados para classes Python e suas colunas para atributos de classe.
Permite que você interaja com o banco de dados usando objetos Python em vez de SQL.
Facilita a criação, leitura, atualização e exclusão (CRUD) de registros no banco de dados com métodos Python.

#### Principais Componentes

1. **Engine:** Conecta-se ao banco de dados e é responsável por executar consultas SQL.

2. **Session:** Gerencia as operações de persistência de objetos no banco de dados, mantendo uma conversa com o banco de dados.

3. **Declarative Base:** Permite criar classes mapeadas para tabelas do banco de dados de forma declarativa.

4. **Query:** Utilizada para construir consultas e recuperar dados de forma orientada a objetos.

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Cria a engine e se conecta ao banco de dados
engine = create_engine('sqlite:///exemplo.db', echo=True)

# Base declarativa para mapeamento
Base = declarative_base()

# Define uma classe que será mapeada para uma tabela
class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)

# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Exemplo de criação e inserção de um novo usuário
novo_usuario = Usuario(nome="Maria", idade=30)
session.add(novo_usuario)
session.commit()

```
**Vantagens:**

**Abstração:** Esconde a complexidade do SQL, permitindo foco na lógica de negócios.
**Portabilidade:** Facilita a troca de bancos de dados sem alterar o código da aplicação.
**Escalabilidade:** Suporta transações complexas e consultas avançadas de forma eficiente.

#### Desvantagens:

**Curva de Aprendizado:** A abstração pode ser complexa para iniciantes.
**Performance:** Em casos muito específicos, pode ser menos performático do que SQL puro.


## 5684. APRESENTAÇÃO

- Nesse modulo veremos como instalar e configurar esse ORM.

## 5685. REFATORANDO O CODIGO DO PROJETO

- baixar o pacote mysqlclient -> pip install mysqlclient
- criar o diretorio: 
    - fabrica/ -> ira conter os arquivos __init.py__ e fabrica_conexao.py
    - entidades/ -> ira conter os arquivos __init.py__ e cliente.py
    - repositorios/ -> ira conter os arquivos __init.py__ e cliente_repositorio.py 

```bash
https://github.com/TREINAWEB/TREINAWEB-PYTHON-DATABASE-API
```
   
