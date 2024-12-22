

import ctypes
import os

SPI_SETDESKWALLPAPER = 20
WALLPAPER_PATH = "F:\صور فيس\New Folder (2)"  # ضع مسار الصورة هنا

# تغيير خلفية سطح المكتب
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)

print("تم تغيير الخلفية بنجاح!")