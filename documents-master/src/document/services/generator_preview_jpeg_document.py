import fitz
import os.path

from django.conf import settings


class GeneratorPreviewJpeg:
    def __init__(self, file):
        self.file = file

    def __call__(self):
        return self.create_preview_image()

    def create_preview_image(self):
        name_file = os.path.basename(self.file.name)[:-4]
        path = f'{settings.MEDIA_ROOT}/images/{name_file}.jpg'
        doc = fitz.open(self.file.name)
        pix = doc.get_page_pixmap(0)
        pix.pil_save(path, optimize=True, dpi=(150, 150))
        doc.close()
        return f"images/{name_file}.jpg"
