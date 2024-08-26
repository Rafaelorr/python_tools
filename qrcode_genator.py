import segno

# error correction "M1" "L" "M" "Q" "H"
text = input("qrcode tekst: ")
scale = int(input("grootte: "))
border = int(input("border: "))
version = int(input("qrcode version: "))
error = input("error correction level: ")
file_name = input("file name: ")
light_color = input("light color: ")
data_light_color = input("data light color: ")
dark_color = input("dark color: ")
data_dark_color = input("data dark color: ")
quiet_zone_color = input("quiet zone color: ")

qrcode = segno.make_qr(content=text,error=error,version=version)
qrcode.save(file_name, 
            scale=scale,
            border=border,
            light=light_color,
            data_light=data_light_color,
            dark=dark_color,
            data_dark=data_dark_color,
            quiet_zone=quiet_zone_color)
