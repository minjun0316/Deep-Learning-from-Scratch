import matplotlib.pyplot as plt
from matplotlib.image import imread

#현재 파일을 실행하는 쉘 기준(CWD) 상대 경로 기준으로 인자 작성
img = imread("img/test.png")

plt.imshow(img)
plt.show()