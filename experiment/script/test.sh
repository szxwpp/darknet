experiment_case='cardet_20180628'

cd ../../

# test a filelist
./darknet detector test \
./experiment/case/$experiment_case/car.data \
./experiment/case/$experiment_case/test.cfg \
/ssd/shizhixiang/models/car_detection/$experiment_case/train_final.weights \
-dont_show < ./experiment/case/$experiment_case/test.txt > ./experiment/case/$experiment_case/result.txt


# test a file
# ./darknet detector test \
# ./experiment/case/$experiment_case/car.data \
# ./experiment/case/$experiment_case/test.cfg \
# /ssd/shizhixiang/models/car_detection/$experiment_case/train_final.weights \
# /ssd/shizhixiang/dataset/Cars/test/images/00001.jpg
