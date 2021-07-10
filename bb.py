import streamlit as st
import pyqrcode
import png
import matplotlib.pyplot as plt
from pyqrcode import QRCode
import os
import os
import base64
from pyzbar import pyzbar
from PIL import Image

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
        #load qr code imge
        image = Image.open(upload)
        qr_code = pyzbar.decode(image)[0]
        #convert into string
        data= qr_code.data.decode("utf-8")
        type = qr_code.type
        text = f"{type}-->, {data}"
        print("----")
        print(text)
        print("----")



            
            


image_ren ="""
<img src="https://1tpecash.fr/wp-content/uploads/elementor/thumbs/Renaud-Louis-osf6t5lcki4q31uzfafpi9yx3zp4rrq7je8tj6p938.png" alt="Avatar" style="vertical-align: middle;width: 100px;height: 100px;border-radius: 50%;" >
"""

st.sidebar.markdown(image_ren, unsafe_allow_html = True)
st.sidebar.markdown('**Auteur: Renaud Louis DAHOU**')
st.sidebar.markdown('Email:dahou.r@yahoo.com')
st.sidebar.markdown('[Linkedin](https://www.linkedin.com/in/dahou-renaud-louis-8958599a/)')
