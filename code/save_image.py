import os
import matplotlib.pyplot as plt
from urllib.request import Request, urlopen
from PIL import Image
import numpy as np

def download_images(save_dir,name, urls):
  start_index = 0
  image_names = []
  i = 0
  len_img = len(os.listdir(save_dir))
  while i < len(urls):
    try:
        image_name = f'{name}_{str(i+len_img)}.jpg'
        image_path = os.path.join(save_dir, image_name)
        req = Request(urls[i], headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req)
        img = Image.open(webpage)
        img.save(image_path)
        try:
            plt.imread(image_path)
            image_names.append(image_name)
            start_index += 1
            i += 1
        except:
            # print('[DELETE] Image has no contents -', image_name)
            os.remove(image_path)
            urls.remove(urls[i])
    except:
        # print('[ERROR] Failed to request -', image_name, '-', urls[i])
        urls.remove(urls[i])