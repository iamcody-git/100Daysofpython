from fpdf import FPDF
import pandas as pd

# orientation p=portrait and l = landscape
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"], align="L", ln=1)
    
    # this for line like copy
    for y in range(20,298,10):
        pdf.line(10,y,200,y)
    pdf.line(10,21,200,21)
    
    #footer part
    pdf.ln(265)  # total length of A4 size paper is 298mm so we consider for footer 265mm
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"], align="R", ln=1)
    
    # footer part
    
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(275)
        pdf.set_font(family="Times", style="IB", size=10)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"], align="R", ln=1)
        
        #this is for line like copy
    for y in range(20,298,10):
        pdf.line(10,y,200,y)
            
pdf.output("result.pdf")
