# Dataset Translator App
This is a Python-based GUI application that allows users to upload a dataset (in .csv or .xlsx format) and translate its contents into a selected target language. The application uses the googletrans library for translation and openpyxl for handling Excel files.

# Requirements
Requirements
Ensure the following Python libraries are installed before running the application:

tkinter: For building the GUI (comes pre-installed with Python),pandas: For handling datasets,googletrans==4.0.0-rc1: For translating text,openpyxl: For reading and writing Excel files,numpy: For handling NaN values in the dataset.

# Install Packages
pip install pandas googletrans==4.0.0-rc1 openpyxl numpy

# How to use
1.Clone or Download the Repository: Download this repository and navigate to the folder.


2.Run the Application: Run the following command to start the application:


python dataset_translator.py

3.Upload Dataset

4.Click on the "Upload Dataset" button.

5.Select a .csv or .xlsx file from your system.


6.Select target language in the drop down

7.Translate Dataset

8.Once the dataset is uploaded and a language is selected, click "Translate Dataset" to begin the translation process.

9.The progress bar will show the status of the translation.


10.After the translation completes, the application will save the translated dataset with the language code appended to the original filename.

# Code Structure

1.dataset_translator.py: The main script containing all functionality, including file upload, language selection, dataset translation, and file saving.

2.Translation: The googletrans library is used to translate non-empty strings. If any translation fails, the original text is preserved.

# License

This project is licensed under the MIT License. You are free to use, modify, and distribute the application as you wish.




