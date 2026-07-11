import fitz
def extract_text_from_pdf(filepath:str): #service is unaware of framework
    #pass #not using ocr cuz ocr is for scanned docs,imgs not text pdfs
    doc=fitz.open(filepath)# doc obj
    text=""
    for page in doc:
        text+=page.get_text("text")
    return text
