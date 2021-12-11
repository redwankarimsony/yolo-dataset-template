## User Manual
This repository can create a standard training and validation dataset for YOLO-V3 model for object detection. Please follow the steps below to know how it works.


Dataset_name --
--/Images (dir for training data)
	--/Test (dir for inference data)
	--/scripts/
--create_dataset.py(generates train.txt, valid.txt,classes.names, datset_name.data and train.sh) 
                         	--create_inference_dataset.py(generates inference.txt and test.sh. Also after cloning the ‘darknet’ repo, a copy of “data” directory of darknet is kept both inside ‘dataset_name’ directory and in pwd )
	--/cfg/
--yolov3-custom-train.cfg
			--yolov3-custom-test.cfg
            --/backup_weights/
-- darknet53.conv.74(Must be present here when training from the pretrained coco version. If not present, download it using the command “wget https://pjreddie.com/media/files/darknet53.conv.74 -P data_dir_name/weights_backup/”)
-- custom_trained_weights1
-- custom_trained_weights2… and many more
	-- train.txt
	-- valid.txt
            -- inference.txt
-- classes.txt
            -- dataset_name.data
	-- train.sh(After generating train.sh by running “create_dataset.py” we will need to manually give the “weight_file_name” in the blank “<>” section to “data_dir_name/backup_weights/”weight_file_name”. Here “weight_file_name” = the weight file from where we want to train the model.)
	--test.sh
( Make coco.names and put the class label names [nomask, mask]. It also contains ‘labels’ folder and “make_labels.py”. Also make dummy “coco.data” in the working directory
