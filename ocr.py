# import sys
# import os

# # 添加 packages 目录到 LD_LIBRARY_PATH
# sys.path.append(os.path.join(os.getcwd(), "packages"))
# os.environ['LD_LIBRARY_PATH'] = os.path.join(os.getcwd(), "packages")


import easyocr as ocr  # OCR
# from paddleocr import PaddleOCR, draw_ocr
import streamlit as st  # Web App
from PIL import Image  # Image Processing
import numpy as np  # Image Processing

# title
st.title("OCR - Extract Text from Images")

# subtitle
# st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

st.markdown("")

# image uploader
image = st.file_uploader(label="Upload your image here: ", type=['png', 'jpg', 'jpeg'])


# # 创建一个选择框，用户可以从列表中选择一个值
# selected_option = st.selectbox("Choose language", ["英文", "中文", "Option 3"])
#
# lang_dict = {
#     "英文": "en",
#     "中文": "ch_sim",
# }

@st.cache_resource
def load_model():
    reader = ocr.Reader(['en', 'ch_sim'], model_storage_directory='.', gpu=False)
    # reader = PaddleOCR(use_angle_cls=True, lang="ch")
    return reader


reader = load_model()  # load model

if image is not None:
    input_image = Image.open(image)  # read image
    st.image(input_image)  # display image

    with st.spinner("Pending..."):
        result = reader.readtext(np.array(input_image))
        # result = reader.ocr(np.array(input_image), cls=True)

        # result_mod = result[0]

        # txts = [str(line[1][0]) for line in result_mod]

        # text_all = " ".join(txts)

        result_text = []  # empty list for results
        
        for text in result:
            result_text.append(text[1])

        text_all = " ".join(result_text)

        st.markdown("## After OCR: ")
        
        st.write(result_text)
    # st.success("Here you go!")
    # st.balloons()
# else:
#     st.write("Upload an Image")

st.caption("Made by :red[lolo] :sunglasses:")
