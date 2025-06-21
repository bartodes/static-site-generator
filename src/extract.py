from re import findall

def extract_markdown_images(text):
    return findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    
def extract_markdown_links(text):
    return findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)