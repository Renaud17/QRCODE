import streamlit as st
import pyqrcode
import png
import matplotlib.pyplot as plt
from pyqrcode import QRCode
import os
import os
import base64
import cv2

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">👉Télécharger {file_label}</a>'
    return href



col1, col2= st.beta_columns(2)
with col1:
    st.subheader("Générateur de code QR")
    text=st.text_input("Saisissez le texte à convertir:",key=0)
    #st.markdown("****")
    img=st.text_input("Entrez le nom de l'image à sauvegarder:",key=1)
col3,col4,col5= st.beta_columns([1,6,1])
with col3:
    if st.button("Générer"):
        # Adding extension as .pnf
        name=img+".png"
        # Creating QR code
        url=pyqrcode.create(text)
        # Saving QR code as  a png file
        url.show()
        url.png(name, scale =6)
        st.image(name)
        st.markdown(get_binary_file_downloader_html(name, 'ICI'), unsafe_allow_html=True)

        
with col2:
    st.markdown("<h3 style='text-align: right; color: black;'>Lècteur de code QR</h3>", unsafe_allow_html=True)
    upload =st.file_uploader("Image QRC ici")
    if st.button("Lècture",key=1):
        img = cv2.imread(upload)
        detector = cv2.QRCodeDetector()
        # detect and decode
        data, bbox, straight_qrcode = detector.detectAndDecode(img)
        # if there is a QR code
        if bbox is not None:
            #print(f"QRCode data:\n{data}")
            # display the image with lines
            # length of bounding box
            n_lines = len(bbox)
        for i in range(n_lines):
            # draw all lines
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
            cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
#with col5:
    


            
            


image_ren ="""
<img src="https://1tpecash.fr/wp-content/uploads/elementor/thumbs/Renaud-Louis-osf6t5lcki4q31uzfafpi9yx3zp4rrq7je8tj6p938.png" alt="Avatar" style="vertical-align: middle;width: 100px;height: 100px;border-radius: 50%;" >
"""

st.sidebar.markdown(image_ren, unsafe_allow_html = True)
st.sidebar.markdown('**Auteur: Renaud Louis DAHOU**')
st.sidebar.markdown('Email:dahou.r@yahoo.com')
st.sidebar.markdown('[Linkedin](https://www.linkedin.com/in/dahou-renaud-louis-8958599a/)')
