from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "mysql+pymysql://Tech0Gen8TA2:gen8-1-ta@2@tech0-gen-8-step4-db-2.mysql.database.azure.com/class2_db"

username = "Tech0Gen8TA2"
password = "gen8-1-ta%402"   #gen8-1-ta@2
server_name = "tech0-gen-8-step4-db-2.mysql.database.azure.com"
db_name = "class2_db"
path = "C:\\Users\\toshi\\ASPASIO Dropbox\\suezawa toshihiro\\Suezawa\\Tech0\\★★★_2501181223_Step4\\DigiCertGlobalRootCA.crt.pem"

# DATABASE_URL = f"mysql+pymysql://{username}:{password}@{server_name}/{db_name}??ssl_disabled=true"

DATABASE_URL = f"mysql+pymysql://{username}:{password}@{server_name}/{db_name}?ssl_ca={path}"

#    ーDBについてー
# 　名前：tech0-gen-8-step4-db-2
# 　管理者：Tech0Gen8TA2
# 　PASS：gen8-1-ta@2


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()