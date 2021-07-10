import streamlit as st
import pyqrcode
import png
import matplotlib.pyplot as plt
from pyqrcode import QRCode
import os


def get_image_download_link(img,filename,text):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href



col1, col2= st.beta_columns(2)
with col1:
    st.markdown("**Saisissez le texte à convertir:**")
    text=st.text_input("",key=0)
    st.markdown("**Entrez le nom de l'image à sauvegarder:**")
    img=st.text_input("",key=1)
    if st.button("Générer"):
        # Adding extension as .pnf
        name=img+".png"
        # Creating QR code
        url=pyqrcode.create(text)
        # Saving QR code as  a png file
        url.show()
        url.png(name, scale =6)
        with col2:
            st.image(name)
            ## Original image came from cv2 format, fromarray convert into PIL format
            result = Image.fromarray(name)
            st.markdown(get_image_download_link(result,img_file.name,'Download '+img_file.name), unsafe_allow_html=True)
            
            


