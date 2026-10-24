# AI Text Summarizer

An AI-powered text summarization application built using Python and a pretrained Hugging Face model. It converts lengthy text into concise summaries with configurable output lengths and input validation.

## Project Overview

The AI Text Summarizer uses a pretrained DistilBART model to generate short, meaningful summaries from user-provided text. It supports different summary lengths and includes an evaluation process to assess factual accuracy and instruction following.

## Features

- **Automatic Summarization:** Generates concise summaries from input text.
- **Adjustable Summary Length:** Supports short, medium, and long summaries.
- **Input Validation:** Handles empty input and rejects excessively long text.
- **Pretrained AI Model:** Uses an existing model without training from scratch.
- **Evaluation:** Tests five examples across different topics.
- **CSV Results:** Saves generated summaries and evaluation records for further analysis.

## Technologies Used

- Python
- Hugging Face Transformers
- PyTorch
- Pandas
- VS Code

## Model Used

**Model:** `sshleifer/distilbart-cnn-12-6`

This pretrained model is based on the BART architecture and fine-tuned for summarization. It generates summaries using the supplied text and configurable generation parameters.

## Project Structure

```text
AI_Text_Summarizer/
├── main.py
├── evaluate.py
├── calculate_scores.py
├── requirements.txt
├── README.md
└── outputs/
    └── evaluation_results.csv
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd AI_Text_Summarizer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the summarizer

```bash
python main.py
```

Enter your text and select the required summary length.

### 5. Evaluate the model

```bash
python evaluate.py
```

The generated summaries and evaluation records are saved in the `outputs/` directory.

## Evaluation Methodology

Five sample texts were evaluated:

1. Artificial Intelligence
2. Climate Change
3. Education
4. Healthcare
5. Cybersecurity

Each summary was reviewed against its original input for factual correctness, preservation of the main idea, and compliance with the requested output.

### Evaluation Results

| Evaluation Stage | Factual Accuracy / Support Rate |
|---|---:|
| Initial evaluation | 80% |
| After updating and re-evaluating | 100% |

The initial evaluation identified an issue in one of the test cases. After updating the implementation and reviewing the generated outputs again, the reported score increased to 100%.

*These scores reflect the project's five-example evaluation and are not a guarantee of general model accuracy.*

## Limitations

- Summaries may omit relevant details from the original text.
- The model may generate incomplete or inaccurate statements.
- Summary length settings control generated tokens rather than an exact number of words.
- Evaluation on five examples is limited and does not establish performance across all types of documents.

## Future Improvements

- Build a web interface using Streamlit or Flask.
- Add support for uploading text files and documents.
- Evaluate summaries using ROUGE scores.
- Test the model on a larger and more diverse dataset.
- Improve factual consistency and summary completeness.

## Conclusion

This project demonstrates how a pretrained language model can be used to automate text summarization. It combines adjustable summary lengths, input validation, and manual evaluation to provide a simple, practical introduction to natural language processing and generative AI.

## Author

Developed as a mini project on **Prompt Design and AI Text Summarization**.
