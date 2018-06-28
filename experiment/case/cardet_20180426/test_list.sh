experiment_case='cardet_20180426'

cd ../../

./darknet detector test \
./experiment/$experiment_case/car.data \
./experiment/$experiment_case/test.cfg \
/ssd/shizhixiang/models/$experiment_case/train_34400.weights \
-dont_show < ./experiment/$experiment_case/minitest_ld.txt > ./experiment/$experiment_case/result.txt
