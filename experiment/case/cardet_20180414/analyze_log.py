import os
import numpy as np
import matplotlib.pyplot as plt

pre2200_log_file = os.path.join(os.getcwd(), 'pre2200.log')
after2200_log_file = os.path.join(os.getcwd(), 'after2200.log')
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


pre2200_avg_losses = get_avg_loss(pre2200_log_file)
after2200_avg_loess = get_avg_loss(after2200_log_file)
total_avg_losses = pre2200_avg_losses + after2200_avg_loess

pre2200_avg_losses_np = np.array(pre2200_avg_losses)
pre2200_avg_losses_np[np.lexsort(pre2200_avg_losses_np[:,::-1].T)]
after2200_avg_loess_np = np.array(after2200_avg_loess)
after2200_avg_loess_np[np.lexsort(after2200_avg_loess_np[:,::-1].T)]
total_avg_losses_np = np.array(total_avg_losses)
total_avg_losses_np[np.lexsort(total_avg_losses_np[:,::-1].T)]

np.save(os.path.join(save_dir,'avg_losses_0_2200.npy'), pre2200_avg_losses_np)
np.save(os.path.join(save_dir,'avg_loess_2200_40000.npy'), after2200_avg_loess_np)
np.save(os.path.join(save_dir,'avg_losses.npy'), total_avg_losses_np)

plt.figure(1)
plt.plot(pre2200_avg_losses_np[:,0], pre2200_avg_losses_np[:,1])
plt.xlabel('num of batch')
plt.ylabel('avg loss')
plt.figure(2)
plt.plot(after2200_avg_loess_np[:,0], after2200_avg_loess_np[:,1])
plt.xlabel('num of batch')
plt.ylabel('avg loss')
plt.figure(3)
plt.plot(total_avg_losses_np[1000:,0], total_avg_losses_np[1000:,1])
plt.xlabel('num of batch')
plt.ylabel('avg loss')
# plt.axis([0, , 0, 20])
plt.show()


