"""
Docs: http://kanungo.com/pubs/tpami04-ddmest.pdf
https://hal.science/hal-01354467/document
"""

import cv2
import os
import numpy as np


def contrast_score(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contrast = gray.std()
    return contrast


def resolution_score(image_path):
    image = cv2.imread(image_path)
    height, width, dpi = image.shape
    return dpi


def noise_score(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    noise = cv2.meanStdDev(gray)
    return noise[1][0][0]


def document_blurriness(image_path):
    # Загрузка изображения скана документа
    image = cv2.imread(image_path)
    
    # Преобразование изображения в черно-белое
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Вычисление оценки качества изображения
    blur_score = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    blur_score = int(round(blur_score, 0))

    if blur_score < 100:
        blurriness = f"Высокая размытость ({blur_score} < 100)"
    elif blur_score < 500:
        blurriness = f"Средняя размытость (100 < {blur_score} < 500)"
    else:
        blurriness = f"Низкая размытость ({blur_score} >= 500)"
    
    return blurriness


def detect_unwanted_elements(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)
    
    # Преобразование изображения в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Выполнение гауссово размытие для сглаживания изображения
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Применение адаптивного порогового значения для бинаризации изображения
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
    
    # Поиск контуров на бинаризованном изображении
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Проход по каждому найденному контуру
    for contour in contours:
        # Вычисление площади контура
        area = cv2.contourArea(contour)
        
        # Если площадь контура ниже некоторого порога, то считаем его нежелательным элементом
        if area < 1000:
            # Рисуем прямоугольник вокруг нежелательного элемента
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Отображение изображения с обнаруженными нежелательными элементами
    cv2.imshow('Result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_file_size(file_path):
    """Подсчет размера файла скана в Mb
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        size_in_bytes = file_info.st_size
        size_in_kilobytes = round(size_in_bytes / 1024, 0)
        size_in_megabytes: int = int(round(size_in_kilobytes / 1024, 0))
        return size_in_kilobytes
    else:
        print("Файл не найден")
        return -1
