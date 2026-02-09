import cv2
import pytesseract

# 🔴 FORCE tesseract path (no restart needed)
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\student\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)

def extract_text(image_path: str) -> str:
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        return "Image could not be read"

    img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)[1]
    img = cv2.medianBlur(img, 3)

    text = pytesseract.image_to_string(img)
    return text.strip()
