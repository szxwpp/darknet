import os
import subprocess

experiment = 'cardet_20180425'


cfg_path = './experiment/%s/test.cfg' % experiment
data_path = './experiment/%s/car.data' % experiment
models_dir = '/ssd/shizhixiang/models'
weight_dir = os.path.join(models_dir, experiment)
eval_log_dir = os.path.join(weight_dir, 'eval_log')


if not os.path.exists(eval_log_dir):
    os.mkdir(eval_log_dir)
evaled_files = os.listdir(eval_log_dir)
if not os.path.exists(eval_log_dir):
    os.mkdir(eval_log_dir)

for weight_file in os.listdir(weight_dir):
    if 'weights' in weight_file:
    	full_weight_file = os.path.join(weight_dir, weight_file)
    	log_file = weight_file.replace('.weights', '.log')
    
    	if log_file in evaled_files:
        	continue
    	else:
        	full_log_file = os.path.join(eval_log_dir, log_file)
        	eval_cmd = 'cd ../../ \n ./darknet detector map %s %s %s -dont_show 2>&1 | tee %s' % (data_path, cfg_path, full_weight_file, full_log_file)
        	subprocess.call(eval_cmd, shell=True)

    else:
    	pass
