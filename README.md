# PitchSmurf
## Bank of America Codeweek

## Pitch Smurf eases pitch book creation by automating the process and using AI to create Smart Pitch Books for companies.

### TLDR
Built with Python and Native WebStack
The Flask backend serves the main connection point where the user inputs the company name
Company is converted to a ticker symbol using Marketdata API
Ticker symbol is used to access financial and other information about the company
We provide distinctive price analysis values based on TTM data
All of this data is presented as a PowerPoint

### Stock Analysis
Long short-term memory Model
    Recurrent AI Neural Network (deep learning) with feedback connections so it can process entire sequences of data vs traditional 1 point.
Transformer Model
   The LSTM model is used to train the Transformer model (deep learning recurrent neural network). This model is designed to handle sequential data including layering so we can correlate sequential data of different types. 
Pandas (Python Library) Datareader
   Used to gather all historic data to train the model
   This approach allows us to keep historic P/E and P/B value while training the model
