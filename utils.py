"""
Docs: http://kanungo.com/pubs/tpami04-ddmest.pdf
https://hal.science/hal-01354467/document
"""

import cv2
import numpy as np


def neighborhood_pattern_distributions(image_path):
    """Estimating degradation model parameters using 
    neighborhood pattern distributions: an optimization approach.
    """
    # Load image
    image = cv2.imread(image_path)

    # Image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 1. Flip each foreground pixel with probability
    
    # 2. Compute the distance d of each pixel from the character boundary

    # 3. Flip each background pixel with probability

    # 4. Perform morphological closing with a disk element of diameter k

    return None


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

    # cv2.imshow("", blur_score)
    # cv2.waitKey(0)
    
    return blurriness
