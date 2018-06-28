import os
import random
import math

from analyze_result.experiment_config import experiment_config


def CreateDataset(imgsfile_list, ratio, target_dir):
    random.shuffle(imgsfile_list)
    num_train = random.sample(imgsfile_list, int(math.floor(
        len(imgsfile_list) * ratio[0] / (ratio[0] + ratio[1]))))
    num_test = list(set(imgsfile_list).difference(set(num_train)))

    print('ratio of train:test ', ratio)
    print(
        'number of train:test:all',
        len(num_train),
        len(num_test),
        len(imgsfile_list))

    for splite in ['train', 'test']:
        with open(os.path.join(target_dir, '%s.txt' % splite), 'w') as filehandle:
            for item in eval('num_' + splite):
                if '\n' in item:
                    filehandle.write(item)
                else:
                    filehandle.write(item + '\n')


dataset_list = ['../case/%s/all.txt' % experiment_config['experiment']]
ratio = [95.0, 5.0]
for dataset_path in dataset_list:
    target_dir = os.path.dirname(dataset_path)
    with open(dataset_path, 'r') as filehandle:
        imgsfile_list = filehandle.readlines()
    CreateDataset(imgsfile_list, ratio, target_dir)
