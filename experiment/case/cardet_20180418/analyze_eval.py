import os
import numpy as np
import matplotlib.pyplot as plt

log_dir = os.path.join(os.getcwd(), 'eval_log')


def str2float(str):
    if str == '-nan':
        return 0
    else:
        return float(str)


result={}
result_relief = []
for log_file in os.listdir(log_dir):
    if 'final' in log_file:
        iteration='40000'
    else:
        iteration = log_file.split('.')[0].split('_')[1]
    with open(os.path.join(log_dir, log_file), 'r') as logfile:
        for line in logfile.readlines():
            try:
                if 'ap' in line:
                    ap = line.strip().split(',')[2].strip().replace('ap = ', '')
                    ap_value = ap.strip().replace(' %', '')
                    ap_value = str2float(ap_value)
                if 'recall' in line:
                    thresh = line.strip().split(',')[0].strip().replace('for thresh = ', '')
                    precision = line.strip().split(',')[1].strip().replace('precision = ', '')
                    precision_value = str2float(precision)
                    recall = line.strip().split(',')[2].strip().replace('recall = ', '')
                    recall_value = str2float(recall)
                    F1_score = line.strip().split(',')[3].strip().replace('F1-score = ', '')
                if 'TP' in line:
                    TP = line.strip().split(',')[1].strip().replace('TP = ', '')
                    FP = line.strip().split(',')[2].strip().replace('FP = ', '')
                    FN = line.strip().split(',')[3].strip().replace('FN = ', '')
                    average_IoU = line.strip().split(',')[4].strip().replace('average IoU = ', '')
                    average_IoU_value = average_IoU.strip().replace(' %', '')
                    average_IoU_value = str2float(average_IoU_value)
            except:
                print('wrong when deal with: ', log_file)

    if average_IoU_value == 0 or ap_value == 0:
        pass
    else:
        try:
            result_relief.append([int(iteration), ap_value, average_IoU_value, precision_value, recall_value])
        except:
            print('wrong when deal with: ', log_file)
    result[iteration]={'ap': ap, 'average_IoU':average_IoU, 'thresh': thresh, 'precision': precision, 'recall': recall, 'F1_score': F1_score, 'TP': TP, 'FP':FP, 'FN':FN}


list_key = list(result.keys())
list_iteration = [int(it) for it in list_key]
list_iteration.sort()

for it in list_iteration:
    print('iteration: ', it, result[str(it)])

result_relief.sort()
print(result_relief)

result_relief = np.array(result_relief, dtype=np.float32)
print('num of valid data: ', result_relief.shape[0])
max_ap = result_relief[:, 1].max()
max_ap_index = np.where(result_relief[:, 1]==max_ap)
print('max ap: ', result_relief[max_ap_index, :])
max_avg_IOU = result_relief[:, 2].max()
max_avg_IOU_index = np.where(result_relief[:, 2]==max_avg_IOU)
print('max avg_IOU: ', result_relief[max_avg_IOU_index, :])
# max_precision = result_relief[:, 3].max()
# max_precision_index = np.where(result_relief[:, 3]==max_precision)
# print('max precision: ', result_relief[max_precision_index, :])
# max_recall = result_relief[:, 4].max()
# max_recall_index = np.where(result_relief[:, 4]==max_recall)
# print('max recall: ', result_relief[max_recall_index, :])

line1, = plt.plot(result_relief[:, 0], result_relief[:, 1], 'r-')
line2, = plt.plot(result_relief[:, 0], result_relief[:, 2], 'b-')
plt.legend(handles=[line1, line2], labels=['ap', 'avg_IOU'], loc='best')
plt.title('origin yolov3\nmax ap: iteration %d ap %s and average_IOU %s\nmax avg_IOU: iteration %d ap %s and average_IOU %s' %
          (result_relief[max_ap_index, 0], result_relief[max_ap_index, 1], result_relief[max_ap_index, 2],
           result_relief[max_avg_IOU_index, 0], result_relief[max_avg_IOU_index, 1], result_relief[max_avg_IOU_index, 2]))
plt.xlabel('num of iteration')
plt.show()


