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
    load_model = pickle.load(open('data/phosphodiesterase_model.pkl', 'rb'))
    # Apply model to make predictions
    prediction = load_model.predict(input_data)
    st.header('**Prediction output**')
    prediction_output = pd.Series(prediction, name='pIC50')
    molecule_name = pd.Series(load_data[0], name='molecule_name')
    df = pd.concat([molecule_name, prediction_output], axis=1)
    st.write(df)
    st.markdown(filedownload(df), unsafe_allow_html=True)



# Page title
st.markdown("""
# Bioactivity Prediction System with Machine Learning
## Target: Phosphodiesterase 5A
""")

st.markdown("""
This app aims to predict the bioactivity of compounds towards inhibiting the PDE5A enzyme, providing valuable insights and assisting in the discovery of novel drugs for the treatment of pulmonary hypertension.

Pulmonary hypertension (PH) is characterized by high blood pressure in arteries of the lungs, leading to symptoms such as shortness of breath and fatigue. Phosphodiesterase 5A (PDE5A) is crucial for the regulation of vascular smooth muscle in pulmonary arteries. Inhibiting PDE5A can lead to vasodilation and improved blood flow, making it a potential therapeutic target for treating pulmonary hypertension.
""")

st.markdown("""
---
## How to use this app

1. Upload a CSV file containing SMILES strings of your compounds (see the example file).
2. Click the **Predict** button to predict the bioactivity of your molecule against the PDE5A enzyme in pIC50.

""")
image = Image.open('data/logo.png')
st.image(image, use_column_width=True)

st.markdown("""

---
**Credits**
- App built in `Python` + `Streamlit` by [Omar Ahmed](https://www.linkedin.com/in/omar-ahmedd/)
- Molecular Descriptors calculated using [PaDEL-Descriptor](http://www.yapcwsoft.com/dd/padeldescriptor/) [[Read the Paper]](https://doi.org/10.1002/jcc.21707).
- Machine Learning model trained using data from [ChEMBL Database](https://www.ebi.ac.uk/chembl/) obtained on July 5, 2023.
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
    
    with open('molecule.smi', 'r') as file:
        lines = file.readlines()

    lines = [line.replace('"', '') for line in lines] 

    with open('molecule.smi', 'w') as file:
        file.writelines(lines)

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
    Xlist = list(pd.read_csv('data/selected_features.csv').columns)
    desc_subset = desc[Xlist]
    st.write(desc_subset)
    st.write(desc_subset.shape)

    # Apply trained model to make prediction on query compounds
    build_model(desc_subset)
else:
    st.info('Upload input data in the sidebar to start!')