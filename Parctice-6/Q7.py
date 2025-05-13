with open('img1.jpg','rb')as file:
    image=file.read()
with open('img2.jpg','wb')as file:
    file.write(image)
import zipfile as zf
with zf.ZipFile("imp_img",'w') as zipf:
    zipf.write('img1.jpg')
    zipf.write('img2.jpg')
