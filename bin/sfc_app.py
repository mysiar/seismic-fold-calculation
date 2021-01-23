import json
from sqlalchemy import create_engine

from SeismicFoldDbGis.FoldDbGis import FoldDbGis
from FixedWidthTextParser.Seismic.SpsParser import Sps21Parser
from SeismicFold.Grid import Grid
from SeismicFold.Fold import Fold

DB_URL = 'db_url'
GRID = 'grid_file'
SPS = 'sps_file'
RPS = 'rps_file'
XPS = 'xps_file'
VERBOSE = 'verbose'


def create_db_table(prj_file: str):
    prj = read_project_file(prj_file)
    engine = create_engine(prj[DB_URL], echo=bool(prj[VERBOSE]))
    fold = FoldDbGis(db_engine=engine)
    fold.create_table()


def delete_db_table(prj_file: str):
    prj = read_project_file(prj_file)
    engine = create_engine(prj[DB_URL], echo=bool(prj[VERBOSE]))
    fold = FoldDbGis(db_engine=engine)
    fold.delete_table()


def usage(text: str):
    print('Params required: ' + text)


def read_project_file(filename: str):
    file = open(filename, "r")
    result = json.load(file)
    file.close()
    return result


def calculate_fold(prj_file: str, fold_csv_file: str):
    prj = read_project_file(prj_file)
    parser = Sps21Parser()
    grid = Grid()
    grid.read(prj['grid_file'])
    fold = Fold(
        grid=grid,
        parser=parser,
        sps_file=prj['sps_file'],
        rps_file=prj['rps_file'],
        xps_file=prj['xps_file'],
        verbose=bool(prj['verbose'])
    )

    fold.load_data()
    fold.calculate_fold()
    fold.write_fold2csv(fold_csv_file)
