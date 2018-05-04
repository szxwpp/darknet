experiment_case='platedet_20180504'

# cd ../../

# ./darknet detector train \
# ./experiment/$experiment_case/plate.data \
# ./experiment/$experiment_case/train.cfg \
# /ssd/shizhixiang/models/best/cardet_20180416.conv.74 \
# -gpus 3 2>&1 | tee ./experiment/$experiment_case/pre1000.log



cd ../../

./darknet detector train \
./experiment/$experiment_case/plate.data \
./experiment/$experiment_case/train.cfg \
/ssd/shizhixiang/models/platedet_20180504/train_2400.weights \
-gpus 2,3 2>&1 | tee ./experiment/$experiment_case/train.log
