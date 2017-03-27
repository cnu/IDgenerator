# !/usr/bin/python
"""Tiny script to create PyCon India id cards using reportlab"""

from reportlab.pdfgen import canvas, textobject, pdfimages
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color, black, blue, red
import qrcode
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from wccg.settings import CREDENTIALS


with open('templates/mail_template.txt', 'r') as f:
    mail_template = f.read()
username = CREDENTIALS.get('sender_email')
password = CREDENTIALS.get('sender_pass')


def create_qr(fname, data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(fname)
    return fname


def draw_borders(c):
    """Draws the two borders around the card"""
    # c.rect(0*cm, 13*cm, 17*cm, 13.25*cm, stroke=1)
    c.roundRect(0 * cm, 14 * cm, 17 * cm, 13 * cm, radius=5, stroke=1)
    c.roundRect(0 * cm, 3.5 * cm, 8.5 * cm, 4.25 * cm, radius=5, stroke=1)
    c.roundRect(9 * cm, 3.5 * cm, 8.5 * cm, 4.25 * cm, radius=5, stroke=1)


def draw_banner(c):
    """Draws the 'Pycon India 2009' banner and the line below it at*cm
    the top"""
    c.setFont("Helvetica-Bold", 15)
    c.line(0 * cm, 25 * cm, 17 * cm, 25 * cm)
    c.line(0 * cm, 6.75 * cm, 8.5 * cm, 6.75 * cm)


def draw_image(c):
    """Draws the logo image at the correct position"""
    # im = Image('LogoFull02.png', 4*cm, 4*cm)
    # c.drawImage(im)
    c.drawImage("templates/logo.jpg", 1 * cm, 25.5 * cm, width=4 * cm, height=1.2 * cm, preserveAspectRatio=True)
    c.drawImage("templates/logo.jpg", 0 * cm, 7 * cm, width=3 * cm, height=0.6 * cm, preserveAspectRatio=True)


def draw_photo(c):
    c.roundRect(11.5 * cm, 14.5 * cm, 5 * cm, 5.5 * cm, radius=5, stroke=1)
    c.roundRect(13.75 * cm, 4.0 * cm, 3.15 * cm, 3.25 * cm, radius=5, stroke=1)


def draw_qr(c, fname):
    c.drawImage(fname, 1 * cm, 10.75 * cm, width=5 * cm, height=12 * cm, preserveAspectRatio=True)
    c.drawImage(fname, 9.5 * cm, 3.75 * cm, width=3.5 * cm, height=3.5 * cm, preserveAspectRatio=True)


def write_details(c, id, name, blood, emergency_name, emergency_no):

    t = c.beginText()
    c.setFont("Times-Bold", 30)
    c.drawCentredString(8.5 * cm, 23.25 * cm, name.upper())
    t.setTextOrigin(11 * cm, 25.6 * cm)
    t.setFont("Times-Bold", 32)
    t.textLine(id)

    t.setFont("Times-Roman", 16)
    t.setTextOrigin(1 * cm, 22 * cm)
    t.textLine('Blood Group')

    t.setFont("Times-Bold", 20)
    t.setTextOrigin(6.3 * cm, 22 * cm)
    t.textLine(': ' + blood)

    t.setFont("Times-Roman", 16)
    t.setTextOrigin(1 * cm, 20.75 * cm)
    t.textLine('Emergency Contact')

    t.setFont("Times-Bold", 20)
    t.setTextOrigin(6.3 * cm, 20.75 * cm)
    t.textLine(': ' + emergency_name)

    t.setFont("Times-Roman", 16)
    t.setTextOrigin(1 * cm, 19.5 * cm)
    t.textLine('Emergency Contact No')

    t.setFont("Times-Bold", 20)
    t.setTextOrigin(6.3 * cm, 19.5 * cm)
    t.textLine(': ' + emergency_no)
    #
    # t.setFont("Times-Roman", 16)
    # t.setTextOrigin(13.25 * cm, 18 * cm)
    # t.textLine('Photo')
    t.setFont("Times-Italic", 16)
    t.setTextOrigin(13.25 * cm, 17.25 * cm)
    t.setFillColorRGB(0.7, 0.7, 0.7)
    t.textLine('Photo')

    t.setTextOrigin(7.25 * cm, 13.25 * cm)
    t.textLine('Display Card')

    c.drawText(t)


def write_idcard_details(c, id, name, blood, emergency_name, emergency_no):


    t = c.beginText()
    t.setFillColorRGB(0, 0, 0)

    t.setTextOrigin(5.5 * cm, 7 * cm)
    t.setFont("Times-Bold", 16)
    t.textLine(id)

    c.setFont("Times-Bold", 16)
    c.setFillColor(black)
    c.drawCentredString(4.25 * cm, 6 * cm, name.upper())

    t.setFont("Times-Roman", 10)
    t.setTextOrigin(0.5 * cm, 5 * cm)
    t.textLine('Blood Group')

    t.setFont("Times-Bold", 10)
    t.setTextOrigin(4.3 * cm, 5 * cm)
    t.textLine(': ' + blood)

    t.setFont("Times-Roman", 10)
    t.setTextOrigin(0.5 * cm, 4.5 * cm)
    t.textLine('Emergency Contact')

    t.setFont("Times-Bold", 10)
    t.setTextOrigin(4.3 * cm, 4.5 * cm)
    t.textLine(': ' + emergency_name)

    t.setFont("Times-Roman", 10)
    t.setTextOrigin(0.5 * cm, 4 * cm)
    t.textLine('Emergency Contact No')

    t.setFont("Times-Bold", 10)
    t.setTextOrigin(4.3 * cm, 4 * cm)
    t.textLine(': ' + emergency_no)
    #
    # t.setFont("Times-Roman", 16)
    # t.setTextOrigin(13.25 * cm, 18 * cm)
    # t.textLine('Photo')
    t.setFont("Times-Italic", 16)
    t.setTextOrigin(14.75 * cm, 5.5 * cm)
    t.setFillColorRGB(0.7, 0.7, 0.7)
    t.textLine('Photo')

    t.setTextOrigin(3 * cm, 2.5 * cm)
    t.setFillColorRGB(0.7, 0.7, 0.7)
    t.textLine('ID Card Front')

    t.setTextOrigin(12 * cm, 2.5 * cm)
    t.setFillColorRGB(0.7, 0.7, 0.7)
    t.textLine('ID Card Back')

    c.drawText(t)


def send_mail(recipient, subject, body, attachment):
    recipients = [recipient]
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = 'narenravi92@gmail.com'
    msg['Reply-to'] = recipient

    msg.preamble = 'Multipart massage.\n'

    part = MIMEText(body)
    msg.attach(part)

    part = MIMEApplication(open(str(attachment), "rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=str(attachment))
    msg.attach(part)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(msg['From'], emaillist, msg.as_string())


def main(metadata):
    print("Generating ID card for Rider")
    uid = '17CC123' # metadata.get('rider_id')
    name = metadata.get('first_name')
    blood = metadata.get('blood_group')
    emergency_name = metadata.get('emergency_name')
    emergency_no = metadata.get('emergency_number')
    rider_no = 111111
    rider_mail = metadata.get('contact_email')
    qr_data = "ID: {0}\n{1}\nBlood Group: {2}\nContact : {3}".format(uid, name, blood, rider_no)
    qr_created = create_qr(str(uid) + '.png', qr_data)
    c = canvas.Canvas(str(uid) + ".pdf", bottomup=1, pagesize=A4)
    c.translate(2 * cm, 2 * cm)
    draw_borders(c)
    draw_banner(c)
    draw_image(c)
    draw_qr(c, qr_created)
    draw_photo(c)
    write_details(c, uid, name, blood, emergency_name, emergency_no)
    write_idcard_details(c, uid, name, blood, emergency_name, emergency_no)
    c.showPage()
    c.save()
    subject = 'WELCOME TO WCCG - We are Chennai Cycling Group'
    header = 'Hey ' + name + ',\n\n' + "Your rider number is {0}.\n\nThanks a bunch for your interest in WCCG! " \
                                       "One of the best cycling groups " \
                                       "in Namma Chennai! We are extremely delighted to have you " \
                                       "\"Ride it out!\" " \
                                       "with us. \n\n".format(uid)
    body = mail_template
    send_mail(rider_mail, subject, header + body, str(uid) + '.pdf')
    return True
