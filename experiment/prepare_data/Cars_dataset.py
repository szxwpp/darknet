import scipy.io as sio
import os
import cv2
import numpy as np

from utils import DelOrCreate


def get_labels(anno_filepath, dataset_dir):
    data = sio.loadmat(anno_filepath)

    annotations = data['annotations']
    anno_shape = annotations.shape

    for index in range(anno_shape[1]):
        # print(annotations[0][index])
        try:
            bbox = []
            for i in range(4):
                bbox.append(float(annotations[0][index][i][0, 0]))
            filename = annotations[0][index][-1][0]

            img = cv2.imread(os.path.join(dataset_dir, filename))
            img_h, img_w, _ = img.shape

            x_center = (bbox[0] + bbox[2])/2.0/img_w
            y_center = (bbox[1] + bbox[3])/2.0/img_h
            w = (bbox[2] - bbox[0])/img_w
            h = (bbox[3] - bbox[1])/img_h
        except:
            print(annotations[0][index])

        label_dir = dataset_dir.replace('images', 'labels')
        label_name = filename.replace('jpg', 'txt')
        with open(os.path.join(label_dir, label_name), 'w') as filehandle:
            filehandle.write('0 ' + ' '.join([str(x_center), str(y_center), str(w), str(h)]) + '\n')




train_anno_filepath = r'/ssd/shizhixiang/dataset/Cars/devkit/cars_train_annos.mat'
train_images_dir = r'/ssd/shizhixiang/dataset/Cars/train/images'
test_anno_filepath = r'/ssd/shizhixiang/dataset/Cars/devkit/cars_test_annos.mat'
test_images_dir = r'/ssd/shizhixiang/dataset/Cars/test/images'
DelOrCreate(train_images_dir.replace('images', 'labels'))
DelOrCreate(test_images_dir.replace('images', 'labels'))


get_labels(train_anno_filepath, train_images_dir)
get_labels(test_anno_filepath, test_images_dir)