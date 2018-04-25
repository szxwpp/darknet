cd ../../

./darknet detector test \
./experiment/cardet_20180414/car.data \
./experiment/cardet_20180414/test.cfg \
/ssd/shizhixiang/models/cardet_20180414/train_20900.weights \
-dont_show < filelist.txt > result.txt
