cd ../../

./darknet detector train \
./experiment/cardet_20180418/car.data \
./experiment/cardet_20180418/train.cfg \
/ssd/shizhixiang/models/cardet_20180418/train_7440.weights \
-dont_show -gpus 4,5,6 2>&1 | tee ./experiment/cardet_20180418/after7440.log


# cd ../../

# ./darknet detector train \
# ./experiment/cardet_20180414/car.data \
# ./experiment/cardet_20180414/train.cfg \
# /ssd/shizhixiang/models/cardet_20180414/train_2200.weights \
# -dont_show -gpus 4 2>&1 | tee ./experiment/cardet_20180414/after2200.log
