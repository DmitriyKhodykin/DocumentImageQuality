"""
Основной модуль, точка входа методов оценки качества изображений.
"""

from utils import document_blurriness, estimate_noise, calculate_document_quality

from config import (
    path_good_quality, path_black_scanner, path_white_scanner,
    path_gausian_1_5, path_gausian_1, path_melting_20, path_melting_50
)

# Тест на размытие
print("Размытие в качественном скане:", document_blurriness(path_good_quality))
print("Размытие в документе с гаусовым размытием 1х1:", document_blurriness(path_gausian_1))
print("Размытие в документе с гаусовым размытием 1.5х1.5:", document_blurriness(path_gausian_1_5))

# Тест на шум
print("Зашумленность в качественном скане:", calculate_document_quality(path_good_quality)[1])
print("Зашумленность в скане с таянием 20:", calculate_document_quality(path_melting_20)[1])
print("Зашумленность в скане с таянием 50:", calculate_document_quality(path_melting_50)[1])
