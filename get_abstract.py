import fitz
import requests

def extract_abstract(url):
    
    def is_abstract(block):
        abstract_exists = False
        for i in range(len(block)):
            if isinstance(block[i], str):
                if "Abstract" in block[i]:
                    abstract_exists = True
                    return abstract_exists
        return False

    
    response = requests.get(url)
    pdf_content = response.content
    doc = fitz.open("pdf", pdf_content)

    abstract_headline = "Abstract"

    first_page = doc[0]

    counter = 0
    abstract_headline_exists = None
    blocks = []
    
    for block in first_page.get_text("blocks"):

        blocks.append(block)
        
        if is_abstract(block):
            return block[4].replace("\n", " ")
        elif counter == 5:
            abstract_headline_exists = False
            break
        else:
            counter += 1

    b1 = None
    if not abstract_headline_exists:
        b1 = blocks[2][4].replace("\n", " ")

    return b1
