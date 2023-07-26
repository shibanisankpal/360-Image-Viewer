import streamlit as st
import base64

def main():
    st.title('VR 360° Image Viewer')
    st.write('Drag and drop your 360° image here:')
    
    # File Uploader to get the 360° image from the user
    uploaded_file = st.file_uploader("Choose a 360° image...", type=['jpg', 'png', 'jpeg'])
    
    if uploaded_file is not None:
        # Display the 360° image
        st.write("Uploaded 360° Image:")
        st.image(uploaded_file, use_column_width=True)
        
        # Convert the image to base64 to use in the A-Frame HTML
        encoded_image = base64.b64encode(uploaded_file.read()).decode('utf-8')
        
        # Create the A-Frame HTML for the 360° image viewer
        aframe_html = f'''
            <head>
                <script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>
            </head>
            <body>
                <a-scene>
                    <a-sky src="data:image/png;base64,{encoded_image}" rotation="0 -130 0"></a-sky>
                </a-scene>
            </body>
        '''
        st.components.v1.html(aframe_html, height=500)

if __name__ == '__main__':
    main()
