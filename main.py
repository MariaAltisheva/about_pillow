from PIL import Image

filename = "buildings.jpg"
with Image.open(filename) as img:
    img.load()

#
# type(img)
#
# isinstance(img, Image.Image)

# print(img.format)
# print(img.size)
# print(img.mode)

#Обрезаем изображение

cropped_img = img.crop((300, 150, 700, 1000))
# cropped_img.size
# cropped_img.show()
cropped_img.save('buildings_cropped.jpg')

# Сжатие файла

low_res_img = cropped_img.reduce(4)
low_res_img.save("low_resolution_cropped_image.png")

# low_res_img = cropped_img.resize((cropped_img.width // 4, cropped_img.height // 4))
# low_res_img.show()

# Переворачиваем изображение
converted_img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
# converted_img.show()
converted_img.save("converted_image.png")

# Поворачиваем картинку на 45 градусов
rotated_img = img.rotate(45)
# rotated_img.show()
rotated_img.save("rotated_image.png")

# Поворачиваем картинку на 45 градусов, полностью выводя на экран
rotated_img = img.rotate(45, expand=True)
# rotated_img.show()
rotated_img.save("rotated_image.png")

