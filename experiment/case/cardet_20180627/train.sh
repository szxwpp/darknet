experiment_case='cardet_20180627'

# cd ../../

# ./darknet detector train \
# ./experiment/$experiment_case/car.data \
# ./experiment/$experiment_case/train.cfg \
# -gpus 3 2>&1 | tee ./experiment/$experiment_case/pre1000.log



cd ../../

./darknet detector train \
./experiment/$experiment_case/car.data \
./experiment/$experiment_case/train.cfg \
/ssd/shizhixiang/models/car_detection/$experiment_case/train_4400.weights \
-gpus 0,1,2,3 2>&1 | tee ./experiment/$experiment_case/after4400.log
