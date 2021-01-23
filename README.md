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
  "verbose": 1
}
```
_verbose_ - to display information during different operations


## Commands
* `sfc-create-db-table` - creates *bins* table in database
* `sfc-delete-db-table` - deletes *bins* table in database
* `sfc-calculate-fold` - calculates fold and writes it to CSV file

## How to use it



