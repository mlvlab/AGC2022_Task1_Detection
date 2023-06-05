# AGC2022_Task1_Detection
### Pre-trained Model Download
- Superglue: https://drive.google.com/file/d/1ACYKMSg8GCb5qEgvfO5m0LTCJvhnOMWm/view?usp=sharing
- Yolov7: https://drive.google.com/file/d/1-eCIYzgr9eXp2ANBp3R4ZQor7Vl8YQwO/view?usp=share_link

## Superglue Dependencies  
- Python >= 3.5   
- PyTorch >= 1.1   
- OpenCV >= 3.4 (4.1.2.30 recommended for best GUI keyboard interaction, see this note)   
- Matplotlib >= 3.1   
- NumPy >= 1.18   

### Make Checkpoint Folder
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
