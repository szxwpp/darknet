# cd ../../

# ./darknet detector test \
# ./experiment/cardet_20180418/car.data \
# ./experiment/cardet_20180418/test.cfg \
# /ssd/shizhixiang/models/best/cardet_20180418.weights \
# -dont_show < ./experiment/cardet_20180418/minitest_sd.txt > ./experiment/cardet_20180418/result.txt

cd ../../

./darknet detector test \
./experiment/cardet_20180424/car.data \
./experiment/cardet_20180424/test.cfg \
/ssd/shizhixiang/models/cardet_20180424/yolov3-car_33628.weights \
-dont_show < ./experiment/cardet_20180424/minitest_ld.txt > ./experiment/cardet_20180424/result.txt
