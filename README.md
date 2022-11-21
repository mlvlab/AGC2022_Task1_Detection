# AGC2022_Task1_Detection
### Pre-trained Model Download
- Superglue: https://drive.google.com/file/d/1ACYKMSg8GCb5qEgvfO5m0LTCJvhnOMWm/view?usp=sharing
- Yolov7: https://drive.google.com/file/d/1-eCIYzgr9eXp2ANBp3R4ZQor7Vl8YQwO/view?usp=share_link

### Make Checkpoint foler
``` 
    cd superglue
    mkdir weights
    cd weights
    mv {SUPERGLUE_PRETRAINED_MODEL} .
```

### Run
```
    python task1.py
   --clue_path={CLUE_PATH}
   --yolo_path={YOLO_PRETRAINED_MODEL_PATH}
   --img_conf_th 0.1 
   --img_kp_th 150 
   --txt_th 0.3 
   --od_th 0.3 
```
