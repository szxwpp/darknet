experiment_case='platedet_20180506'

cd ../../

# ./darknet detector train \
# ./experiment/$experiment_case/plate.data \
# ./experiment/$experiment_case/train.cfg \
# -gpus 2 2>&1 | tee ./experiment/$experiment_case/pre1000.log

./darknet detector train \
./experiment/$experiment_case/plate.data \
./experiment/$experiment_case/train.cfg \
/ssd/shizhixiang/models/best/platedet_20180503.weights \
-gpus 1 2>&1 | tee ./experiment/$experiment_case/train.log


# ./darknet detector train \
# ./experiment/$experiment_case/plate.data \
# ./experiment/$experiment_case/train.cfg \
# /ssd/shizhixiang/models/platedet_20180502/train_16344.weights \
# -gpus 3 2>&1 | tee ./experiment/$experiment_case/pre1000.log
