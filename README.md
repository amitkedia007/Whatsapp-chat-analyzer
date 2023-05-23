# Social Media Chat Analyzer

This project is a social media chat analyzer built with Python and Streamlit. The application provides various analyses on a chat log, including top statistics, activity timelines, activity maps, word cloud, most common words, emoji analysis, and sentiment analysis. The analysis can be done for a specific user or for the overall chat.

## Features

1. **Top Statistics**: Displays the total number of messages, total words, media shared, and links shared.

2. **Activity Timelines**: Shows the monthly and daily activity timelines.

3. **Activity Maps**: Visualizes the most busy day and month.

4. **Word Cloud**: Generates a word cloud for frequent words.

5. **Most Common Words**: Lists the most common words used in the chat.

6. **Emoji Analysis**: Analyzes the usage of emojis in the chat.

7. **Sentiment Analysis**: Performs sentiment analysis based on the text and emojis used in the messages.

## Installation

1. Clone the repository:
```
gh repo clone amitkedia007/Whatsapp-chat-analyzer
```

2. Navigate to the project directory:
```
cd Whatsapp-chat-analyzer
```

3. Install the required Python packages:
```
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```
streamlit run app.py
```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload a chat log file using the file uploader in the sidebar.

4. Select a user from the dropdown menu in the sidebar.

5. Click the "Show Analysis" button in the sidebar to display the analysis.

## Project Structure

- `app.py`: The main Streamlit application.

- `preprocessor.py`: Contains the `preprocess` function for preprocessing the chat log.

- `helper.py`: Contains various helper functions for the analyses.

- `stopwords.txt`: A text file containing common stopwords to be excluded from the word cloud and most common words analysis.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
