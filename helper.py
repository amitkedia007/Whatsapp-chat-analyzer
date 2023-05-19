from urlextract import URLExtract
from wordcloud import WordCloud
extract = URLExtract()

def fetch_stats(selected_user, df):

    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    
    # Fetch the number of messages
    num_messages = df.shape[0] 

    # Fetch the total number of words
    words = []
    for messages in df['message']:
        words.extend(messages.split())
    
    #Fetch number of media messages
    num_media_msg = df[df['message'] == '<Media omitted>\n'].shape[0]

    # Fetch number of links shared
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))
    
    return num_messages, len(words), num_media_msg, len(links)


# finding the busiest users in the group(Group Level)

def most_busy_user(df):
    # Filter out 'group_notification'
    df_filtered = df[df['user'] != 'group_notification']

    x = df_filtered['user'].value_counts().head()

    df_percent = round((df_filtered['user'].value_counts() / df_filtered.shape[0]) * 100, 2).reset_index().rename(columns = {'user': 'Name', 'count': 'Percent'})

    return x, df_percent

def create_wordcloud(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    
    wc = WordCloud(width= 500, height= 500, min_font_size= 10, background_color='white')
    df_wc =wc.generate(df['message'].str.cat(sep=" "))
    return df_wc