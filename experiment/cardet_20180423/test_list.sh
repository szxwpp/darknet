cd ../../

./darknet detector test \
./experiment/cardet_20180423/car.data \
./experiment/cardet_20180423/test.cfg \
/ssd/shizhixiang/models/cardet_20180423/train_34400.weights \
-dont_show < ./experiment/cardet_20180423/minitest_ld.txt > ./experiment/cardet_20180423/result.txt
