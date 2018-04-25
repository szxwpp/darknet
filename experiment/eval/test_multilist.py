import os
import subprocess

experiment = 'cardet_20180423'


cfg_path = './experiment/%s/test.cfg' % experiment
data_path = './experiment/%s/car.data' % experiment
weight_path = '/ssd/shizhixiang/models/best/%s.weights' % experiment


for dataset in ['COCO', 'fifth', 'fourth', 'KITTI', 'seventh', 'sixth']:
    test_list = './experiment/eval/list/eval_%s.txt' % dataset
    result = './experiment/eval/test_list_result/result_%s_%s.txt' % (dataset, experiment)

    eval_cmd = 'cd ../../ \n ./darknet detector test %s %s %s -dont_show < %s > %s' % (data_path, cfg_path, weight_path, test_list, result)
    subprocess.call(eval_cmd, shell=True)
