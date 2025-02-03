from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
c.setFont("Arial", 12)

def checkbox_line(c, margin, width, line_height, y_position, checkbox_size, topics):
    c.setFont("Helvetica", 10)
    c.setStrokeColorRGB(120/255, 148/255, 158/255)
    for i, topic in enumerate(topics):
        if margin + (i + 1) * (checkbox_size) > width - margin:  # Check for row overflow
            y_position -= line_height + 40  # Move to next row
            i = 0  # Reset horizontal index

        # Draw the checkbox
        x_position = margin + i * (checkbox_size)
        c.rect(x_position, y_position - checkbox_size, checkbox_size, checkbox_size, stroke=1, fill=0)

        # Rotate and draw the topic text at 45 degrees
        c.saveState()
        c.translate(x_position + checkbox_size / 4, y_position - checkbox_size - 5)
        c.rotate(-45)
        c.drawString(5, 0, topic)
        c.restoreState()
    c.setStrokeColorRGB(0, 0, 0)
    c.rect(x_position - (i)*checkbox_size, y_position - checkbox_size, (i+1)*checkbox_size, checkbox_size, stroke=1, fill=0)

def create_exam_topics_pdf(filename, topics):
    # Set up the PDF canvas
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    margin = 50
    line_height = 20

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, height - margin, r"Státnice")
    c.line(margin, height - margin - 5, width - margin, height - margin - 5)

    # Draw each topic with a checkbox
    
    
    checkbox_size = 20

    y_position = height - margin - 30
    # Adjust the loop to place checkboxes side by side
    checkbox_line(c, margin, width, line_height, y_position, checkbox_size, topics)



    # Save the PDF
    c.save()

# Example usage
topics = [
    "ARMA modely",
    "Černá skříňka",
    "Patrice Lumumba's acid trip"
]

create_exam_topics_pdf("exam_topics_checklist.pdf", topics)
