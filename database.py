from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# .env ファイルから環境変数を読み込む
load_dotenv()

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
server_name = os.getenv("DB_SERVER")
db_name = os.getenv("DB_NAME")
path = os.getenv("SSL_PATH")


# DATABASE_URL = f"mysql+pymysql://{username}:{password}@{server_name}/{db_name}?ssl_ca={path}"

DATABASE_URL = f"mysql+pymysql://{username}:{password}@{server_name}/{db_name}?ssl_disabled=true"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()