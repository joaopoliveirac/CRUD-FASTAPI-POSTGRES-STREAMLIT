from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_DATABASE_URL = 'postgresql://user:password@postgres/mydatabase'

engine = create_engine(POSTGRES_DATABASE_URL) 

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal() #criar sessões que se conectam ao banco de dados especificado no engine
    try:
        yield db #Em vez de retornar um valor imediatamente (como com return), ele entrega o controle para quem está usando a função.( A sessão criada (session) é entregue para o código que chama a função. Isso permite executar operações no banco de dados com essa sessão.)
    finally: #: O bloco finally é executado sempre, independentemente de o código no try ter sucesso ou falhar
        db.close() # Fecha a conexão com o banco de dados, liberando recursos. Isso é importante para evitar vazamentos de conexão




