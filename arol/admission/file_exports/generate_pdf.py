from io import BytesIO

from django.http import HttpResponse
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Frame,
    FrameBreak,
    Image,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    SimpleDocTemplate,
)

sample_style_sheet = getSampleStyleSheet()


def title_style(sample_style_sheet):
    title_style = sample_style_sheet["Title"]
    title_style.alignment = 0
    return title_style


def subtitle_style(sample_style_sheet):
    subtitle_style = sample_style_sheet["Heading1"]
    subtitle_style.alignment = 1
    subtitle_style.fontSize = 14
    return subtitle_style


def field_label_style(sample_style_sheet):
    field_label_style = sample_style_sheet["Normal"]
    field_label_style.alignment = 0
    field_label_style.fontSize = 12
    field_label_style.fontName = "Helvetica"
    return field_label_style


def field_input_style(sample_style_sheet):
    field_input_style = sample_style_sheet["Code"]
    field_input_style.alignment = 2
    field_input_style.fontSize = 12
    return field_input_style


def subheading_style(sample_style_sheet):
    subheading_style = sample_style_sheet["Heading2"]
    subheading_style.alignment = 0
    return subheading_style


def logo(filename):
    image = Image(filename)
    image.drawHeight = 1 * inch
    image.drawWidth = 1 * inch
    return image


def profile(filename):
    image = Image(filename)
    image.drawHeight = 2 * inch
    image.drawWidth = 2 * inch
    return image


def create_frame(frames, page, x1, y1, width, height, showBoundary=1):
    frames[page - 1].append(Frame(x1, y1, width, height, showBoundary=showBoundary))


def fill_field(flowables, label, input):
    field_label = Paragraph(
        "{label}".format(label=label), field_label_style(sample_style_sheet)
    )
    field_input = Paragraph(
        "<b>{input}</b>".format(input=input), field_input_style(sample_style_sheet)
    )
    flowables.append(field_label)
    flowables.append(field_input)
    flowables.append(FrameBreak())


def export_pdf_wrapper(request, application_id):

    response = HttpResponse(content_type="application/pdf")
    response[
        "Content-Disposition"
    ] = "attachment; filename={application_id}.pdf".format(
        application_id=application_id
    )
    buffer = generate_pdf(request)
    response.write(buffer.getvalue())
    buffer.close()
    return response


def generate_pdf(request):

    buffer = BytesIO()

    pdf = SimpleDocTemplate(
        buffer,
        title="Admission Application",
        topMargin=40,
        leftMargin=40,
        rightMargin=40,
        bottomMargin=0,
    )

    flowables = []
    frames = [[]]

    create_frame(frames, 1, pdf.leftMargin, 725, 86, 86, 0)
    flowables.append(logo("./static/logo.png"))
    flowables.append(FrameBreak())

    create_frame(frames, 1, pdf.leftMargin + 120, 725, 335, 75, 0)
    title = Paragraph(
        "Indian Institute of Technology, Indore", title_style(sample_style_sheet)
    )
    subtitle = Paragraph("APPLICATION FORM", subtitle_style(sample_style_sheet))
    flowables.append(title)
    flowables.append(subtitle)
    flowables.append(FrameBreak())

    create_frame(frames, 1, pdf.leftMargin, 645, 200, 40)
    fill_field(flowables, "Application ID", "2201010202-220001")

    create_frame(frames, 1, pdf.leftMargin + 200, 645, 140, 40)
    fill_field(flowables, "Academic Year", "2022")

    create_frame(frames, 1, pdf.leftMargin, 605, 340, 40)
    fill_field(flowables, "Full Name", "Raja Krishnappa Bairya")

    create_frame(frames, 1, pdf.leftMargin, 565, 170, 40)
    fill_field(flowables, "Department", "CSE")
    create_frame(frames, 1, pdf.leftMargin + 170, 565, 170, 40)
    fill_field(flowables, "Programme", "PhD")

    create_frame(frames, 1, pdf.leftMargin, 525, 170, 40)
    fill_field(flowables, "Applicant", "Indian Applicant")
    create_frame(frames, 1, pdf.leftMargin + 170, 525, 170, 40)
    fill_field(flowables, "Nationality", "India")

    create_frame(frames, 1, pdf.leftMargin + 340, 525, 170, 160)
    flowables.append(profile("./static/sample_profile_picture.png"))
    flowables.append(FrameBreak())

    create_frame(frames, 1, pdf.leftMargin, 475, 510, 40, 0)
    subheading = Paragraph("Personal Profile", subheading_style(sample_style_sheet))
    flowables.append(subheading)
    flowables.append(FrameBreak())

    create_frame(frames, 1, pdf.leftMargin, 445, 170, 40)
    fill_field(flowables, "Date of Birth", "21-12-2000")
    create_frame(frames, 1, pdf.leftMargin + 170, 445, 340, 40)
    fill_field(flowables, "Father's/Spouse Name", "Raja Krishnappa Bairya")

    create_frame(frames, 1, pdf.leftMargin, 405, 170, 40)
    fill_field(flowables, "Marital Status", "Married")
    create_frame(frames, 1, pdf.leftMargin + 170, 405, 170, 40)
    fill_field(flowables, "Gender", "Male")
    create_frame(frames, 1, pdf.leftMargin + 340, 405, 170, 40)
    fill_field(flowables, "Caste Category", "General")

    create_frame(frames, 1, pdf.leftMargin, 365, 225, 40)
    fill_field(flowables, "Contact Number", "1234567890")
    create_frame(frames, 1, pdf.leftMargin + 225, 365, 285, 40)
    fill_field(flowables, "Parent Contact Number", "1234567890")

    create_frame(frames, 1, pdf.leftMargin, 325, 225, 40)
    fill_field(flowables, "Persons with Disabilities", "No")
    create_frame(frames, 1, pdf.leftMargin + 225, 325, 285, 40)
    fill_field(flowables, "Type of Disability", "-")

    create_frame(frames, 1, pdf.leftMargin, 275, 510, 40, 0)
    subheading = Paragraph(
        "Address for Correspondence", subheading_style(sample_style_sheet)
    )
    flowables.append(subheading)
    flowables.append(FrameBreak())

    create_frame(frames, 1, pdf.leftMargin, 245, 510, 40)
    fill_field(flowables, "Address", "7, Lok Kalyan Marg")
    create_frame(frames, 1, pdf.leftMargin, 205, 170, 40)
    fill_field(flowables, "City", "New Delhi")
    create_frame(frames, 1, pdf.leftMargin + 170, 205, 170, 40)
    fill_field(flowables, "State", "Delhi")
    create_frame(frames, 1, pdf.leftMargin + 340, 205, 170, 40)
    fill_field(flowables, "Pin/Zip", "110011")

    create_frame(frames, 1, pdf.leftMargin, 155, 510, 40, 0)
    subheading = Paragraph("Permanent Address ", subheading_style(sample_style_sheet))
    flowables.append(subheading)
    flowables.append(FrameBreak())

    create_frame(frames, 1, pdf.leftMargin, 125, 510, 40)
    fill_field(flowables, "Address", "7, Lok Kalyan Marg")
    create_frame(frames, 1, pdf.leftMargin, 85, 170, 40)
    fill_field(flowables, "City", "New Delhi")
    create_frame(frames, 1, pdf.leftMargin + 170, 85, 170, 40)
    fill_field(flowables, "State", "Delhi")
    create_frame(frames, 1, pdf.leftMargin + 340, 85, 170, 40)
    fill_field(flowables, "Pin/Zip", "110011")
    create_frame(frames, 1, pdf.leftMargin, 45, 510, 40, 0)
    flowables.append(NextPageTemplate("second_page"))
    flowables.append(PageBreak())

    frames.append([])
    create_frame(frames, 2, pdf.leftMargin, 735, 510, 40, 0)
    subheading = Paragraph("Educational Details", subheading_style(sample_style_sheet))
    flowables.append(subheading)
    flowables.append(FrameBreak())

    create_frame(frames, 2, pdf.leftMargin, 705, 170, 40)
    fill_field(flowables, "Examination", "Graduation")
    create_frame(frames, 2, pdf.leftMargin + 170, 705, 340, 40)
    fill_field(flowables, "Name of Examination", "IIT Boards")

    create_frame(frames, 2, pdf.leftMargin, 665, 340, 40)
    fill_field(flowables, "Board/Institute/University", "IIT Boards")
    create_frame(frames, 2, pdf.leftMargin + 340, 665, 170, 40)
    fill_field(flowables, "Duration of Degree", "4 years")

    create_frame(frames, 2, pdf.leftMargin, 625, 340, 40)
    fill_field(flowables, "Expected Year of Passing", "2022")
    create_frame(frames, 2, pdf.leftMargin + 340, 625, 170, 40)
    fill_field(flowables, "Status", "Completed")

    create_frame(frames, 2, pdf.leftMargin, 585, 170, 40)
    fill_field(flowables, "% of Marks or CPI/CGPA", "% of Marks")
    create_frame(frames, 2, pdf.leftMargin + 170, 585, 170, 40)
    fill_field(flowables, "% or CPI/CGPA", "85")
    create_frame(frames, 2, pdf.leftMargin + 340, 585, 170, 40)
    fill_field(flowables, "Out of CPI/CGPA", "100")

    create_frame(frames, 2, pdf.leftMargin, 545, 170, 40)
    fill_field(flowables, "Class/Division", "First")
    create_frame(frames, 2, pdf.leftMargin + 170, 545, 340, 40)
    fill_field(flowables, "Specialization", "IT")

    pdf.addPageTemplates(
        [
            PageTemplate(id="first_page", frames=frames[0]),
            PageTemplate(id="second_page", frames=frames[1]),
        ]
    )
    pdf.build(flowables)
    return buffer
