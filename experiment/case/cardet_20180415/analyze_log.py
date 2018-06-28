import os
import numpy as np
import matplotlib.pyplot as plt

pre1900_log_file = os.path.join(os.getcwd(), 'pre1900.log')
after1900_log_file = os.path.join(os.getcwd(), 'after1900.log')
after6900_log_file = os.path.join(os.getcwd(), 'after6900.log')
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


pre1900_avg_losses = get_avg_loss(pre1900_log_file)
after1900_avg_loess = get_avg_loss(after1900_log_file)
after6900_avg_loess = get_avg_loss(after6900_log_file)
total_avg_losses = pre1900_avg_losses + after1900_avg_loess + after6900_avg_loess

pre1900_avg_losses_np = np.array(pre1900_avg_losses)
pre1900_avg_losses_np[np.lexsort(pre1900_avg_losses_np[:,::-1].T)]
after1900_avg_loess_np = np.array(after1900_avg_loess)
after1900_avg_loess_np[np.lexsort(after1900_avg_loess_np[:,::-1].T)]
after6900_avg_loess_np = np.array(after6900_avg_loess)
after6900_avg_loess_np[np.lexsort(after6900_avg_loess_np[:,::-1].T)]
total_avg_losses_np = np.array(total_avg_losses)
total_avg_losses_np[np.lexsort(total_avg_losses_np[:,::-1].T)]

np.save(os.path.join(save_dir,'avg_losses_0_1900.npy'), pre1900_avg_losses_np)
np.save(os.path.join(save_dir,'avg_loess_1900_6900.npy'), after1900_avg_loess_np)
np.save(os.path.join(save_dir,'avg_loess_6900_40000.npy'), after6900_avg_loess_np)
np.save(os.path.join(save_dir,'avg_losses.npy'), total_avg_losses_np)

plt.figure(1)
plt.plot(pre1900_avg_losses_np[:,0], pre1900_avg_losses_np[:,1])
plt.xlabel('num of batch')
plt.ylabel('avg loss')
plt.figure(2)
plt.plot(after1900_avg_loess_np[:,0], after1900_avg_loess_np[:,1])
plt.xlabel('num of batch')
plt.ylabel('avg loss')
plt.figure(3)
plt.plot(after6900_avg_loess_np[:,0], after6900_avg_loess_np[:,1])
plt.xlabel('num of batch')
plt.ylabel('avg loss')
plt.figure(4)
plt.plot(total_avg_losses_np[1000:,0], total_avg_losses_np[1000:,1])
plt.xlabel('num of batch')
plt.ylabel('avg loss')
# plt.axis([0, , 0, 20])
plt.show()


