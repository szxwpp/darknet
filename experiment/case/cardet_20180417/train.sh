cd ../../

./darknet detector train \
./experiment/cardet_20180417/car.data \
./experiment/cardet_20180417/train.cfg \
/ssd/shizhixiang/models/cardet_20180417/train_3100.weights \
-dont_show -gpus 0,1 2>&1 | tee ./experiment/cardet_20180417/after3100.log


# cd ../../

# ./darknet detector train \
# ./experiment/cardet_20180414/car.data \
# ./experiment/cardet_20180414/train.cfg \
# /ssd/shizhixiang/models/cardet_20180414/train_2200.weights \
# -dont_show -gpus 4 2>&1 | tee ./experiment/cardet_20180414/after2200.log
