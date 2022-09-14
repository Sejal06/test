import qrcode
#version-size--1 to 40
qr=qrcode.QRCode(version=25,
error_correction=qrcode.constants.ERROR_CORRECT_L,
box_size=10,
border=4,
)
#Add_data hold information which we want to pass in qrcode
qr.add_data("https://youtu.be/syFZfO_wfMQ")
qr.make(fit=True)
#Fit is used to match the dimension with qr code
img1 = qr.make_image(fillcolor=" Blue",back_color="white")
img1.save("C:\Users\Sejal\Desktop\P.png")