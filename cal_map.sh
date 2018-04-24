
# ./darknet detector map \
# ./experiment/experiment_LDCar/car.data \
# ./experiment/experiment_car/yolov3-car-anchors-test.cfg \
# /ssd/shizhixiang/models/best/yolov3-car-anchors_53968.weights \
# -dont_show -gpus 6

./darknet detector map \
./experiment/experiment_LDCar/car.data \
./experiment/experiment_car/yolov3-car-test.cfg \
/ssd/shizhixiang/models/best/yolov3-car_24408.weights \
-dont_show -gpus 6
