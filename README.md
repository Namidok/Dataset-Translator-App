#Dataset Language Translator
This is a Python-based GUI application that allows users to upload a dataset (in .csv or .xlsx format) and translate its contents into a selected target language. The application uses the googletrans library for translation and openpyxl for handling Excel files.

#Features
File Upload: Users can upload datasets in .csv or .xlsx format.
Language Translation: The application translates the dataset's contents into a user-selected target language.
Supported Languages: The app supports translation into languages like English, French, Spanish, German, Chinese, Japanese, Russian, and Arabic.
Progress Bar: A progress bar updates the user on the translation process.
File Export: The translated dataset is saved as a new Excel file, with the name indicating the target language.
Requirements
Ensure the following Python libraries are installed before running the application:

tkinter: For building the GUI (comes pre-installed with Python).
pandas: For handling datasets.
googletrans==4.0.0-rc1: For translating text.
openpyxl: For reading and writing Excel files.
numpy: For handling NaN values in the dataset.
To install the required packages, run:

bash
Copy code
pip install pandas googletrans==4.0.0-rc1 openpyxl numpy
How to Use
Clone or Download the Repository: Download this repository and navigate to the folder.

Run the Application: Run the following command to start the application:

bash
Copy code
python dataset_translator.py
Upload Dataset:

Click on the "Upload Dataset" button.
Select a .csv or .xlsx file from your system.
Select Target Language:

Use the dropdown menu to select the target language for translation.
Translate Dataset:

Once the dataset is uploaded and a language is selected, click "Translate Dataset" to begin the translation process.
The progress bar will show the status of the translation.
After the translation completes, the application will save the translated dataset with the language code appended to the original filename.
Supported Languages
The following languages are supported by default in this application:

English (en)
French (fr)
Spanish (es)
German (de)
Chinese (zh-cn)
Japanese (ja)
Russian (ru)
Arabic (ar)
You can add more languages by modifying the languages dictionary in the code.

Error Handling
If no dataset is selected, an error message will prompt the user to upload a file.
If a cell contains NaN, NoneType, or empty strings, the original value is retained without translation.
Code Structure
dataset_translator.py: The main script containing all functionality, including file upload, language selection, dataset translation, and file saving.
Translation: The googletrans library is used to translate non-empty strings. If any translation fails, the original text is preserved.
License
This project is licensed under the MIT License. You are free to use, modify, and distribute the application as you wish.
