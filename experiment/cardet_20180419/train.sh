cd ../../

./darknet detector train \
./experiment/cardet_20180419/car.data \
./experiment/cardet_20180419/train.cfg \
/ssd/shizhixiang/models/best/yolov3_car.conv.74 \
-gpus 0 2>&1 | tee ./experiment/cardet_20180419/pre1000.log


