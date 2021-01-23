unzip tests/data/test-simple.fold.zip -d tests/data/
echo "Create 'bins' table"
./bin/sfc-db-table-create tests/data/test-project.json
echo "Load fold to db"
./bin/sfc-db-fold-load tests/data/test-project.json tests/data/test-simple.fold.csv
echo "Update fold in db"
./bin/sfc-db-fold-update tests/data/test-project.json tests/data/test-simple.fold.csv
echo "Delete 'bins' table"
./bin/sfc-db-table-delete tests/data/test-project.json
rm tests/data/test-simple.fold.csv