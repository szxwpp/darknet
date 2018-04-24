#./darknet detector test ./experiment/experiment_car/car.data ./experiment/experiment_car/yolov3-car-anchors-test.cfg /ssd/shizhixiang/models/yolov3_car/kitti_anchors/yolov3-car-anchors_53968.weights -dont_show -gpus 6 < filelist.txt > result.txt


# ./darknet detector test \
# ./experiment/experiment_car/car.data \
# ./experiment/experiment_car/yolov3-car-test.cfg \
# /ssd/shizhixiang/models/yolov3_car/kitti_yolov3/yolov3-car_24408.weights \
# -dont_show -gpus 0 < filelist1.txt > result1.txt

# ./darknet detector test \
# ./experiment/cardet_20180416/car.data \
# ./experiment/cardet_20180416/yolov3-car-test.cfg \
# /ssd/shizhixiang/models/cardet_20180416/yolov3-car_1000.weights \
# -dont_show < filelist7.txt > result7.txt

./darknet detector test \
./experiment/cardet_20180413/car.data \
./experiment/cardet_20180413/test.cfg \
/ssd/shizhixiang/models/cardet_20180413/train_1000.weights \
-dont_show < filelist1.txt > result1.txt

