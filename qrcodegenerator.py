import qrcode
import image
qr = qrcode.QRCode(
    version = 5, # 15 adalah versi qrcode yg sesuai dengan tingkat susahnya gambar
    box_size = 10, # 10 adalah ukuran yang akan ditampilkan
    border = 5 # adalah bagian putih di antara sisi sisi gambar
)

data = "aku sayang kamu"
# jalur dari scan qrcode mengarah ke variable data

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("fromqrgenerator.png")