# import module
import qrcode
from PIL import Image

# get logo link
logo_link = 'kroeng-logo.png';
logo = Image.open(logo_link);

basewidth = 100

# adjust image size
wpercent = (basewidth/float(logo.size[0]));
hsize = int((float(logo.size[1])*float(wpercent)));
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS);
QRCode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
);

# taking url 
url = 'http://pinjamalat.kroengusk.eu.org/';

# adding URL QRCode
QRCode.add_data(url);

# generating QRCode
QRCode.make();

# taking color name from user
QRColor = 'Black';

# adding color to QR code
QRimg = QRCode.make_image(
    fill_color = QRColor, back_color="white"
).convert('RGB');

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2);
QRimg.paste(logo, pos);

# save the QR code generated
QRimg.save('pinjamalat-kroengusk.png');

print("Done");