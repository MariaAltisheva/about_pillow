from PIL import Image

from sbs import tile

filename = "strawberry.jpg"
with Image.open(filename) as img:
    img.load()


cmyk_img = img.convert("CMYK")
gray_img = img.convert("L")  # Grayscale

# cmyk_img.show()
# gray_img.show()

# cmyk_img.save('straw_cmyk.jpg')
gray_img.save('straw_gray.jpg')

# print(img.getbands())
# # ('R', 'G', 'B')
# print(cmyk_img.getbands())
# # ('C', 'M', 'Y', 'K')
# print(gray_img.getbands())
# # ('L',)

red, green, blue = img.split()
#red
#<PIL.Image.Image image mode=L size=1920x1281 at 0x7FDD80C9AFA0>
# red.mode

zeroed_band = red.point(lambda _: 0)

red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))

green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))

blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))

red_merge.save('sraw_red.png')
green_merge.save('straw_green.png')
blue_merge.save('straw_blue.png')

strawberry_channels = tile(red_merge, green_merge, blue_merge)
strawberry_channels.save('str_chan.png')