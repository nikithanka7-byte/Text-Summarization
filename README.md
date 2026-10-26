#  Hugging Face Pipelines – Text Summarization

##  Project Overview

This project is an AI-powered text summarization application built using **Hugging Face Transformers and Streamlit**.

The application uses a pretrained NLP model to generate concise summaries from long articles, paragraphs, and study materials. Users can enter text, choose a summary length, generate a summary, and download the result as a text file.

##  Objectives

* Understand Hugging Face Transformers Pipelines.
* Perform automatic text summarization using a pretrained model.
* Build an interactive web application using Streamlit.
* Allow users to choose summary length.
* Download generated summaries as text files.

## Technologies Used

* **Python** – Programming language.
* **Hugging Face Transformers** – NLP model and summarization pipeline.
* **PyTorch** – Deep learning framework.
* **Streamlit** – Web application interface.
* **DistilBART CNN** – Pretrained text summarization model.

##  Model Information

This project uses the pretrained model:

`sshleifer/distilbart-cnn-12-6`

The model is designed for English news-style summarization and generates shorter versions of input text while attempting to preserve its main ideas.


##  Project Structure

```text
Text_Summarization/
│
├── app.py
├── requirements.txt
└── README.md
```

##  Requirements

* Python 3.12
* Internet connection for the initial model download
* VS Code or another Python editor
* Required Python libraries listed in `requirements.txt`


## Application link - 


## Application preview
<img width="1317" height="575" alt="image" src="https://github.com/user-attachments/assets/ec39ccf4-5039-4009-a973-d2b84fac597a" />
<img width="1319" height="548" alt="image" src="https://github.com/user-attachments/assets/1eb73aa2-852a-4075-99aa-da8863bd22fd" />


## Installation and Setup

### Step 1: Clone the Repository

If your project is hosted on GitHub, run:

```bash
git clone https://github.com/nikithanka7-byte/Text-Summarization/tree/main
```

Navigate to the project directory:

```bash
cd Text_Summarization
```

Alternatively, open your existing project folder in VS Code.

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

### Step 4: Install Dependencies

Make sure your `requirements.txt` contains:

```text
streamlit
transformers==4.46.3
torch
sentencepiece
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 5: Run the Application

Execute the following command:

```bash
python -m streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that address in your browser to use the application.

Usually, the address is:

`http://localhost:8501`

##  How to Use the Application

1. Open the application in your browser.
2. Enter or paste an article or paragraph into the text area.
3. Choose a summary length: Short, Medium, or Long.
4. Click **Generate Summary**.
5. Wait for the model to process the text.
6. Read the generated summary.
7. Click **Download Summary** to save it as a `.txt` file.

##  How It Works

1. **Text Input:** The user provides the text to summarize.
2. **Model Loading:** Hugging Face loads the pretrained DistilBART model.
3. **Text Processing:** The tokenizer converts the input text into tokens.
4. **Summary Generation:** The summarization pipeline generates a shorter version of the text.
5. **Result Display:** Streamlit displays the generated summary.
6. **Download:** The user can download the summary as a text file.

##  Python Dependencies

| Library         | Purpose                                          |
| --------------- | ------------------------------------------------ |
| `streamlit`     | Creates the web interface                        |
| `transformers`  | Provides the Hugging Face summarization pipeline |
| `torch`         | Runs the deep learning model                     |
| `sentencepiece` | Supports tokenizer functionality where required  |

##  Features

* Simple and interactive user interface.
* AI-powered text summarization.
* Three summary length options.
* Original and summary word counts.
* Downloadable summary files.
* Pretrained model; no model training required.

##  Limitations

* The model is optimized for English news-style summarization.
* Very long input text may be truncated because of model input limits.
* Summary quality depends on the input text and model.
* The first model download requires an internet connection.
* Processing speed depends on the computer's hardware.
* The generated summary may omit details or occasionally misrepresent information, so important results should be checked.

##  Future Improvements

* Support uploading TXT and PDF documents.
* Add multilingual summarization.
* Support longer documents through text chunking.
* Improve the user interface.
* Deploy the application online.
* Add additional summarization models.




---

