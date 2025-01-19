# **Laptop Price Prediction**  

This project is a **Laptop Price Prediction** application built using **Machine Learning**, **Streamlit**, and **Python**.  

The application allows users to predict the price of a laptop based on various features like brand, processor type, RAM size, storage capacity, GPU, screen size, and display resolution.  

## **Features**  
- Select laptop specifications, including:  
  - **Brand**  
  - **Processor Type**  
  - **RAM Size**  
  - **Storage Capacity**  
  - **GPU Specifications**  
  - **Screen Size**  
  - **Display Resolution**  
- Predict the laptop's selling price using a pre-trained machine learning model.  
- Simple and intuitive user interface built with **Streamlit**.  

## **Technologies Used**  
- **Python**: The core programming language used for building the model and backend logic.  
- **Streamlit**: A Python library used to create a web-based user interface.  
- **Pandas**: For data manipulation and preprocessing.  
- **Scikit-learn**: Used to train and develop the machine learning model.  
- **NumPy**: For numerical operations and array handling.  
- **Matplotlib & Seaborn**: For data visualization and exploratory data analysis (EDA).  

## **Setup and Installation**  

### **Prerequisites**  
Make sure you have the following installed:  
- **Python** (version 3.7 or above)  
- **Streamlit** (`pip install streamlit`)  
- **Pandas** (`pip install pandas`)  
- **Scikit-learn** (`pip install scikit-learn`)  
- **NumPy** (`pip install numpy`)  
- **Matplotlib** (`pip install matplotlib`)  
- **Seaborn** (`pip install seaborn`)  

### **Create a Virtual Environment**  
python -m venv venv

### **Activate the Virtual Environment**
venv\Scripts\activate

### **Install Dependencies**
pip install -r requirements.txt

### **Run the Project**
streamlit run app.py

### **File Structure**
-**app.py-**: The main Streamlit application file.
-**laptop_price_model.pkl-**: Pre-trained machine learning model.
-**laptop_data-**.csv: Cleaned dataset used to train the model.
-**README.md-**: Project documentation.

