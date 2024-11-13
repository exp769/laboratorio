from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://admin:3SGxjKDL3UuESNo7ztPAMWn7hs4d0MXq@dpg-csptg5pu0jms73fkbs1g-a.oregon-postgres.render.com/example_postgresql_beaver_4mtl"

engine = create_engine(
    DATABASE_URL
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


if __name__ == "__main__":
    try:
        db = SessionLocal()
        print("conexão feita")
    except Exception as e:
        print("Erro ao conectar com o banco de dados:", e)
    finally:
        db.close()
