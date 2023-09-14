"""
Основной модуль, точка входа методов оценки качества изображений.
"""

from utils import (
    contrast_score, resolution_score, noise_score, document_blurriness, 
    detect_unwanted_elements, get_file_size
)

from config import (
    path_good_quality, path_black_scanner, path_white_scanner,
    path_gausian_1_5, path_gausian_1, path_melting_20, path_melting_50
)

# Данные о размере файлов
print("Размер качественного скана в кБ:", get_file_size(path_good_quality))

# Тест на контраст
print("Контраст в качественном скане:", contrast_score(path_good_quality))
print("Контраст в документе с гаусовым размытием 1х1:", contrast_score(path_gausian_1))
print("Контраст в документе с гаусовым размытием 1.5х1.5:", contrast_score(path_gausian_1_5))

# Тест разрешения
print("Разрешение в качественном скане:", resolution_score(path_good_quality))
print("Разрешение в документе с гаусовым размытием 1х1:", resolution_score(path_gausian_1))
print("Разрешение в документе с гаусовым размытием 1.5х1.5:", resolution_score(path_gausian_1_5))

# Тест на размытие
print("Размытие в качественном скане:", document_blurriness(path_good_quality))
print("Размытие в документе с гаусовым размытием 1х1:", document_blurriness(path_gausian_1))
print("Размытие в документе с гаусовым размытием 1.5х1.5:", document_blurriness(path_gausian_1_5))

# Тест на шум
print("Зашумленность в качественном скане:", noise_score(path_good_quality))
print("Зашумленность в скане с черными полосами:", noise_score(path_black_scanner))
print("Зашумленность в скане с белыми полосами:", noise_score(path_white_scanner))
