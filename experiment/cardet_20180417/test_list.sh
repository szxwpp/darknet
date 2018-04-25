cd ../../

./darknet detector test \
./experiment/cardet_20180417/car.data \
./experiment/cardet_20180417/test.cfg \
/ssd/shizhixiang/models/cardet_20180417/train_34400.weights \
-dont_show < filelist.txt > ./experiment/cardet_20180417/result.txt
