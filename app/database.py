import sqlalchemy
import configparser
import pandas

config = configparser.ConfigParser()
config.read("./config.ini")

ORACLE_HOST = config["DATABASE"]["ORACLE_HOST"]
ORACLE_PORT = config["DATABASE"]["ORACLE_PORT"]
ORACLE_SERVICE = config["DATABASE"]["ORACLE_SERVICE"]
ORACLE_USER = config["DATABASE"]["ORACLE_USER"]
ORACLE_PASS = config["DATABASE"]["ORACLE_PASS"]
CHUNK_SIZE = int(config["DATABASE"]["ORACLE_CHUNK_SIZE"])
CONN_URL = f"oracle+oracledb://{ORACLE_USER}:{ORACLE_PASS}@{ORACLE_HOST}:{ORACLE_PORT}/?service_name={ORACLE_SERVICE}"

engine = sqlalchemy.create_engine(CONN_URL).execution_options(stream_results=True)


def ejecutar_consulta(sql: str) -> pandas.DataFrame:
    with engine.connect() as conn:
        for chunk_data in pandas.read_sql(
            sqlalchemy.text(sql), conn, chunksize=CHUNK_SIZE
        ):
            yield chunk_data
