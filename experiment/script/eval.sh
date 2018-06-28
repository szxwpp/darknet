experiment_case='cardet_20180628'

cd ../../

#./darknet detector map \
#./experiment/eval/car.data \
#./experiment/eval/cardet_20180414_test.cfg \
#/ssd/shizhixiang/models/best/cardet_20180414.weights \
#-dont_show 2>&1 | tee ./experiment/eval/cardet_20180414.log


./darknet detector map \
./experiment/case/$experiment_case/car.data \
./experiment/case/$experiment_case/test.cfg \
/ssd/shizhixiang/models/car_detection/$experiment_case/train_final.weights \
-dont_show 2>&1 | tee ./experiment/case/$experiment_case/eval.log
