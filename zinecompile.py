from fpdf import FPDF
import os
import logging

source = "source"
compiled = "compiled"

def get_source_directories():
    sources = []
    for root, dirs, files in os.walk(source):
        for d in dirs:
            sources.append(d)
    return sources

class Zine():
    def __init__(self, folder):
        logging.info(f"Creating new Zine: {folder}")
        self.paper_width = 11
        self.paper_height = 8.5
        self.padding = 0.2
        self.pdf = FPDF('L', 'in', 'Letter')
        self.pdf.add_page()
        self.source = folder

    def draw_lines(self):
        self.pdf.line(self.paper_width * 0.25, self.padding, self.paper_width * 0.25, self.paper_height - self.padding)
        self.pdf.line(self.paper_width * 0.5, self.padding, self.paper_width * 0.5, self.paper_height - self.padding)
        self.pdf.line(self.paper_width * 0.75, self.padding, self.paper_width * 0.75, self.paper_height - self.padding)
        self.pdf.line(self.paper_width * 0.75, self.padding, self.paper_width * 0.75, self.paper_height - self.padding)
        self.pdf.line(self.padding, self.paper_height * 0.5, self.paper_width * 0.25, self.paper_height * 0.5)
        self.pdf.line(self.paper_width * 0.75, self.paper_height * 0.5, self.paper_width - self.padding, self.paper_height * 0.5)
        self.pdf.dashed_line(self.paper_width * 0.25, self.paper_height * 0.5, self.paper_width * 0.75, self.paper_height * 0.5, 0.1, 0.1)

    def compile(self):
        #pdf.set_font('Arial', 'B', 16)
        #pdf.cell(40, 10, 'Hello World!')
        #pdf.image('cover.png', 6, 3, 2.5, 3.5)
        self.draw_lines()
    
    def source_location(self):
        return f'{source}/{self.source}/'
    
    def compiled_location(self):
        return f'{compiled}/{self.source}/'

    def save(self):
        if not os.path.exists(self.compiled_location()):
            os.makedirs(self.compiled_location())
        self.pdf.output(self.compiled_location() + f'{self.source}.pdf', 'F')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    zines = get_source_directories()
    for z in zines:
        zine = Zine(z)
        zine.compile()
        zine.save()

