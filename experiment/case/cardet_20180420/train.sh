# cd ../../

# ./darknet detector train \
# ./experiment/cardet_20180420/car.data \
# ./experiment/cardet_20180420/train.cfg \
# ./models/darknet19_448.conv.23 \
# -dont_show -gpus 4 2>&1 | tee ./experiment/cardet_20180420/pre1000.log


cd ../../

./darknet detector train \
./experiment/cardet_20180420/car.data \
./experiment/cardet_20180420/train.cfg \
/ssd/shizhixiang/models/cardet_20180420/train_2300.weights \
-dont_show -gpus 4,5,6,7 2>&1 | tee ./experiment/cardet_20180420/after2300.log
