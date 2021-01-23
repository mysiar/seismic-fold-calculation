import json
from sqlalchemy import create_engine
from sqlalchemy.event import listen

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

POSTGRES = 'postgresql'
SQLITE = 'sqlite'
SPATIALITE_EXT = '/usr/lib/x86_64-linux-gnu/mod_spatialite.so'


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
    fold = FoldDbGis(db_engine=engine, verbose=bool(prj[VERBOSE]))
    fold.load_from_csv(fold_csv_file)


def fold_db_update(prj_file: str, fold_csv_file: str):
    prj = read_project_file(prj_file)
    engine = _create_db_engine(db_url=prj[DB_URL], db_verbose=bool(prj[DB_VERBOSE]))
    fold = FoldDbGis(db_engine=engine, verbose=bool(prj[VERBOSE]))
    fold.update_from_csv(fold_csv_file)


def _create_db_engine(db_url: str, db_verbose: bool):
    db_type = db_url.split(":")[0]
    if POSTGRES == db_type:
        return create_engine(db_url, echo=db_verbose)
    elif SQLITE == db_type:
        engine = create_engine(db_url, echo=db_verbose)
        listen(engine, 'connect', _load_spatialite)
        return engine
    else:
        raise Exception('Not supported/tested DB engine: {}'.format(db_type))


def _load_spatialite(dbapi_conn, connection_record):
    dbapi_conn.enable_load_extension(True)
    dbapi_conn.load_extension(SPATIALITE_EXT)


def timer(start, end):
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds)
