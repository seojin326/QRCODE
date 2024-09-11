import streamlit as st
import qrcode
from PIL import Image
import io

# QR 코드 생성 함수
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

# Streamlit 앱 설정
st.title('QR 코드 생성기')

# 사용자 입력
data = st.text_input('QR 코드에 담을 내용을 입력하세요:')

if data:
    # QR 코드 생성
    qr_image = generate_qr_code(data)
    
    # 이미지를 바이트로 변환
    buffered = io.BytesIO()
    qr_image.save(buffered, format="PNG")
    qr_image_bytes = buffered.getvalue()
    
    # QR 코드 이미지를 스트림릿에 표시
    st.image(qr_image_bytes, caption='생성된 QR 코드', use_column_width=True)
