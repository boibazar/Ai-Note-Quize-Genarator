import streamlit as st
from PIL import Image
from api import generate_note , generate_audio, generate_quize

st.title("Note Taking App")
st.divider()

bt = False
with st.sidebar:
    st.header("Comtrol Section")


    #image section
    image = st.file_uploader("Uplode Image",type=["jpg","png","jpeg"], accept_multiple_files = True)
    if image:
        if len(image) > 3:
            st.error("Max Uplode 3 Image")
        else :
            st.subheader("Uploded image is ")
            col = st.columns(len(image))
            
            for i, img in enumerate(image):
                with col[i]:
                    st.image(img)



    deficulty = st.selectbox("Enter the Deficulty ", ("Easy","Mid","Hard"), index = None)
    if deficulty and image:

        bt = st.button("Click to Submit", type = "primary")
    

if bt:
    with st.container(border = True):
        st.subheader("Your Note")


        with st.spinner("W8 a Bit ..."):
            # convat to pil image
            pil_image = []
            for img in image:
                pil_image.append(Image.open(img))
                
            note = generate_note(pil_image)
            st.markdown(note)
        

    with st.container(border = True):
        st.subheader("Audio")
        with st.spinner("Generate Audio..."):
            st.audio(generate_audio(note))

    with st.container(border = True):
        st.subheader(f"Quize Part with {deficulty} deficulty")
        with st.spinner():
            st.markdown(generate_quize(pil_image, deficulty))
        
        