import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_path', default=None, help='video path')
    parser.add_argument('--clue_path', default=None, help='clue(img, txt) path')
    parser.add_argument('--json_output_path', default='.', help='json output path')

    parser.add_argument('--task1_debug', action="store_true", help='(optional)debug mode')
    parser.add_argument('--debug_input_path', default=None, help='debugging input image path')
    parser.add_argument('--debug_output_path', default=None, help='debugging output image path')
    
    parser.add_argument('--yolo_path', default='.', help='yolo task1 checkpoint path')
    parser.add_argument('--img_conf_th', type=float, default=0.6, help='img threshold')   # NOTE: determine best confidence threshold value
    parser.add_argument('--img_kp_th', type=float, default=50, help='img threshold')      # NOTE: determine best keypoint threshold value
    parser.add_argument('--txt_th', type=float, default=0.8, help='txt threshold')        # NOTE: determine value
    parser.add_argument('--od_th', type=float, default=0.5, help='OD threshold')          # NOTE: determine value
    parser.add_argument('--total_th', type=float, default=0.9, help='img+txt threshold')  # NOTE: determine value
    args = parser.parse_args()

    return args