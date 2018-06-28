import os
import numpy as np
import matplotlib.pyplot as plt

experiment = 'cardet_20180628'

log_file = '../case/%s/train.log' % experiment
save_dir = '../case/%s/results' % experiment
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

def get_avg_loss(log_file):
    avg_losses = []
    with open(log_file, 'r') as logfile:
        for line in logfile.readlines():
            if 'avg' in line:
                try:
                    seperate_line = line.strip().split(',')
                    batch_id = int(seperate_line[0].split(':')[0])
                    avg_loss = float(seperate_line[1].split(' ')[1])
                    avg_losses.append([batch_id, avg_loss])
                except:
                    print(line)

    return avg_losses


avg_losses = get_avg_loss(log_file)
avg_losses_np = np.array(avg_losses)
avg_losses_np[np.lexsort(avg_losses_np[:,::-1].T)]

np.save(os.path.join(save_dir,'avg_losses.npy'), avg_losses_np)

print('max iteration: ', np.max(avg_losses_np[:,0]))

plt.figure(1)
# plt.plot(avg_losses_np[:,0], avg_losses_np[:,1])
plt.plot(avg_losses_np[1000:,0], avg_losses_np[1000:,1])
plt.xlabel('num of batch')
plt.ylabel('avg loss')
# plt.axis([0, , 0, 20])
plt.show()


