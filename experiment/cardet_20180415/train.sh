# cd ../../

# ./darknet detector train \
# ./experiment/cardet_20180415/car.data \
# ./experiment/cardet_20180415/train.cfg \
# ./models/yolov2-tiny.conv.13 \
# -dont_show -gpus 3 2>&1 | tee ./experiment/cardet_20180415/pre1000.log


# cd ../../

# ./darknet detector train \
# ./experiment/cardet_20180415/car.data \
# ./experiment/cardet_20180415/train.cfg \
# /ssd/shizhixiang/models/cardet_20180415/train_1900.weights \
# -dont_show -gpus 3 2>&1 | tee ./experiment/cardet_20180415/after1900.log

cd ../../

./darknet detector train \
./experiment/cardet_20180415/car.data \
./experiment/cardet_20180415/train.cfg \
/ssd/shizhixiang/models/cardet_20180415/train_6900.weights \
-dont_show -gpus 3 2>&1 | tee ./experiment/cardet_20180415/after6900.log
