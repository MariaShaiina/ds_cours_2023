#Импорт библиотек и модулей
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from PIL import Image
import torch

from torchvision import models
import torchvision.transforms as T

img = Image.open("/content/drive/My Drive/Colab_Notebooks/input.jpg")
cv.imwrite("/usr/local/Dev/output/" + 'input img.jpg',bin_img)

# Загружаем модель
fcn = models.segmentation.fcn_resnet101(pretrained=True).eval() #eval - выход

# Нормализация
mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]

trf = T.Compose([
    T.ToTensor(), # Привести значения к 1 [0,1]
    T.Normalize(mean=mean, std=std)]
)

input = trf(img).unsqueeze(0) # unsqueeze() c флагом 0 приводит изображение вида (3, 224, 224) к виду (1, 3, 224, 224))

# Прямой проход через сеть
out =fcn(input)['out']

print('Параметры выхода')
print()
for i in range(len(out.shape)):
  s = ['Размер пакета:', 'Кол-во классов', 'W:', 'H:']
  print(s[i], out.shape[i])

  # Преобразуем изображение в 1-канальное (2D), где каждый пиксел является классом
  out = torch.argmax(out.squeeze(), dim=0).detach().cpu().numpy()
  print("Получаем 2D изображение размера", out.shape)
  print("Получаем меткy/метки классa(ов)", np.unique(out))


  # Преобразуем 2D изображение в 3-х канальное
  def decode_segmap(image, class_list, nc=21):

      label_colors = np.array([(0, 0, 0),  # 0-background
                               # 1-aeroplane, 2-bicycle, 3-bird, 4-boat, 5-bottle
                               (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128),
                               # 6-bus, 7-car, 8-cat, 9-chair, 10-cow
                               (0, 128, 128), (128, 128, 128), (64, 0, 0), (192, 0, 0), (64, 128, 0),
                               # 11-dining table, 12-dog, 13-horse, 14, 15
                               (192, 128, 0), (64, 0, 128), (192, 0, 128), (64, 128, 128), (192, 128, 128),
                               # 16, 17-sheep, 18-sofa, 19, 20
                               (0, 64, 0), (128, 64, 0), (0, 192, 0), (128, 192, 0), (0, 64, 128)])

      r = np.zeros_like(image).astype('uint8')
      g = np.zeros_like(image).astype('uint8')
      b = np.zeros_like(image).astype('uint8')

      for clss in range(len(class_list)):
          for _ in range(nc):
              idx = image == class_list[clss]  # метка класса
              r[idx] = label_colors[class_list[clss], 0]
              g[idx] = label_colors[class_list[clss], 1]
              b[idx] = label_colors[class_list[clss], 2]

      rgb = np.stack([r, g, b], axis=2)
      return rgb


  OutRGB_Img = decode_segmap(out, np.unique(out))
  cv.imwrite("/usr/local/Dev/output/" + 'output road img.jpg', OutRGB_Img)

  # Применим эту же функцию к другому изображению, но уже с двумя классами - фон и кошка
  img2 = Image.open("/content/drive/My Drive/Colab_Notebooks/cat.jpg")
  input2 = trf(img2).unsqueeze(0)
  out2 = fcn(input2)['out']
  out2 = torch.argmax(out2.squeeze(), dim=0).detach().cpu().numpy()
  OutRGB_Img2 = decode_segmap(out2, np.unique(out2))
  cv.imwrite("/usr/local/Dev/output/" + 'output cat img.jpg', OutRGB_Img2)
