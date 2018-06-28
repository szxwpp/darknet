cd ../../

./darknet detector train \
./experiment/cardet_20180413/car.data \
./experiment/cardet_20180413/train.cfg \
-dont_show -gpus 2 2>&1 | tee ./experiment/cardet_20180413/pre1000.log


# cd ../../

# ./darknet detector train \
# ./experiment/cardet_20180414/car.data \
# ./experiment/cardet_20180414/train.cfg \
# /ssd/shizhixiang/models/cardet_20180414/train_2200.weights \
# -dont_show -gpus 4 2>&1 | tee ./experiment/cardet_20180414/after2200.log
