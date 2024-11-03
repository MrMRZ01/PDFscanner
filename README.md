▎PDF Image Enhancer

This project is a Python tool for enhancing images extracted from PDF files. It uses OpenCV, NumPy, and PyMuPDF (fitz) to process each page of the PDF, improving the images by converting them to grayscale, applying thresholding, and creating a final image with a white background.

▎Features

• Extract images from PDF pages

• Enhance images by converting them to grayscale and applying thresholding

• Save enhanced images back into a new PDF file

▎Requirements

To run this code, you need the following libraries:

• OpenCV

• NumPy

• Pillow (PIL)

• PyMuPDF (fitz)

You can install these libraries using pip:
```bash
pip install opencv-python numpy Pillow PyMuPDF
```

▎How to Use

1. Save the code in a Python file (for example, pdf_image_enhancer.py).

2. In the terminal, navigate to the directory where you saved the file.

3. Run the code:
```bash
      python pdf_image_enhancer.py
```   

4. You will be prompted to enter the path of the input PDF file, the name of the output PDF file, and the threshold number.

5. The enhanced PDF will be saved at the specified path.

▎Example
```plaintext
Enter the path of your PDF file: path/to/your/document.pdf
Enter the name of your output PDF file: enhanced_document
Enter the number of thresh (Suggested number 80): 80
```

In this example, the input PDF is located at path/to/your/document.pdf, and the output PDF will be saved as enhanced_document.pdf.

▎Notes

• It is recommended to choose the threshold number between 0 and 255. The suggested value is 80.

• Ensure that the input PDF exists and is readable.

---

Thank you for using this tool! If you have any questions or feedback, please feel free to raise them in the Issues section on GitHub.
