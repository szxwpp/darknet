cd ../../

./darknet detector test \
./experiment/cardet_20180415/car.data \
./experiment/cardet_20180415/test.cfg \
/ssd/shizhixiang/models/cardet_20180415/train_30400.weights \
-dont_show < filelist.txt > result.txt
