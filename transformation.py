# coding: UTF-8

import cv2
import matplotlib.pyplot as plt
import numpy as np

# このファイルで透視変換
class Transformation:
  def __init__():
    print("コンストラクタが呼ばれました！")
  def hello():
    print("Hello Transformation")
  def transform(name):
    print("Hello ", name)
    img = cv2.rotate(cv2.imread("./tmp/"+name), cv2.ROTATE_90_COUNTERCLOCKWISE)
    height, width, channels = img.shape[:3]
    print("height: %d, width: %d, channels: %d " % (height, width, channels))
    resize_img = img[910 : 3100, 430: 2750]
    # plt.imshow(resize_img)
    
    resize_height, resize_width, resize_channels = resize_img.shape[:3]

    print("height: %d, width: %d, channels: %d " % (resize_height, resize_width, resize_channels))
    # list = np.float32(左上,左下, 右下, 右上)
    # listの元々の座標から目的の座標のどちらも必要
    # 今回の場合は、元々の目標が画像サイズいっぱいなので、目的の設定は簡単
    # 
    list_srcs = np.float32([[40, 10], [40, 1980], [2300,2000], [2290,300]])
    # 目的値
    list_dsts = np.float32([[0,0], [0,resize_height], [resize_width, resize_height], [resize_width, 0]])
    perspective_matrix = cv2.getPerspectiveTransform(list_srcs, list_dsts)
    dst_image = cv2.warpPerspective(resize_img, perspective_matrix, (resize_height, resize_width))
    # plt.imshow(dst_image)
    dst_name = name.split(".")[0]
    path = './transformed/' + dst_name + '_dst.jpg'
    cv2.imwrite(path, dst_image)
    return dst_name + '_dst.jpg'