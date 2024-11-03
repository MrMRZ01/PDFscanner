import fitz
import cv2
import numpy as np
from PIL import Image
import os


def enhance_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh_image = cv2.threshold(gray_image, thresh_number, 255, cv2.THRESH_BINARY)

    mask = cv2.bitwise_not(thresh_image)

    white_background = np.ones_like(image) * 255
    final_image = np.where(mask[:, :, np.newaxis] == 255, image, white_background)

    return final_image

def process_pdf(input_pdf_path, output_pdf_path):
    doc = fitz.open(input_pdf_path)
    images = []

    for page in doc:
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        enhanced_image = enhance_image(img_cv)
        images.append(enhanced_image)


    output_images = [Image.fromarray(img) for img in images]
    output_images[0].save(output_pdf_path, save_all=True, append_images=output_images[1:])

    print(f"Output saved to {output_pdf_path}")


input_pdf_path = input("Enter the path of your PDF file: ")
output_pdf_path = input("Enter the name of your output PDF file: ")
thresh_number = int(input('Enter the number of thresh(Suggested number 80): '))

if not output_pdf_path.endswith('.pdf'):
    output_pdf_path += ".pdf"

process_pdf(input_pdf_path, output_pdf_path)
