# Social Media Chat Analyzer

This project is a social media chat analyzer built with Python and Streamlit. The application provides various analyses on a chat log, including top statistics, activity timelines, activity maps, word cloud, most common words, emoji analysis, and sentiment analysis. The analysis can be done for a specific user or for the overall chat.

## Features

1. **Top Statistics**: Displays the total number of messages, total words, media shared, and links shared.

![image](https://github.com/amitkedia007/Whatsapp-chat-analyzer/assets/83700281/09838d81-79d1-48e9-b705-caedb885f797)

2. **Activity Timelines**: Shows the monthly and daily activity timelines.
![image](https://github.com/amitkedia007/Whatsapp-chat-analyzer/assets/83700281/c09ed3c6-b4aa-45be-9608-6ff44532a1a8)
![image](https://github.com/amitkedia007/Whatsapp-chat-analyzer/assets/83700281/2cff8753-8523-4d05-b20a-8fab31a3cf8e)

3. **Activity Maps**: Visualizes the most busy day and month.
![image](https://github.com/amitkedia007/Whatsapp-chat-analyzer/assets/83700281/4ca50b46-34f0-4aa3-b009-f547db35aff6)
![image](https://github.com/amitkedia007/Whatsapp-chat-analyzer/assets/83700281/1a0de54c-e896-4f58-9355-28fb2f932676)
![image](https://github.com/amitkedia007/Whatsapp-chat-analyzer/assets/83700281/e9b01318-09cd-48df-85b8-58c79440bfb4)

4. **Word Cloud**: Generates a word cloud for frequent words.
![image](https://github.com/amitkedia007/Whatsapp-chat-analyzer/assets/83700281/5a4a5f83-d5df-4c73-95eb-4279b5a59328)

5. **Most Common Words**: Lists the most common words used in the chat.
![image](https://github.com/amitkedia007/Whatsapp-chat-analyzer/assets/83700281/5b38d033-b0e0-4c02-806a-f29e0663870d)

6. **Emoji Analysis**: Analyzes the usage of emojis in the chat.
![image](https://github.com/amitkedia007/Whatsapp-chat-analyzer/assets/83700281/625211ac-66f7-487c-b7e5-c769e7518b34)

7. **Sentiment Analysis**: Performs sentiment analysis based on the text and emojis used in the messages.
![image](https://github.com/amitkedia007/Whatsapp-chat-analyzer/assets/83700281/3b138135-21ee-454d-812c-5928266f3e21)

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

![image](https://github.com/amitkedia007/Whatsapp-chat-analyzer/assets/83700281/0aa826e8-e54d-453d-aa23-aad7ca74701a)


4. Select a user from the dropdown menu in the sidebar.

5. Click the "Show Analysis" button in the sidebar to display the analysis.

## Project Structure

- `app.py`: The main Streamlit application.

- `preprocessor.py`: Contains the `preprocess` function for preprocessing the chat log.

- `helper.py`: Contains various helper functions for the analyses.

- `stopwords.txt`: A text file containing common stopwords to be excluded from the word cloud and most common words analysis.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
