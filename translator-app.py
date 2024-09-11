import pandas as pd
from googletrans import Translator
from tkinter import Tk, filedialog, Label, Button, StringVar, OptionMenu, messagebox
from tkinter.ttk import Progressbar
import os
import numpy as np

# Function to upload a dataset
def upload_dataset():
    file_path = filedialog.askopenfilename(
        title="Select Dataset",
        filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")]
    )
    if file_path:
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                df = pd.read_excel(file_path)
            else:
                messagebox.showerror("Error", "Unsupported file format.")
                return None, None
            return df, file_path
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load dataset: {str(e)}")
            return None, None
    else:
        return None, None

# Function to translate dataset
def translate_dataset(df, target_language, progress_bar):
    translator = Translator()
    total_rows = len(df)
    current_row = 0
    
    try:
        for column in df.columns:
            for i, value in enumerate(df[column]):
                # Check if the value is a valid string and not NaN/None
                if isinstance(value, str) and value.strip():  # Only translate non-empty strings
                    try:
                        translated_value = translator.translate(value, dest=target_language).text
                        df.at[i, column] = translated_value
                    except Exception as e:
                        # If the translation fails for any reason, keep the original value
                        print(f"Translation error for row {i} and column {column}: {str(e)}")
                        df.at[i, column] = value
                else:
                    # If the value is NaN or NoneType, leave it unchanged
                    df.at[i, column] = value
                # Update progress bar after each row
                current_row += 1
                progress = (current_row / (total_rows * len(df.columns))) * 100
                progress_bar['value'] = progress
                progress_bar.update_idletasks()  # Updates the progress bar on the UI
        return df
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during translation: {str(e)}")
        return None

# Function to save the translated dataset
def save_translated_file(df, original_file_path, target_language):
    base, ext = os.path.splitext(original_file_path)
    save_path = f"{base}_{target_language}.xlsx"
    try:
        df.to_excel(save_path, index=False, engine='openpyxl')
        messagebox.showinfo("Success", f"Translated dataset saved as: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save the translated file: {str(e)}")

# Function to handle the translation process
def handle_translation():
    # Reset the progress bar
    progress_bar['value'] = 0

    df, file_path = upload_dataset()
    if df is None:
        return

    # Get the selected language
    target_language = selected_language.get()
    if not target_language:
        messagebox.showerror("Error", "Please select a target language.")
        return

    # Translate Dataset
    translated_df = translate_dataset(df, target_language, progress_bar)
    if translated_df is not None:
        save_translated_file(translated_df, file_path, target_language)


def create_gui():
    root = Tk()
    root.title("Dataset Language Translator")
    root.geometry("400x250")


    label = Label(root, text="Select a dataset and a target language:")
    label.pack(pady=10)


    languages = {
        'English': 'en',
        'French': 'fr',
        'Spanish': 'es',
        'German': 'de',
        'Chinese': 'zh-cn',
        'Japanese': 'ja',
        'Russian': 'ru',
        'Arabic': 'ar'
    }
    global selected_language
    selected_language = StringVar()
    selected_language.set('en')  # Default value

    language_menu = OptionMenu(root, selected_language, *languages.values())
    language_menu.pack(pady=10)

    # Button to Start Translation
    translate_button = Button(root, text="Translate Dataset", command=handle_translation)
    translate_button.pack(pady=20)

    # Progress Bar
    global progress_bar
    progress_bar = Progressbar(root, orient='horizontal', length=300, mode='determinate')
    progress_bar.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
