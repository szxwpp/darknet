cd ../../

./darknet detector test \
./experiment/cardet_20180413/car.data \
./experiment/cardet_20180413/test.cfg \
/ssd/shizhixiang/models/cardet_20180413/train_34400.weights \
-dont_show < filelist.txt > result.txt
