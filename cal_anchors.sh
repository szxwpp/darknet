#!/bin/bash

./darknet detector calc_anchors ./experiment/cardet_20180419/car.data -num_of_clusters 9 -width 416 -heigh 416

# ./darknet detector calc_anchors ./experiment/cardet_20180415/car.data -num_of_clusters 5 -final_width 13 -final_heigh 13


# ./darknet detector calc_anchors ./experiment/cardet_20180417/car.data -num_of_clusters 9 -final_width 13 -final_heigh 13

