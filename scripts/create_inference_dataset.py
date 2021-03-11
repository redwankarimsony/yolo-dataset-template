import os, glob

data_dir_name = 'yolo-dataset-template'
image_dir_name = 'Test' # this folder contains all the test images for inference
sort_ = True


# Reading the images and writing to the .txt file
image_file_paths = glob.glob(f'{data_dir_name}/{image_dir_name}/*.jpg')
print(f'Total Number of Images Found: {len(image_file_paths)}')
if sort_:
    image_file_paths = sorted(image_file_paths)
    
with open(f'{data_dir_name}/inference.txt', 'w') as file_infer:
	file_infer.write('\n'.join(image_file_paths))

print(f'{data_dir_name}/inference.txt is written with {len(image_file_paths)} images')



	
