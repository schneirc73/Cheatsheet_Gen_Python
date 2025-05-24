# generate_cheatsheet.py

from fpdf import FPDF
from cheatsheet_data import cheatsheet
import os

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "Cheatsheet", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def entry(self, entry):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(0)
        self.multi_cell(0, 10, f"{entry['title']}")
        self.set_font("Helvetica", "", 11)
        self.multi_cell(0, 8, f"Definition: {entry.get('definition', '')}")
        if 'formula' in entry:
            self.multi_cell(0, 8, f"Formula: {entry['formula']}")
        if 'example' in entry:
            self.multi_cell(0, 8, f"Example: {entry['example']}")
        self.ln(4)

def generate_pdf(filename="output/cheatsheet.pdf"):
    os.makedirs("output", exist_ok=True)
    pdf = PDF()
    pdf.add_page()
    for category, entries in cheatsheet.items():
        pdf.chapter_title(category)
        for entry in entries:
            pdf.entry(entry)
    pdf.output(filename)
    print(f"✅ PDF saved to {filename}")

if __name__ == "__main__":
    generate_pdf()
