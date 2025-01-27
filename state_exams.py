from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

def checkbox_line(c, margin, width, line_height, y_position, checkbox_size, topics):
    c.setFont("Helvetica", 10)
    
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

def create_exam_topics_pdf(filename, topics):
    # Set up the PDF canvas
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    margin = 50
    line_height = 20

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, height - margin, "Státnice: společná část")
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
    "Topic 1: Advanced Calculus",
    "Topic 2: Linear Algebra",
    "Topic 3: Probability and Statistics",
    "Topic 4: Numerical Methods",
    "Topic 5: Abstract Algebra",
    "Topic 6: Real Analysis",
    "Topic 7: Complex Analysis",
    "Topic 8: Topology",
    "Topic 9: Functional Analysis",
    "Topic 10: Differential Geometry"
]

create_exam_topics_pdf("exam_topics_checklist.pdf", topics)
