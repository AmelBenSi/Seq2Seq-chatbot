# Seq2Seq Chatbot — No Attention vs Attention + BLEU + Flask UI

Notebook-based NLP project (imported from **Google Colab**) that builds a **Seq2Seq** model for text generation / chatbot-style responses, compares:
- **Seq2Seq without Attention**
- **Seq2Seq with Attention**
and evaluates both using **BLEU**, then demonstrates a simple **Flask UI**.

---

## What this repo does
It builds a **Seq2Seq** chatbot/text-generation pipeline using:
- Data loading + cleaning
- Text processing (tokenization + sequence building + padding)
- Two model variants:
  - **Seq2Seq without Attention**
  - **Seq2Seq with Attention**
- Evaluation using **BLEU**
- A simple **Flask UI** demo notebook

---

## Dataset — Ubuntu Dialogue Corpus

This project uses the **Ubuntu Dialogue Corpus**, consisting of almost **one million** two-person conversations extracted from Ubuntu chat logs.  
It contains approximately **930,000 dialogues** spanning about **100,000,000 words**, making it well-suited for training chatbot models.

### Download
- Official dataset page: https://www.kaggle.com/datasets/rtatman/ubuntu-dialogue-corpus

### How to use it
1. Download the Ubuntu Dialogue Corpus from the link above.
2. Place it under the directory defined in `config.py` (`MAIN_DIR_PATH`), **or** update `MAIN_DIR_PATH` to match your local setup.
3. Run the notebooks in order starting from **`01-DataLoad.ipynb`**.

> The pipeline saves intermediate artifacts (CSV/NPZ/JSON) so later notebooks can run faster without repeating earlier steps.

---

## Note: known issue (Question–Answer pair creation needs fixing)

The code still needs a **small update** in the step where **question–answer (input–output) pairs** are created, to ensure **correct alignment** between encoder inputs and decoder targets.

### What to verify / fix (recommended)
- **Do not cross dialogue boundaries** when pairing consecutive turns (avoid using the last utterance of one dialogue as the “question” and the first utterance of the next dialogue as the “answer”).
- Ensure true **shifted decoder training**:
  - `decoder_input = <SOS> + target_tokens`
  - `decoder_output = target_tokens + <EOS>`
  - and they are **shifted by 1** (teacher forcing alignment).
- Confirm you **exclude turns without a valid next turn** (no corresponding output) to maintain alignment.

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
