import os
import numpy as np
import matplotlib.pyplot as plt

pre40000_log_file = os.path.join(os.getcwd(), 'pre40000.log')
save_dir = os.path.join(os.getcwd(), 'results')
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


pre40000_avg_losses = get_avg_loss(pre40000_log_file)
total_avg_losses = pre40000_avg_losses

pre40000_avg_losses_np = np.array(pre40000_avg_losses)
pre40000_avg_losses_np[np.lexsort(pre40000_avg_losses_np[:,::-1].T)]
total_avg_losses_np = np.array(total_avg_losses)
total_avg_losses_np[np.lexsort(total_avg_losses_np[:,::-1].T)]

np.save(os.path.join(save_dir,'avg_losses_0_40000.npy'), pre40000_avg_losses_np)
np.save(os.path.join(save_dir,'avg_losses.npy'), total_avg_losses_np)

plt.figure(1)
plt.plot(pre40000_avg_losses_np[1000:,0], pre40000_avg_losses_np[1000:,1])
plt.xlabel('num of batch')
plt.ylabel('avg loss')
plt.figure(2)
plt.plot(total_avg_losses_np[:,0], total_avg_losses_np[:,1])
plt.xlabel('num of batch')
plt.ylabel('avg loss')
# plt.axis([0, , 0, 20])
plt.show()


