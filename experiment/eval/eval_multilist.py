import os
import subprocess

experiment = 'cardet_20180424'


cfg_path = './experiment/%s/test.cfg' % experiment
weight_path = '/ssd/shizhixiang/models/best/%s.weights' % experiment


def gen_newdatafile(new_datafile_path, dataset):
    test_list = './experiment/eval/list/eval_%s.txt' % dataset

    with open(new_datafile_path, 'w') as filehandle:
        filehandle.write('classes= 1' + '\n')
        filehandle.write('train = ./experiment/%s/train.txt' % experiment + '\n')
        filehandle.write('valid = %s' % test_list + '\n')
        filehandle.write('names = ./experiment/%s/car.names' % experiment + '\n')
        filehandle.write('backup = /ssd/shizhixiang/models/%s/' % experiment)





for dataset in ['COCO', 'fifth', 'fourth', 'KITTI', 'seventh', 'sixth']:
    new_datafile_path = os.path.join(os.getwd(), 'car_%s.data' % dataset)
    get_newdatafile(new_datafile_path, dataset)

    full_log_file = './experiment/eval/eval_list_result/result_%s_%s.txt' % (dataset, experiment)
    eval_cmd = 'cd ../../ \n ./darknet detector map %s %s %s -dont_show 2>&1 | tee %s' % (new_datafile_path, cfg_path, weight_path, full_log_file)
    subprocess.call(eval_cmd, shell=True)
