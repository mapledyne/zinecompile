from fpdf import FPDF
import os
import logging

source = 'source'
compiled = 'compiled'

def get_source_directories():
    sources = []
    for root, dirs, files in os.walk(source):
        for d in dirs:
            sources.append(d)
    return sources

class Zine():
    def __init__(self, folder):
        logging.info(f"Creating new Zine: {folder}")
        self.compiled = False
        self.paper_width = 11
        self.paper_height = 8.5
        self.padding = 0.2
        self.pdf = FPDF('L', 'in', 'Letter')
        self.pdf.add_page()

        name = folder.split('-')

        self.source = folder
        self.issue = name[0].strip()
        self.title = name[1].strip()
        
        logging.info(f'-->Issue: {self.issue}')
        logging.info(f'-->Title: {self.title}')

    def draw_lines(self):
        self.pdf.line(self.paper_width * 0.25, self.padding, self.paper_width * 0.25, self.paper_height - self.padding)
        self.pdf.line(self.paper_width * 0.5, self.padding, self.paper_width * 0.5, self.paper_height - self.padding)
        self.pdf.line(self.paper_width * 0.75, self.padding, self.paper_width * 0.75, self.paper_height - self.padding)
        self.pdf.line(self.paper_width * 0.75, self.padding, self.paper_width * 0.75, self.paper_height - self.padding)
        self.pdf.line(self.padding, self.paper_height * 0.5, self.paper_width * 0.25, self.paper_height * 0.5)
        self.pdf.line(self.paper_width * 0.75, self.paper_height * 0.5, self.paper_width - self.padding, self.paper_height * 0.5)
        self.pdf.dashed_line(self.paper_width * 0.25, self.paper_height * 0.5, self.paper_width * 0.75, self.paper_height * 0.5, 0.1, 0.1)

    def draw_title(self):
        cover_w = self.paper_width * 0.75
        cover_h = self.paper_height * 0.5
        page_width = self.paper_width * 0.25

        title_h = cover_h * 0.8 + cover_h

        self.pdf.set_font('Arial', 'B', 16)
        self.pdf.set_xy(cover_w, title_h)
        self.pdf.cell(page_width, txt=self.title, align='C')

    def draw_issue(self):
        cover_w = self.paper_width * 0.75
        cover_h = self.paper_height * 0.5
        page_width = self.paper_width * 0.25

        issue_h = cover_h * 0.25 + cover_h
        issue_w = page_width * 0.8 + cover_w

        self.pdf.set_xy(issue_w, issue_h)
        self.pdf.set_font('Arial', '', 16)
        self.pdf.cell(1, txt=f"#{self.issue}")

    def draw_heading(self):
        cover_w = self.paper_width * 0.75
        cover_h = self.paper_height * 0.5
        page_width = self.paper_width * 0.25

        title_h = cover_h * 0.05 + cover_h

        self.pdf.image(f'{source}/title.png', cover_w, title_h, w=page_width)

    def draw_cover_img(self):
        cover_w = self.paper_width * 0.75
        cover_h = self.paper_height * 0.5
        page_width = self.paper_width * 0.25

        image_y = cover_h * 0.15 + cover_h
        image_width = page_width * 0.85

        image_x = cover_w + ((page_width - image_width) / 2)
        self.pdf.image(f'{source}/{self.source}/cover.png', image_x, image_y, w=image_width)

    def draw_step_1(self):
        page_w = self.paper_width * 0.25
        page_h = self.paper_height / 2 + self.padding

        page_width = self.paper_width * 0.25
        image_width = 2.5
        page_w += (page_width - image_width) / 2
        self.pdf.image(f'{source}/{self.source}/1_4x.png', page_w, page_h, w=image_width)

    def draw_step_2(self):
        page_w = self.paper_width * 0.5
        page_h = self.paper_height / 2 + self.padding

        page_width = self.paper_width * 0.25
        image_width = 2.5
        page_w += (page_width - image_width) / 2

        self.pdf.image(f'{source}/{self.source}/2_4x.png', page_w, page_h, w=image_width)

    def draw_step_3(self):
        page_w = self.paper_width * 0.75
        page_h = self.paper_height / 2 + self.padding

        page_width = self.paper_width * 0.25
        image_width = 2.5
        page_w += (page_width - image_width) / 2

        self.pdf.image(f'{source}/{self.source}/3_4x.png', page_w, page_h, w=image_width)

    def draw_step_4(self):
        page_w = 0
        page_h = self.paper_height / 2 + self.padding

        page_width = self.paper_width * 0.25
        image_width = 2.5
        page_w += (page_width - image_width) / 2

        self.pdf.image(f'{source}/{self.source}/4_4x.png', page_w, page_h, w=image_width)

    def draw_step_5(self):
        page_w = self.paper_width * 0.25
        page_h = self.paper_height / 2 + self.padding

        page_width = self.paper_width * 0.25
        image_width = 2.5
        page_w += (page_width - image_width) / 2

        self.pdf.image(f'{source}/{self.source}/5_4x.png', page_w, page_h, w=image_width)

    def draw_back_cover(self):
        f = open(f"{source}/back.txt", "r")
        back_text = f.read()

        page_w = self.paper_width * 0.5 + self.padding
        page_h = self.paper_height * 0.5 + self.padding

        cell_width = self.paper_width * 0.25 - (self.padding * 2)
        self.pdf.set_font('Arial', '', 10)
        self.pdf.set_xy(page_w, page_h)
        self.pdf.multi_cell(w=cell_width, h=0.2, txt=back_text, align='L')

    def draw_intro(self):
        f = open(f"{source}/{self.source}/intro.txt", "r")
        intro_text = f.read()

        page_w = self.padding
        page_h = self.paper_height * 0.5 + self.padding
        cell_width = self.paper_width * 0.25 - (self.padding * 2)
        self.pdf.set_font('Arial', '', 10)
        self.pdf.set_xy(page_w, page_h)
        self.pdf.multi_cell(w=cell_width, h=0.2, txt=intro_text, align='L')

    def compile(self):
        logging.info(f"Compiling zine: {self.title}")
        #pdf.set_font('Arial', 'B', 16)
        #pdf.cell(40, 10, 'Hello World!')

        self.draw_cover_img()
        self.draw_title()
        self.draw_issue()
        self.draw_heading()

        self.draw_step_4()
        self.draw_step_5()

        self.draw_back_cover()

        self.pdf.rotate(180, self.paper_width / 2, self.paper_height / 2)

        self.draw_step_1()
        self.draw_step_2()
        self.draw_step_3()
        self.draw_intro()

        self.draw_lines()

        self.compiled = True

    def source_location(self):
        return f'{source}/{self.source}/'
    
    def compiled_location(self):
        return f'{compiled}/'

    def save(self):
        if not self.compiled:
            self.compile()
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

