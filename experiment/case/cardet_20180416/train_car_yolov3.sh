# cd ../../

# ./darknet detector train \
# ./experiment/cardet_20180416/car.data \
# ./experiment/cardet_20180416/yolov3-car.cfg \
# /ssd/shizhixiang/models/cardet_20180416/yolov3-car_1000.weights \
# -dont_show -gpus 1,2 2>&1 | tee ./experiment/cardet_20180416/after1000.log

cd ../../

./darknet detector train \
./experiment/cardet_20180416/car.data \
./experiment/cardet_20180416/yolov3-car.cfg \
/ssd/shizhixiang/models/cardet_20180416/yolov3-car_36652.weights \
-dont_show -gpus 4,5,6 2>&1 | tee ./experiment/cardet_20180416/after36652.log
