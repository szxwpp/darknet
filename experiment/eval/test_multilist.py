import os
import subprocess

experiment = 'cardet_20180425'


cfg_path = './experiment/%s/test.cfg' % experiment
data_path = './experiment/%s/car.data' % experiment
weight_path = '/ssd/shizhixiang/models/best/%s.weights' % experiment


for dataset in ['COCO', 'first', 'second', 'third', 'fourth', 'fifth', 'KITTI', 'seventh', 'sixth']:
    test_list = './experiment/eval/list/minitest_%s.txt' % dataset
    result = './experiment/eval/test_list_result/%s_%s.txt' % (experiment, dataset)

    eval_cmd = 'cd ../../ \n ./darknet detector test %s %s %s -dont_show < %s > %s' % (data_path, cfg_path, weight_path, test_list, result)
    subprocess.call(eval_cmd, shell=True)
