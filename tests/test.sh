unzip -o tests/data/TestZipper.zip -d tests/data/
echo "Calculate fold for Zipper 1"
./bin/sfc-fold-calculate tests/data/TestZipper1.prj tests/data/TestZipper1.fold.csv
echo "Calculate fold for Zipper 2"
./bin/sfc-fold-calculate tests/data/TestZipper2.prj tests/data/TestZipper2.fold.csv
echo "Create 'bins' table"
./bin/sfc-db-table-create tests/data/TestZipper1.prj
echo "Load fold of Zipper 1 to DB"
./bin/sfc-db-fold-load tests/data/TestZipper1.prj tests/data/TestZipper1.fold.csv
echo "Load fold of Zipper 2 to DB - update"
./bin/sfc-db-fold-update tests/data/TestZipper1.prj tests/data/TestZipper2.fold.csv
echo "Delete 'bins' table"
./bin/sfc-db-table-delete tests/data/TestZipper1.prj
