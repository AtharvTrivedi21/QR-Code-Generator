import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# Function to generate QR code
def generate_qr_code(url: str) -> BytesIO:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    buffered.seek(0)
    return buffered

# Streamlit app layout
st.title("QR Code Generator")
st.write("Enter a URL to generate a QR code.")

# User input for URL
url = st.text_input("Enter URL:")

# Generate and display QR code if URL is provided
if url:
    qr_buffer = generate_qr_code(url)
    
    # Display QR code
    st.image(qr_buffer, caption="Generated QR Code", width= 300)

    # Download button for the QR code
    st.download_button(
        label="Download QR Code",
        data=qr_buffer,
        file_name="qr_code.png",
        mime="image/png"
    )
