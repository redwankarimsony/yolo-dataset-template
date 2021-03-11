import os, glob

data_dir_name = 'yolo-dataset-template'
image_dir_name = 'Test' # this folder contains all the test images for inference
backup_dir_name = 'weights_backup'
sort_ = True


# Reading the images and writing to the .txt file
image_file_paths = glob.glob(f'{data_dir_name}/{image_dir_name}/*.jpg')
print(f'Total Number of Images Found: {len(image_file_paths)}')
if sort_:
    image_file_paths = sorted(image_file_paths)
    
with open(f'{data_dir_name}/inference.txt', 'w') as file_infer:
	file_infer.write('\n'.join(image_file_paths))

print(f'{data_dir_name}/inference.txt is written with {len(image_file_paths)} images')


# Creating coco.names and putting the labels from the classes.txt file
with open(f'{data_dir_name}/classes.txt',  'r') as f1:
    with  open(f'coco.names',  'w') as f2:  #coco.names is created outside data_dir_name folder from where we run everything
    	classes = f1.read().strip().split('\n')
    	f2.write('\n'.join(classes))
    	no_of_classes = len(classes)


# Creating dummy coco.data
if os.path.exists(f'coco.data'):
	print(f'coco.data already exists outside {data_dir_name}')
else:
    with open(f'coco.data', 'w') as f:
        pass

#Creating test script
test_command = f'./darknet/darknet detect {data_dir_name}/cfg/yolov3-custom-test.cfg {data_dir_name}/{backup_dir_name}/<weight> {data_dir_name}/{image_dir_name}'

with open(f'{data_dir_name}/test.sh', 'w') as f:
	f.write(test_command.strip() )
