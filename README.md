# Seismic fold calculation - cli scripts

## Install
* clone repository `git clone https://github.com/mysiar/seismic-fold-calculation-cli.git`
* `cd seismic-fold-calculation-cli`
* `sh install.sh`

## Project file definition
```json
{
  "db_url": "postgresql://user:password@db_host/db_fold",
  "grid_file": "grid.json",
  "sps_file": "your SPS source file",
  "rps_file": "your SPS receiver file",
  "xps_file": "your SPS relation file",
  "verbose": 1,
  "db_verbose": 1,
}
```
* _verbose_ - to display information during different operations
* _db_verbose_ - SQLAlchemy echo

## Commands
* `sfc-create-db-table` - creates *bins* table in database
* `sfc-delete-db-table` - deletes *bins* table in database
* `sfc-calculate-fold` - calculates fold and writes it to CSV file
* `sfc-db-fold-load` - load fold from CSV file to db
* `sfc-db-fold-update` - update fold from CSV file to db

## How to use it

### Scenario 1 - single SPS data set
* create Spatial DB (PostgreSQL or SQLite)
* create bins table `sfc-create-db-table` 
* create project
* calculate fold `sfc-calculate-fold`
* load fold to db `sfc-db-fold-load`

### Scenario 2 - multiple SPS data set
* TODO


### Tests
* to run `tests/test.sh` you need to create spatial SQLite db using `spatialite tests/data/fold.sqlite`

## More info

* [Seismic Fold](https://github.com/mysiar/seismic-fold-python-package)
* [Seismic Fold Db GIS](https://github.com/mysiar/seismic-fold_db_gis-python-package)


