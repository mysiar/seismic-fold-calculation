import json

from SeismicFoldDbGis.FoldDbGis import FoldDbGis
from sqlalchemy import create_engine


def create_db_table(db_url: str):
    engine = create_engine(db_url, echo=True)
    fold = FoldDbGis(db_engine=engine)
    fold.create_table()


def delete_db_table(db_url: str):
    engine = create_engine(db_url, echo=True)
    fold = FoldDbGis(db_engine=engine)
    fold.delete_table()


def usage(text: str):
    print('Params required: ' + text)


def read_project_file(filename: str):
    file = open(filename, "r")
    result = json.load(file)
    file.close()
    return result
