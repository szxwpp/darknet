cd ../../

./darknet detector test \
./experiment/cardet_20180420/car.data \
./experiment/cardet_20180420/test.cfg \
/ssd/shizhixiang/models/cardet_20180420/train_34400.weights \
-dont_show < ./experiment/cardet_20180420/minitest.txt > ./experiment/cardet_20180420/result.txt
