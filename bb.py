import streamlit as st
import pyqrcode
import png
from pyqrcode import QRCode


col1, col2= st.beta_columns(2)

with col1:
    NCR = inputcheck(st.text_input("Nombre de Non conformité remontée",value=0,key=0))
    FNCR = inputcheck(st.text_input("Nombre de fiche de Non conformité remontée",value=0,key=1))
    NCC = inputcheck(st.text_input("Nombre de Non conformité cloturée",value=0,key=2))
    FNCC= inputcheck(st.text_input("Nombre de fiche de Non conformité cloturée",value=0, key=3))
    IDD=email
with col2:
    st.subheader("DATE ET NOM DU CHANTIER")
    Date = st.date_input("Date")
    Chantier = st.text_input("Chantier")
    button3=st.button("AJOUTER LES DÉTAILS")
if button3:
    add_NC(IDD,Chantier,NCR,FNCR,NCC,FNCC,Date)
    st.success("AJOUTÉ AVEC SUCCÈS: {}".format(Chantier))

"""
with col1:
    st.markdown("**Saisissez le texte à convertir**")
    text=st.text_input("",key=0)
    st.markdown("**Entrez le nom de l'image à sauvegarder**")
    img=st.text_input("",key=1)
    if st.button("Générer"):
        # Adding extension as .pnf
        name=img+".png"
        # Creating QR code
        url=pyqrcode.create(text)
        # Saving QR code as  a png file
        url.show()
        url.png(d, scale =6)
with col2:
    st.image(url.png(d, scale =6))
"""
