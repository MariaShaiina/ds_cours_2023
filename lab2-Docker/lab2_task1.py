#Пороговая обработка и повышение контрастности изображения
#Импорт библиотек и модулей
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from numpy import ndarray

print( cv.__version__ )

#1. Считаем цветное rgb изображение
img = cv.imread("/home/masha/TI_labs_2023/lab2_task1/input/orig_img.jpg")
cv.imshow("Original Image", img)
cv.waitKey(30000)  # Wait 0,5s
cv.destroyAllWindows()

#2. Преобразуем изображение в градации серого
def conversion_to_grayscale(image):
    grscl_img = (np.dot(img[...,0:3], [0.21, 0.72, 0.07])).astype(int)
    return grscl_img

gray_scl_img: ndarray = conversion_to_grayscale(img)
print("Разменрость исходного изображения", img.shape)
print("Разменрость изображения в градации серого", gray_scl_img.shape)

def preparate(img, prepfun):
    return np.vectorize(prepfun)(img)

# 3. Напишем функцию отображения гистограммы
def my_hist(img):
    hist = np.histogram(np.reshape(img, -1), np.arange(257))[0]
    hist = hist / img.size
    plt.bar(np.arange(256), hist, 1)
    plt.xticks(np.arange(0, 256, 15))

#4. Cделать пороговую обработку методом Otsu (Функция OpenCV)
# plt.subplots(2, 2, figsize=(26, 10))
#
# plt.subplot(2, 2, 1)
# plt.imshow(gray_scl_img, cmap='gray', vmin=0, vmax=255)
# plt.title('Input image', fontsize=18)
#
# plt.subplot(2, 2, 3)
#
# my_hist(gray_scl_img)
#
# plt.ylim(0, 0.017)
# plt.xlabel('Intensity values', fontsize=18)
# plt.ylabel('Number of pixels', fontsize=18)

trthreshold, bin_img = cv.threshold(gray_scl_img.astype("uint8"), 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imwrite("/home/masha/TI_labs_2023/lab2_task1/output/" + 'threshold img.jpg',bin_img)
print("Пороговое значение:", " ", trthreshold)

# plt.subplot(2, 2, 2)
# plt.imshow(bin_img, cmap='gray', vmin=0, vmax=255)
# plt.title('Output image', fontsize=18)
#
# plt.subplot(2, 2, 4)
# my_hist(bin_img)
# plt.ylim(0, 1)
# plt.xlabel('Pixel intensity values', fontsize=18)
# plt.ylabel('Number of pixels', fontsize=18)
#
# plt.show() #block=False

#Определим динамический диапазон входного изображения
print(f"Минимальное значение яркости: {np.amin(gray_scl_img)} \nМаксимальное значение яркости: {np.amax(gray_scl_img)}")

#Линейное контрастирование
a = 255 / (np.amax(gray_scl_img) - np.amin(gray_scl_img))
b = -1 * a * np.amin(gray_scl_img)
print("Коэффициенты ЛФ", '  ', a, ' ', b)

def lin_contrast(x):
    rez = a * x + b
    if rez < 0:
        return 0
    if rez > 255:
        return 255
    return (int)(rez)
lin_contrast_img = preparate(gray_scl_img, lin_contrast)
cv.imwrite("/home/masha/TI_labs_2023/lab2_task1/output/result img.jpg", lin_contrast_img)

#Отображение результатов
plt.subplots(2,  2, figsize=(24, 8.5))

plt.subplot(2, 2, 1)
plt.imshow(gray_scl_img, cmap='gray', vmin=0, vmax=255)
plt.title('Input image', fontsize= 18)

plt.subplot(2, 2, 3)
my_hist(gray_scl_img)
plt.ylim (0, 0.017)
plt.xlabel('Intensity values', fontsize = 18)
plt.ylabel('Number of pixels', fontsize = 18)

plt.subplot(2, 2, 2)
plt.imshow(lin_contrast_img, cmap='gray', vmin=0, vmax=255)
plt.title('Output image', fontsize= 18)

plt.subplot(2, 2, 4)
my_hist(lin_contrast_img)
plt.ylim (0, 0.017)
plt.xlabel('Intensity values', fontsize = 18)
plt.ylabel('Number of pixels', fontsize = 18)

plt.show()