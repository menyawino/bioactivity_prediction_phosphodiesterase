# Bioactivity Prediction System for Phosphodiesterase 5A (PDE5A)

Welcome to the Bioactivity Prediction System for Phosphodiesterase 5A (PDE5A) repository! This project aims to provide a powerful tool for predicting the bioactivity of compounds targeting the PDE5A enzyme, with the ultimate goal of assisting in the discovery of novel drugs for the treatment of pulmonary hypertension.

## About

Pulmonary hypertension (PH) is a debilitating condition characterized by high blood pressure in the arteries of the lungs, resulting in significant health challenges for patients. By targeting the phosphodiesterase 5A (PDE5A) enzyme, which plays a crucial role in regulating vascular smooth muscle tone in the pulmonary arteries, there is potential to enhance blood flow and alleviate symptoms, offering new possibilities for the management of pulmonary hypertension.

The Bioactivity Prediction System leverages advanced machine learning techniques and molecular descriptor calculations using PaDEL-Descriptor, a widely used tool for analyzing chemical structures. This system provides a platform to accelerate the drug discovery process, enabling researchers and scientists to efficiently analyze compound bioactivities and make informed decisions.

## Features

- Predicts the bioactivity of compounds targeting the PDE5A enzyme
- Utilizes state-of-the-art machine learning algorithms for accurate predictions
- Integrates molecular descriptor calculations using PaDEL-Descriptor
- Generates insightful predictions to aid in the discovery of novel drugs for pulmonary hypertension

## Biological and Computational Rationale
### Why Target PDE5A?
PDE5A is a clinically validated target for PH. Understanding how structural features of chemical compounds influence their ability to inhibit PDE5A can guide the development of next-generation drugs with improved potency and safety profiles.

### Why Use Machine Learning?
Traditional high-throughput screening methods for identifying bioactive compounds are expensive and time-intensive. Machine learning can analyze large datasets of chemical structures and activities, uncovering patterns that predict bioactivity. This approach not only accelerates the screening process but also reduces the reliance on costly lab experiments.

### Why PaDEL-Descriptor?
Molecular descriptors, such as lipophilicity and molecular weight, capture critical properties of chemical structures that correlate with biological activity. PaDEL-Descriptor is a robust tool that computes these features efficiently, making it a natural choice for input into machine learning models.

## Scientific Workflow: From Data to Prediction
The project comprises several key steps, each contributing to the overarching goal of discovering new PDE5A inhibitors:

### Data Preparation:

Chemical structure datasets are curated and formatted. Known PDE5A inhibitors and inactive compounds are included for model training and validation.
###Feature Engineering:

Molecular descriptors are computed using PaDEL-Descriptor, yielding a numerical representation of each compound's chemical structure.

### Model Training and Validation:

Advanced machine learning algorithms, such as random forests and gradient boosting, are trained to predict bioactivity based on molecular descriptors.
Performance metrics, including accuracy, precision, and recall, ensure the reliability of the models.

### Predictive Analysis:

The trained model is deployed to evaluate new compounds, highlighting promising candidates for further experimental validation.
## Getting Started

To get started with the Bioactivity Prediction System, please follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using the provided `requirements.txt` file.
3. Ensure that Java is installed on your system to run the PaDEL-Descriptor tool.
4. Make sure you modify launch.json file to run streamlit
5. Prepare your input data file in the appropriate format (refer to the example file provided).
6. Launch the application by running the main script.

## Credits

- Built with `Python` and `Streamlit` by [Omar Ahmed](https://www.linkedin.com/in/omar-ahmedd/)
- Molecular descriptors calculated using [PaDEL-Descriptor](http://www.yapcwsoft.com/dd/padeldescriptor/) - [[Read the Paper]](https://doi.org/10.1002/jcc.21707)

## Contact

For any inquiries or suggestions, please feel free to reach out to [omarahmedd@aucegypt.edu]. I value your feedback and would be delighted to connect and collaborate on further advancements in this project.
