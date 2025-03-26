import base64
import streamlit as st
import io
import pdf2image
import google.generativeai as genai

def get_gemini_response(input, pdf_content, prompt):
    model=genai.GenerativeModel('gemini-2.0-flash')
    response=model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(
            uploaded_file.read(),
            poppler_path=r'C:\Users\Mouli\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin'  # Needed for Windows
            # Or for Linux/Mac: poppler_path='/usr/bin/'
        )

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")
user_api_key = st.text_input("Enter your Gemini API Key", type="password", 
                           help="Get your API key from https://aistudio.google.com/app/apikey")
st.subheader("Upload your resume and job description to get started")
st.text("Made with ❤️ for fellow job seekers by Mouli")

input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("What are the skills that I should add in my resume to improve the match?")

submit3 = st.button("Percentage match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""
input_prompt2 = """
You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
 Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if not user_api_key:
        st.error("Please enter your Gemini API key to proceed.")
    elif uploaded_file is not None:
        genai.configure(api_key=user_api_key)
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("Here you go")
        st.write(response)
    else:
        st.write("Please upload the resume")

if submit2:
    if not user_api_key:
        st.error("Please enter your Gemini API key to proceed.")
    elif uploaded_file is not None:
        genai.configure(api_key=user_api_key)
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("Here you go")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if not user_api_key:
        st.error("Please enter your Gemini API key to proceed.")
    elif uploaded_file is not None:
        genai.configure(api_key=user_api_key)
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("Here you go")
        st.write(response)
    else:
        st.write("Please upload the resume")



   





