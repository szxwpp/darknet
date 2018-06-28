experiment_case='cardet_20180627'

cd ../../

./darknet detector test \
./experiment/$experiment_case/car.data \
./experiment/$experiment_case/test.cfg \
/ssd/shizhixiang/models/car_detection/$experiment_case/train_34400.weights \
-dont_show < ./experiment/$experiment_case/test.txt > ./experiment/$experiment_case/result.txt
