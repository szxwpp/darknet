
target_file = './result.txt'

def GetTime(line):
    line_seperate = line.strip().split(':')
    line_post = line_seperate[2].strip().replace('Predicted in ', '')
    cost_time =  line_post.strip().replace(' seconds.', '')
    cost_time = float(cost_time)

    return cost_time

sum_time = 0
count = 0
with open(target_file, 'r') as file_handle:
    lines = file_handle.readlines()
    for line in lines:
        if 'Predicted in' in line:
            count += 1
            sum_time += GetTime(line)

print('images: %d sum time: %f per: %f' % (count, sum_time, sum_time/count))
print('FPS: %f' % (count/sum_time))
