experiment_case='cardet_20180426'

# cd ../../

# ./darknet detector train \
# ./experiment/cardet_20180420/car.data \
# ./experiment/cardet_20180420/train.cfg \
# ./models/darknet19_448.conv.23 \
# -dont_show -gpus 4 2>&1 | tee ./experiment/cardet_20180420/pre1000.log



cd ../../

./darknet detector train \
./experiment/$experiment_case/car.data \
./experiment/$experiment_case/train.cfg \
/ssd/shizhixiang/models/best/cardet_20180423.conv.105 \
-dont_show -gpus 3 2>&1 | tee ./experiment/$experiment_case/train.log
