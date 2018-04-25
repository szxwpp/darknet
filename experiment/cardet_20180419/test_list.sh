cd ../../

./darknet detector test \
./experiment/cardet_20180419/car.data \
./experiment/cardet_20180419/test.cfg \
/ssd/shizhixiang/models/cardet_20180419/train_34400.weights \
-dont_show < minitestlist.txt > ./experiment/cardet_20180419/result.txt
