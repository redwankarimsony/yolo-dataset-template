import os, glob

data_dir_name = 'yolo-dataset-template'
image_dir_name = 'Images'
backup_dir_name = 'weights_backup'
valid_split = 0.2
sort_ = False
no_of_classes = -1

# Reading the images and writing to the .txt file
image_file_paths = glob.glob(f'{data_dir_name}/{image_dir_name}/*.jpg')
print(f'Total Number of Images Found: {len(image_file_paths)}')
if sort_:
    image_file_paths = sorted(image_file_paths)

train_file_paths = image_file_paths[:int(len(image_file_paths) * (1-valid_split))]
valid_file_paths = image_file_paths[int(len(image_file_paths) * (1-valid_split)):]

with open(f'{data_dir_name}/train.txt', 'w') as file_train:
	file_train.write('\n'.join(train_file_paths))
with open(f'{data_dir_name}/valid.txt', 'w') as file_valid:
	file_valid.write('\n'.join(valid_file_paths))
print(f'Train Images: {len(train_file_paths)}\nValidation Images: {len(valid_file_paths)}')


# Creating classes.txt >> classes.names

with open(f'{data_dir_name}/classes.txt',  'r') as f1:
    with  open(f'{data_dir_name}/classes.names',  'w') as f2:
    	classes = f1.read().strip().split('\n')
    	f2.write('\n'.join(classes))
    	no_of_classes = len(classes)
    	
metadata = f'classes = {no_of_classes}\ntrain = {data_dir_name}/train.txt\n\
valid = {data_dir_name}/valid.txt\nnames = {data_dir_name}/classes.names\n\
backup = {data_dir_name}/{backup_dir_name}'
print(metadata)


with open(f'{data_dir_name}/{data_dir_name}.data', 'w') as f:
	f.write(metadata.strip())

if os.path.exists(f'{data_dir_name}/{backup_dir_name}'):
	print(f'{backup_dir_name} exists inside {data_dir_name}')
else:
	os.mkdir(f'{data_dir_name}/{backup_dir_name}')
	print(f'New Backup directory created')
	



	
train_command = f'./darknet/darknet detector train {data_dir_name}/{data_dir_name}.data {data_dir_name}/cfg/yolov3-custom-train.cfg {data_dir_name}/{backup_dir_name}/<> -dont_show -map'

with open(f'{data_dir_name}/train.sh', 'w') as f:
	f.write(train_command.strip())
	
	
	
# Downloading the weights file. 
if os.path.exists(f'{data_dir_name}/{backup_dir_name}/darknet53.conv.74'):
	print('darknet53.conv.74 weights already exists')
else:
	print(f'darknet53.conv.74 can not be found in uour data directory.\n Run the following \'wget https://pjreddie.com/media/files/darknet53.conv.74 - P {data_dir_name}/{backup_dir_name}/')
	




    
