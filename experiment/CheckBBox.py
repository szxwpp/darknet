import os
import cv2

root_dir = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".")
imgslist_path = os.path.join(root_dir, 'filelist.txt')


with open(imgslist_path, 'r') as filehandle:
    imgs_filelist = filehandle.readlines()
imgs_count = len(imgs_filelist)


def GetLabelsPath(full_imgpath, split):
    img_dir = os.path.dirname(full_imgpath)
    img_name = os.path.basename(full_imgpath)
    label_name = '%s.txt' % (os.path.splitext(img_name)[0])
    label_dir = img_dir.replace('JPEGImages', split)

    label_filepath = os.path.join(label_dir, label_name)

    return label_filepath


def GetBBox(width, height, line):
    line_seperate = line.strip().split(' ')
    x = float(line_seperate[1])
    y = float(line_seperate[2])
    w = float(line_seperate[3])
    h = float(line_seperate[4])

    left = int((x - w / 2) * width)
    right = int((x + w / 2) * width)
    top = int((y - h / 2) * height)
    down = int((y + h / 2) * height)

    if left < 0:
        left = 0
    if right > width - 1:
        right = width - 1
    if top < 0:
        top = 0
    if down > height - 1:
        down = height - 1

    if len(line_seperate) == 5:
        return [left, top, right, down]
    elif len(line_seperate) == 6:
        return [left, top, right, down, int(line_seperate[5])]
    else:
        print('wrong label')



for index in range(imgs_count):
    print(imgs_filelist[index].replace('\n', ''))
    full_imgpath = os.path.join(root_dir, imgs_filelist[index].replace('\n', ''))
    img = cv2.imread(full_imgpath)

    if img is None:
        raise Exception('fail to load img: %s' % full_imgpath)
    else:
        height, width, chanels = img.shape
        print('width %d, height %d' % (width, height))

    # ground truth
    with open(GetLabelsPath(full_imgpath, 'labels'), 'r') as label_filehandle:
        lines = label_filehandle.readlines()
        print('ground truth: %d' % len(lines))
        for line in lines:
            bb = GetBBox(width, height, line)
            cv2.rectangle(img, (bb[0], bb[1]), (bb[2], bb[3]), (55, 255, 155), 3)

    # result bbox
    with open(GetLabelsPath(full_imgpath, 'resultlabels'), 'r') as label_filehandle:
        lines = label_filehandle.readlines()
        print('result bbox: %d' % len(lines))
        for line in lines:
            bb = GetBBox(width, height, line)
            if bb[4] >= 90:
                cv2.rectangle(img, (bb[0], bb[1]), (bb[2], bb[3]), (255, 0, 255), 3)
                cv2.putText(img, 'Car:%.2f'% (bb[4]/100), (bb[2]-150, bb[1]+30), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 255), 1, False)

    cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)
    cv2.imshow('img', img)
    key = cv2.waitKey(0)

    if key == 99:
        cv2.destroyAllWindows()
        break

cv2.destroyAllWindows()