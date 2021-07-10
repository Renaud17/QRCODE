import streamlit as st
import pyqrcode
import png
from pyqrcode import QRCode


col1, col2= st.beta_columns(2)
with col1:
    st.markdown("**Saisissez le texte à convertir:**")
    text=st.text_input("ici",key=0)
    st.markdown("**Entrez le nom de l'image à sauvegarder:**")
    img=st.text_input("ici",key=1)
    if st.button("Générer"):
        # Adding extension as .pnf
        name=img+".png"
        # Creating QR code
        url=pyqrcode.create(text)
        # Saving QR code as  a png file
        url.show()
        url.png(d, scale =6)
with col2:
    #st.image(url.png(d, scale =6))

