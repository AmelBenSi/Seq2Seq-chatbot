# Seq2Seq chatbot — No Attention vs Attention 
Notebook-based NLP project (imported from **Google Colab**) that builds a **Seq2Seq** model for text generation / chatbot-style responses, compares:
- **Seq2Seq without Attention**
- **Seq2Seq with Attention**
and evaluates both using **BLEU**, then demonstrates a simple **Flask UI**.

---

## Project workflow (notebook order)

Run notebooks in this order:

1. **01-DataLoad.ipynb**  
   Load / merge the raw dataset.

2. **02-DataClean.ipynb**  
   Clean and prepare the dataset.

3. **03-DataProcessing.ipynb**  
   Tokenization + sequence building + padding, and creation of train/val/test artifacts.

4. **04.1-Seq2Seq-NA-Model.ipynb**  
   Train **Seq2Seq No-Attention** model.

5. **04.2-Seq2Seq-WA-Model.ipynb**  
   Train **Seq2Seq With-Attention** model.

6. **05.1-S2SNA-BLEU.ipynb**  
   BLEU evaluation for **No-Attention** model.

7. **05.2-S2SWA-BLEU.ipynb**  
   BLEU evaluation for **With-Attention** model.

8. **06.1-S2SNA-FlaskUI.ipynb**  
   Flask UI demo using **No-Attention** model.

9. **06.2-S2SWA-FlaskUI.ipynb**  
   Flask UI demo using **With-Attention** model.

---

## Configuration (important)

This project uses a shared configuration file: **`config.py`**.

It defines:
- A main dataset directory path: `MAIN_DIR_PATH`
- Filenames for each pipeline stage (raw/cleaned/tokenized/padded/train/val/test)
- Saved model filenames for both versions (no-attention vs attention)

If you are running locally (not Colab/Google Drive), you must update:
- `MAIN_DIR_PATH`

Example filenames expected/produced by the pipeline include:
- `raw_merged_data.csv`
- `cleaned_data.csv`
- `tokenizer.json`
- `tokenized_text.csv`
- `padded_sequences.npz`
- `train_data.npz`, `val_data.npz`, `test_data.npz`
- `seq2seq_no_attention_model.h5`
- `seq2seq_with_attention_model.h5`

(See `config.py` for the authoritative list.)

---

## Quickstart (run locally)

### (Optional) Create & activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
