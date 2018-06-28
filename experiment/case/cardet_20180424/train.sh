# cd ../../

# ./darknet detector train \
# ./experiment/cardet_20180420/car.data \
# ./experiment/cardet_20180420/train.cfg \
# ./models/darknet19_448.conv.23 \
# -dont_show -gpus 4 2>&1 | tee ./experiment/cardet_20180420/pre1000.log


cd ../../

./darknet detector train \
./experiment/cardet_20180424/car.data \
./experiment/cardet_20180424/train.cfg \
/ssd/shizhixiang/models/best/cardet_20180416.conv.74 \
-dont_show -gpus 0 2>&1 | tee ./experiment/cardet_20180424/pre1000.log
