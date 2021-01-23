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
DB_VERBOSE = 'db_verbose'


def db_table_create(prj_file: str):
    prj = read_project_file(prj_file)
    engine = _create_db_engine(db_url=prj[DB_URL], db_verbose=bool(prj[DB_VERBOSE]))
    fold = FoldDbGis(db_engine=engine)
    fold.create_table()


def db_table_delete(prj_file: str):
    prj = read_project_file(prj_file)
    engine = _create_db_engine(db_url=prj[DB_URL], db_verbose=bool(prj[DB_VERBOSE]))
    fold = FoldDbGis(db_engine=engine)
    fold.delete_table()


def usage(text: str):
    print('Params required: ' + text)


def read_project_file(filename: str):
    file = open(filename, "r")
    result = json.load(file)
    file.close()
    return result


def fold_calculate(prj_file: str, fold_csv_file: str):
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


def fold_db_load(prj_file: str, fold_csv_file: str):
    prj = read_project_file(prj_file)
    engine = _create_db_engine(db_url=prj[DB_URL], db_verbose=bool(prj[DB_VERBOSE]))
    fold = FoldDbGis(db_engine=engine, verbose=prj[VERBOSE])
    fold.load_from_csv(fold_csv_file)


def fold_db_update(prj_file: str, fold_csv_file: str):
    prj = read_project_file(prj_file)
    engine = _create_db_engine(db_url=prj[DB_URL], db_verbose=bool(prj[DB_VERBOSE]))
    fold = FoldDbGis(db_engine=engine, verbose=prj[VERBOSE])
    fold.update_from_csv(fold_csv_file)


def _create_db_engine(db_url: str, db_verbose: bool):
    # TODO : sqlite
    engine = create_engine(db_url, echo=db_verbose)
    return engine
