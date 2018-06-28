experiment_case='cardet_20180628'

cd ../../

# ./darknet detector train \
# ./experiment/case/$experiment_case/car.data \
# ./experiment/case/$experiment_case/train.cfg \
# ./models/darknet53.conv.74 \
# -gpus 3 2>&1 | tee ./experiment/case/$experiment_case/pre900.log


./darknet detector train \
./experiment/case/$experiment_case/car.data \
./experiment/case/$experiment_case/train.cfg \
/ssd/shizhixiang/models/car_detection/$experiment_case/train_900.weights \
-gpus 0,1,2,3 2>&1 | tee ./experiment/case/$experiment_case/after900.log
