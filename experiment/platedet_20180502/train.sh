experiment_case='platedet_20180502'

# cd ../../

# ./darknet detector train \
# ./experiment/cardet_20180420/car.data \
# ./experiment/cardet_20180420/train.cfg \
# ./models/darknet19_448.conv.23 \
# -dont_show -gpus 4 2>&1 | tee ./experiment/cardet_20180420/pre1000.log



cd ../../

./darknet detector train \
./experiment/$experiment_case/plate.data \
./experiment/$experiment_case/train.cfg \
/ssd/shizhixiang/models/platedet_20180502/train_16344.weights \
-dont_show -gpus 0 2>&1 | tee ./experiment/$experiment_case/pre1000.log
