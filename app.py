import streamlit as st
import pandas as pd
from PIL import Image
import subprocess
import os
import base64
import pickle

def desc_calc():
    # Performs the descriptor calculation
    bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/PubchemFingerprinter.xml -dir ./ -file descriptors_output.csv"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    os.remove('molecule.smi')

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    return href

def build_model(input_data):
    # Reads in saved regression model
    load_model = pickle.load(open('D:\PROJECTS\Bioinformatics I\Big Bioinformatics Camp\Drug Discovery\Phosphodiesterase\phosphodiesterase_model copy.pkl', 'rb'))
    # Apply model to make predictions
    prediction = load_model.predict(input_data)
    st.header('**Prediction output**')
    prediction_output = pd.Series(prediction, name='pIC50')
    molecule_name = pd.Series(load_data[1], name='molecule_name')
    df = pd.concat([molecule_name, prediction_output], axis=1)
    st.write(df)
    st.markdown(filedownload(df), unsafe_allow_html=True)

image = Image.open('logo.png')
st.image(image, use_column_width=True)

# Page title
st.markdown("""
# Bioactivity Prediction System (Phosphodiesterase 5A)

This app aims to predict the bioactivity of compounds towards inhibiting the PDE5A enzyme, providing valuable insights and assisting in the discovery of novel drugs for the treatment of pulmonary hypertension.

Pulmonary hypertension (PH) is a debilitating condition characterized by high blood pressure in the arteries of the lungs, leading to symptoms such as shortness of breath and fatigue. The phosphodiesterase 5A (PDE5A) enzyme plays a crucial role in the regulation of vascular smooth muscle tone in the pulmonary arteries. Inhibiting PDE5A can lead to vasodilation and improved blood flow, making it a potential therapeutic target for treating pulmonary hypertension.

**Credits**
- App built in `Python` + `Streamlit` by [Omar Ahmed](https://www.linkedin.com/in/omar-ahmedd/)
- Molecular Descriptors calculated using [PaDEL-Descriptor](http://www.yapcwsoft.com/dd/padeldescriptor/) [[Read the Paper]](https://doi.org/10.1002/jcc.21707).
---
""")

# Sidebar
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input file", type=['txt'])
    st.sidebar.markdown("""
[Example input file](https://raw.githubusercontent.com/menyawino/bioactivity_prediction_phosphodiesterase/main/example_phosphodiesterase.txt)
""")

if st.sidebar.button('Predict'):
    load_data = pd.read_table(uploaded_file, sep=' ', header=None)
    load_data.to_csv('molecule.smi', sep = '\t', header = False, index = False)

    st.header('**Original input data**')
    st.write(load_data)

    with st.spinner("Calculating descriptors..."):
        desc_calc()

    # Read in calculated descriptors and display the dataframe
    st.header('**Calculated molecular descriptors**')
    desc = pd.read_csv('descriptors_output.csv')
    st.write(desc)
    st.write(desc.shape)

    # Read descriptor list used in previously built model
    st.header('**Subset of descriptors from previously built models**')
    Xlist = list(pd.read_csv('descriptor_list.csv').columns)
    desc_subset = desc[Xlist]
    st.write(desc_subset)
    st.write(desc_subset.shape)

    # Apply trained model to make prediction on query compounds
    build_model(desc_subset)
else:
    st.info('Upload input data in the sidebar to start!')