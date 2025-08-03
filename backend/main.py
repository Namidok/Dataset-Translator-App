from fastapi import FastAPI, File, UploadFile, Form, Response
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from googletrans import Translator
import io

app = FastAPI()

# CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/translate/")
async def translate(file: UploadFile = File(...), target_language: str = Form(...)):
    try:
        # Read the uploaded file into a pandas DataFrame
        if file.filename.endswith('.csv'):
            df = pd.read_csv(io.StringIO(file.file.read().decode('utf-8')))
        elif file.filename.endswith('.xlsx'):
            df = pd.read_excel(io.BytesIO(file.file.read()))
        else:
            return {"error": "Unsupported file format"}

        # Translate the dataset
        translator = Translator()
        for column in df.columns:
            for i, value in enumerate(df[column]):
                if isinstance(value, str) and value.strip():
                    try:
                        translated_value = translator.translate(value, dest=target_language).text
                        df.at[i, column] = translated_value
                    except Exception as e:
                        print(f"Translation error for row {i} and column {column}: {str(e)}")
                        df.at[i, column] = value
                else:
                    df.at[i, column] = value

        # Save the translated DataFrame to a new Excel file in memory
        output = io.BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        output.seek(0)

        return Response(content=output.read(), media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={'Content-Disposition': f'attachment; filename="translated_{file.filename}"'})    

    except Exception as e:
        return {"error": str(e)}
