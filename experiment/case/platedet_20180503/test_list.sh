experiment_case='platedet_20180503'

cd ../../

./darknet detector test \
./experiment/$experiment_case/plate.data \
./experiment/$experiment_case/test.cfg \
/ssd/shizhixiang/models/$experiment_case/train_34400.weights \
-dont_show < ./experiment/$experiment_case/minitest_ld.txt > ./experiment/$experiment_case/result.txt
