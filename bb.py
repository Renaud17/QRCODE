import streamlit as st
import pyqrcode
import png
import matplotlib.pyplot as plt
from pyqrcode import QRCode
import os
import base64
from PIL import Image

result = Image.fromarray(name)
def get_image_download_link(img):
	"""Generates a link allowing the PIL image to be downloaded
	in:  PIL image
	out: href string
	"""
	buffered = BytesIO()
	img.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href = f'<a href="data:file/jpg;base64,{img_str}">Download result</a>'
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
            st.markdown(get_image_download_link(result), unsafe_allow_html=True)
            


