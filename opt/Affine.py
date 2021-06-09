import cv2
import numpy as np

img = cv2.imread("input/fall.jpg")
h,w=img.shape[:2]

# 平行移動量
dx, dy = 200, 1000

# 平行変換行列の作成
afn_mat = np.float32([[1,0,dx],[0,1,dy]])

# 平行アフィン変換の実行
img_affine = cv2.warpAffine(img, afn_mat, (w,h))

# 回転変換行列の作成
rot_mat = cv2.getRotationMatrix2D((w/2,h/2), 40, 0.8)

# 回転アフィン変換の実行
img_affine_rot = cv2.warpAffine(img_affine, rot_mat, (w,h))

cv2.imwrite("output/fall_affine.jpg",img_affine)
cv2.imwrite("output/fall_affine_rot.jpg",img_affine_rot)