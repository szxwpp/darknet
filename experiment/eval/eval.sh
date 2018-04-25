#cd ../../

#./darknet detector map \
#./experiment/eval/car.data \
#./experiment/eval/cardet_20180414_test.cfg \
#/ssd/shizhixiang/models/best/cardet_20180414.weights \
#-dont_show 2>&1 | tee ./experiment/eval/cardet_20180414.log

cd ../../

./darknet detector map \
./experiment/eval/car.data \
./experiment/eval/bmw_cardet_test.cfg \
/ssd/shizhixiang/models/best/bmw_cardet.weights \
-dont_show 2>&1 | tee ./experiment/eval/bmw_cardet.log
