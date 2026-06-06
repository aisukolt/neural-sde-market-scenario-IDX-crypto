from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Flowable
 
class AnswerBox(Flowable):
    """A lined answer box with a label."""
    def __init__(self, lines=8, label="Jawaban:", width=None):
        Flowable.__init__(self)
        self.lines = lines
        self.label = label
        self.box_width = width or (A4[0] - 4*cm)
        self.line_height = 0.75*cm
        self.height = self.line_height * self.lines + 0.8*cm
 
    def wrap(self, availWidth, availHeight):
        self.box_width = availWidth
        return (self.box_width, self.height)
 
    def draw(self):
        c = self.canv
        # Label
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(colors.HexColor("#333333"))
        c.drawString(0, self.height - 0.5*cm, self.label)
        
        # Box border
        c.setStrokeColor(colors.HexColor("#4A90D9"))
        c.setLineWidth(1.2)
        box_top = self.height - 0.65*cm
        box_height = self.line_height * self.lines
        c.rect(0, box_top - box_height, self.box_width, box_height)
        
        # Inner lines
        c.setStrokeColor(colors.HexColor("#CCDDEE"))
        c.setLineWidth(0.5)
        for i in range(1, self.lines):
            y = box_top - i * self.line_height
            c.line(2, y, self.box_width - 2, y)
 
 
def build_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
 
    styles = getSampleStyleSheet()
 
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=14,
        textColor=colors.HexColor("#1A3A5C"),
        spaceAfter=4,
        alignment=TA_CENTER,
    )
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor("#555555"),
        spaceAfter=2,
        alignment=TA_CENTER,
    )
    chapter_style = ParagraphStyle(
        'Chapter',
        parent=styles['Heading1'],
        fontSize=12,
        textColor=colors.white,
        backColor=colors.HexColor("#1A3A5C"),
        spaceBefore=14,
        spaceAfter=6,
        leftIndent=-0.5*cm,
        rightIndent=-0.5*cm,
        borderPad=5,
    )
    section_style = ParagraphStyle(
        'Section',
        parent=styles['Heading2'],
        fontSize=10,
        textColor=colors.HexColor("#1A3A5C"),
        spaceBefore=10,
        spaceAfter=4,
        borderWidth=0,
        borderColor=colors.HexColor("#4A90D9"),
        borderPad=2,
    )
    question_style = ParagraphStyle(
        'Question',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor("#222222"),
        spaceBefore=6,
        spaceAfter=3,
        leftIndent=0.3*cm,
        leading=15,
    )
    note_style = ParagraphStyle(
        'Note',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.HexColor("#888888"),
        spaceAfter=2,
    )
 
    story = []
 
    # Header
    story.append(Paragraph("MA2231 Kalkulus Peubah Banyak", title_style))
    story.append(Paragraph("PR 2", title_style))
    story.append(Paragraph("Waktu Pengerjaan 1 Minggu, dikumpul 8 Juni 2026", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#1A3A5C"), spaceAfter=10))
 
    # ─────────────── BAB 5 ───────────────
    story.append(Paragraph("BAB 5", chapter_style))
 
    story.append(Paragraph("Latihan Dasar", section_style))
 
    story.append(Paragraph(
        "Hitunglah integral lipat dua dan integral lipat 3 berikut ini:", question_style))
 
    story.append(Paragraph(
        "a) &nbsp;&nbsp;&#x222C;<sub>D</sub> (x<super>2</super> + y<super>2</super>) dy dx &nbsp;"
        "di mana D &#x2282; &#x211D;<super>2</super> dibatasi sumbu x, sumbu y dan garis "
        "3x = 4y = 10.", question_style))
    story.append(AnswerBox(lines=10, label="Jawaban (a):"))
    story.append(Spacer(1, 0.3*cm))
 
    story.append(Paragraph(
        "b) &nbsp;&nbsp;&#x222D;<sub>W</sub> (x + y + z) dV &nbsp;"
        "di mana W adalah limas segitiga dengan titik-titik sudut di "
        "(0,0,0), (1,0,0), (0,1,0), (0,0,1).", question_style))
    story.append(AnswerBox(lines=10, label="Jawaban (b):"))
    story.append(Spacer(1, 0.3*cm))
 
    story.append(Paragraph("Latihan Lanjut", section_style))
 
    story.append(Paragraph(
        "1. &nbsp; Buktikan bahwa", question_style))
    story.append(Paragraph(
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        "&#x222B;<sub>0</sub><super>x</super> [ &#x222B;<sub>0</sub><super>t</super> F(u) du ] dt "
        "= &#x222B;<sub>0</sub><super>x</super> (x &#x2212; u) F(u) du",
        question_style))
    story.append(Paragraph("dimana F : &#x211D; &#x2192; &#x211D;.", question_style))
    story.append(AnswerBox(lines=10, label="Jawaban no. 1:"))
    story.append(Spacer(1, 0.3*cm))
 
    story.append(Paragraph(
        "2. &nbsp; Misalkan f : &#x211D;<super>3</super> &#x2192; &#x211D; adalah fungsi kontinu "
        "dan misalkan B<sub>&#x03B5;</sub> adalah bola berjari-jari &#x03B5; yang berpusat di "
        "(x<sub>0</sub>, y<sub>0</sub>, z<sub>0</sub>). Misalkan vol(B<sub>&#x03B5;</sub>) "
        "menyatakan volume dari bola B<sub>&#x03B5;</sub>. Tunjukkan bahwa",
        question_style))
    story.append(Paragraph(
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        "lim<sub>&#x03B5;&#x2192;0</sub> &nbsp;"
        "(1 / vol(B<sub>&#x03B5;</sub>)) &nbsp;"
        "&#x222D;<sub>B<sub>&#x03B5;</sub></sub> f(x,y,z) dV = f(x<sub>0</sub>, y<sub>0</sub>, z<sub>0</sub>).",
        question_style))
    story.append(AnswerBox(lines=10, label="Jawaban no. 2:"))
 
    # ─────────────── BAB 6 ───────────────
    story.append(Paragraph("BAB 6", chapter_style))
 
    story.append(Paragraph("Latihan Dasar", section_style))
 
    story.append(Paragraph(
        "1. &nbsp; Hitunglah &#x222C;<sub>R</sub> (1/(x+y)) dx dy di mana R adalah daerah yang "
        "dibatasi oleh x = 0, y = 0, x+y = 1 dan x+y = 4 dengan menggunakan pemetaan "
        "x = u &#x2212; uv, &nbsp; y = uv.", question_style))
    story.append(AnswerBox(lines=10, label="Jawaban no. 1:"))
    story.append(Spacer(1, 0.3*cm))
 
    story.append(Paragraph(
        "2. &nbsp; Tentukan volume yang dibatasi oleh "
        "z &#x2264; 6 &#x2212; x<super>2</super> &#x2212; y<super>2</super> "
        "dan z &#x2265; &#x221A;(x<super>2</super> + y<super>2</super>).", question_style))
    story.append(AnswerBox(lines=10, label="Jawaban no. 2:"))
 
    story.append(Paragraph("Latihan Lanjut", section_style))
 
    story.append(Paragraph(
        "1. &nbsp; Misalkan E adalah elipsoida &nbsp;"
        "E = {(x,y,z) | x<super>2</super>/a<super>2</super> + "
        "y<super>2</super>/b<super>2</super> + z<super>2</super>/c<super>2</super> &#x2264; 1} "
        "di mana a &gt; 0, b &gt; 0, c &gt; 0. Hitunglah "
        "&#x222D;<sub>E</sub> xyz dx dy dz.", question_style))
    story.append(AnswerBox(lines=10, label="Jawaban no. 1:"))
    story.append(Spacer(1, 0.3*cm))
 
    story.append(Paragraph(
        "2. &nbsp; Misalkan B adalah daerah di kuadran 1 yang dibatasi oleh kurva xy = 1, xy = 3, "
        "x<super>2</super> &#x2212; y<super>2</super> = 1, "
        "x<super>2</super> &#x2212; y<super>2</super> = 4. Hitunglah "
        "&#x222C;<sub>B</sub> (x<super>2</super> + y<super>2</super>) dx dy menggunakan "
        "perubahan variabel u = x<super>2</super> &#x2212; y<super>2</super> dan v = xy.",
        question_style))
    story.append(AnswerBox(lines=10, label="Jawaban no. 2:"))
 
    # ─────────────── BAB 7 ───────────────
    story.append(Paragraph("BAB 7", chapter_style))
 
    story.append(Paragraph("Latihan Dasar", section_style))
 
    story.append(Paragraph(
        "1. &nbsp; Tentukan luas dari daerah di permukaan "
        "&#x03A6; : (u, v) &#x21A6; (x, y, z) di mana "
        "x = u, y = u<super>2</super>, z = vu; &nbsp; 0 &#x2264; u &#x2264; 1, "
        "0 &#x2264; v &#x2264; 1 menggunakan dua pendekatan berikut:", question_style))
    story.append(Paragraph(
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a) Integral lintasan", question_style))
    story.append(AnswerBox(lines=8, label="Jawaban (a):"))
    story.append(Paragraph(
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b) Integral permukaan", question_style))
    story.append(AnswerBox(lines=8, label="Jawaban (b):"))
    story.append(Spacer(1, 0.3*cm))
 
    story.append(Paragraph(
        "2. &nbsp; Hitunglah &#x222C;<sub>S</sub> (&#x2207; &#xD7; <b>F</b>) &#x22C5; d<b>S</b> "
        "di mana S adalah permukaan x<super>2</super> + y<super>2</super> + 3z<super>2</super> = 1, "
        "z &#x2264; 0 dan <b>F</b> = y<b>i</b> &#x2212; x<b>j</b> + "
        "(zx<super>3</super>y<super>2</super>)<b>k</b>. Pilih <b>n</b> yang menghadap ke atas.",
        question_style))
    story.append(AnswerBox(lines=10, label="Jawaban no. 2:"))
 
    story.append(Paragraph("Latihan Lanjut", section_style))
    story.append(Paragraph(
        "Misalkan S adalah permukaan bola satuan dan <b>F</b> adalah medan vektor, "
        "dan F<sub>r</sub> adalah komponen dari <b>F</b> dalam arah radial. Tunjukkan bahwa",
        question_style))
    story.append(Paragraph(
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        "&#x222C;<sub>S</sub> <b>F</b> &#x22C5; d<b>S</b> = "
        "&#x222B;<sub>0</sub><super>2&#x03C0;</super> &#x222B;<sub>0</sub><super>&#x03C0;</super> "
        "F<sub>r</sub> sin&#x03C6; d&#x03C6; d&#x03B8;.", question_style))
    story.append(AnswerBox(lines=10, label="Jawaban:"))
 
    # ─────────────── BAB 8 ───────────────
    story.append(Paragraph("BAB 8", chapter_style))
 
    story.append(Paragraph("Latihan Dasar", section_style))
 
    story.append(Paragraph(
        "1. &nbsp; Periksa Teorema Green untuk integral garis berikut: "
        "&#x222E;<sub>C</sub> x<super>2</super>y dx + y dy "
        "di mana C adalah pinggiran dari daerah yang dibatasi oleh kurva y = x dan y = x<super>3</super>, "
        "0 &#x2264; x &#x2264; 1.", question_style))
    story.append(AnswerBox(lines=10, label="Jawaban no. 1:"))
    story.append(Spacer(1, 0.3*cm))
 
    story.append(Paragraph(
        "2. &nbsp; Tunjukkan bahwa medan vektor "
        "<b>F</b>(x,y,z) = (2xyz + sin x)<b>i</b> + (x<super>2</super>z)<b>j</b> + "
        "(x<super>2</super>y)<b>k</b> bebas lintasan. "
        "Tentukan sebuah fungsi bernilai skalar f yang memenuhi &#x2207;f = <b>F</b>.",
        question_style))
    story.append(AnswerBox(lines=10, label="Jawaban no. 2:"))
    story.append(Spacer(1, 0.3*cm))
 
    story.append(Paragraph(
        "3. &nbsp; Misalkan W adalah benda pejal yang dibatasi permukaan "
        "x = y<super>2</super>, x = 9, z = 0 dan x = z. Misalkan S = &#x2202;W. "
        "Hitung flux dari "
        "<b>F</b>(x,y,z) = (3x &#x2212; 5y)<b>i</b> + (4z &#x2212; 2y)<b>j</b> + (8yz)<b>k</b> "
        "sepanjang permukaan S.", question_style))
    story.append(AnswerBox(lines=10, label="Jawaban no. 3:"))
 
    story.append(Paragraph("Latihan Lanjut", section_style))
    story.append(Paragraph(
        "Misalkan D = {(x,y) | x<super>2</super> + y<super>2</super> &#x2264; 1} dan "
        "misalkan f : D &#x2192; &#x211D; fungsi kontinu. Tunjukkan ketunggalan solusi persamaan "
        "&#x2207; &#x22C5; &#x2207;u = 0 yang memenuhi u(x,y) = f(x,y) untuk semua (x,y) yang "
        "memenuhi x<super>2</super> + y<super>2</super> = 1.", question_style))
    story.append(AnswerBox(lines=12, label="Jawaban:"))
 
    story.append(Spacer(1, 0.5*cm))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1A3A5C")))
    story.append(Paragraph(
        "MA2231 Kalkulus Peubah Banyak — PR 2 &nbsp;|&nbsp; Dikumpul 8 Juni 2026",
        note_style))
 
    doc.build(story)
    print("PDF created successfully.")
 
import os
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_dir, "PR2_MA2231_dengan_slot_jawaban.pdf")
    build_pdf(output_path)