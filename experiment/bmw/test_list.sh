# cd ../../

# ./darknet detector test \
# ./experiment/cardet_20180414/car.data \
# ./experiment/cardet_20180414/test.cfg \
# /ssd/shizhixiang/models/cardet_20180414/train_20900.weights \
# -dont_show < filelist.txt > result.txt

cd ../../

./darknet detector test \
./experiment/cardet_20180414/car.data \
./experiment/eval/bmw_cardet_test.cfg \
/ssd/shizhixiang/models/best/bmw_cardet.weights \
-dont_show < filelist.txt > result.txt
