import os
import glob
import random
import string
import base64
from urllib.parse import urlparse
from icrawler import ImageDownloader
from icrawler.builtin import GoogleImageCrawler


global unique_image_name

def refresh_unique_image_name():
    global unique_image_name
    unique_string = string.ascii_uppercase + string.ascii_lowercase + string.digits
    unique_image_name = ''.join(random.choice(unique_string) for _ in range(16))
    
    return None


class PrefixNameDownloader(ImageDownloader):

    def get_filename(self, task, default_ext):
        global unique_image_name
        url_path = urlparse(task['file_url'])[2]
        if '.' in url_path:
            extension = url_path.split('.')[-1]
            if extension.lower() not in ['jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif', 'ppm', 'pgm']: extension = default_ext
        else:
            extension = default_ext
        filename = base64.b64encode(url_path.encode()).decode()

        return "p_" + unique_image_name + '{}.{}'.format(filename, extension)


class ImageCrawler():

    def google_crawler(self, image_query):
        refresh_unique_image_name()
        google_crawler = GoogleImageCrawler(downloader_cls=PrefixNameDownloader, storage={'root_dir': os.getcwd()})
        google_crawler.crawl(keyword=image_query, max_num=1)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = glob.glob(f"p_{unique_image_name}*")
        img_path = os.path.join(dir_path, file_name[0])

        return img_path


if __name__=='__main__':
    image_query = 'imagem_onix.jpg'
    ImageCrawler().google_crawler(image_query)
