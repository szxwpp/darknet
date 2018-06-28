import os

from analyze_result.experiment_config import experiment_config

label_str = 'Car'
target_filepath = '../case/%s/result.txt' % experiment_config['experiment']


def GetLabelFilePath(line):
    line_seperate = line.strip().split(':')
    img_path = line_seperate[1].strip()

    img_name = os.path.basename(img_path)
    img_name_seperate = os.path.splitext(img_name)
    label_name = '%s.txt' % img_name_seperate[0]

    img_dir = os.path.dirname(img_path)
    label_dir = img_dir.replace('images', 'resultlabels')
    label_dir = label_dir.replace('JPEGImages', 'resultlabels')
    if not os.path.exists(label_dir):
        os.makedirs(label_dir)

    target_path = os.path.join(label_dir, label_name)

    return target_path


def GetBBox(line):
    line_seperate = line.strip().split(':')
    bbox_seperate = line_seperate[1].strip().split(' ')
    predict = bbox_seperate[0]
    del bbox_seperate[0]
    bbox_seperate.append(predict)
    return ' '.join(val for val in bbox_seperate)


with open(target_filepath, 'r') as filehandle:
    lines = filehandle.readlines()
lines_count = len(lines)

pre_bbox_count = 0
pre_file_count = 0
for i in range(lines_count-1):
    pre_file_count += lines[i].count('Enter Image Path')
    pre_bbox_count += lines[i].count(label_str)

count = 0
bbox_count = 0
file_count = 0
while count < lines_count-1:
    if 'Enter Image Path' in lines[count]:
        label_filepath = GetLabelFilePath(lines[count])
        count += 1
        with open(label_filepath, 'w') as label_filehandle:
            file_count += 1
            while 'Enter Image Path' not in lines[count] :
                if 'Car' in lines[count]:
                    label_filehandle.write('0 ' + GetBBox(lines[count]) + '\n')
                    bbox_count += 1
                count += 1
    else:
        count += 1

if pre_bbox_count != bbox_count or pre_file_count != file_count:
    print('wrong, pre_bbox_count: %d, bbox_count: %d, pre_file_count: %d, file_count: %d' % (pre_bbox_count, bbox_count, pre_file_count, file_count))
