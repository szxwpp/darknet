import os
import subprocess

from analyze_result.experiment_config import experiment_config


cfg_path = '../case/%s/test.cfg' % experiment_config['experiment']
weight_path = '/ssd/shizhixiang/models/best/%s.weights' % experiment_config['experiment']
# weight_path = '/ssd/shizhixiang/models/%s/train_30680.weights' % experiment

def gen_newdatafile(new_datafile_path, dataset):
    test_list = './experiment/eval/list/minitest_%s.txt' % dataset

    with open(new_datafile_path, 'w') as filehandle:
        filehandle.write('classes= 1' + '\n')
        filehandle.write('train = ./experiment/%s/train.txt' % experiment_config['experiment'] + '\n')
        filehandle.write('valid = %s' % test_list + '\n')
        filehandle.write('names = ./experiment/%s/car.names' % experiment_config['experiment'] + '\n')
        filehandle.write('backup = /ssd/shizhixiang/models/%s/' % experiment_config['experiment'])



for dataset in ['COCO', 'fifth', 'fourth', 'KITTI', 'seventh', 'sixth']:
    new_datafile_path = os.path.join(os.getcwd(), 'car_%s.data' % dataset)
    gen_newdatafile(new_datafile_path, dataset)

    full_log_file = './experiment/eval/eval_list_result/%s_%s.txt' % (experiment_config['experiment'], dataset)
    eval_cmd = 'cd ../../ \n ./darknet detector map %s %s %s -dont_show 2>&1 | tee %s' % (new_datafile_path, cfg_path, weight_path, full_log_file)
    subprocess.call(eval_cmd, shell=True)
