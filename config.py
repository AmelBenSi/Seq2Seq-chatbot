# config.py
# Configuration file for shared paths and settings

# Define the main directory path for the dataset
MAIN_DIR_PATH = '/content/drive/MyDrive/CSCK507_EMA_GroupC_Final'

# Define filenames for each stage
RAW_DATA_FILE = 'raw_merged_data.csv'
CLEANED_DATA_FILE = 'cleaned_data.csv'
TOKENIZER_FILE = 'tokenizer.json'
TOKENIZED_DATA_FILE = 'tokenized_text.csv'
PADDED_SEQUENCES_FILE = 'padded_sequences.npz'
DECODER_IO_PAIRS = 'decoder_input_output_pairs.npz'
INPUT_OUTPUT_PAIRS = 'input_output_pairs.npz'
TRAIN_DATA = 'train_data.npz'
VAL_DATA = 'val_data.npz'
TEST_DATA = 'test_data.npz'
SEQ2SEQ_NA_MODEL = 'seq2seq_no_attention_model.h5'
SEQ2SEQ_WA_MODEL = 'seq2seq_with_attention_model.h5'