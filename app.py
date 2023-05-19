import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

st.sidebar.title("Social Media Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    mydata =bytes_data.decode("utf-8")
    try:
        df = preprocessor.preprocess(mydata)

        st.dataframe(df)
    except Exception as e:
        st.write("An error occurred:",e)
    
    #fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove("group_notification")
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show Analysis with respect to", user_list)

if st.sidebar.button("Show Analysis"):
        
    num_messages, words, num_media_msg, links = helper.fetch_stats(selected_user,df)
        
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.header("Total Messages")
        st.title(num_messages)
    with col2:
        st.header("Total Words")
        st.title(words)
    with col3:
        st.header("Media Shared")
        st.title(num_media_msg)
    with col4:
        st.header("Links Shared")
        st.title(links)
        
# finding the busiest users in the group(Group Level)

    if selected_user == 'Overall':
        st.title('Most Busy Users')

        x, new_df = helper.most_busy_user(df)

        fig, ax = plt.subplots()

        col1, col2 = st.columns(2)

        with col1:
            colors = cm.viridis(np.linspace(0, 1, len(x.index)))  # Create a colormap
            ax.bar(x.index, x.values, color=colors)  # Use the colormap for the bars
            plt.title('User Activity')  # Add a title
            plt.xlabel('User')  # Add x-axis label
            plt.ylabel('Activity Count')  # Add y-axis label
            plt.xticks(rotation="vertical")
            plt.grid(True)  # Add grid lines
            st.pyplot(fig)

        with col2:
            st.write('## User Activity Data')  # Add a title to the DataFrame
            st.dataframe(new_df.style.highlight_max(color='lightgreen'))  # Highlight max values

    # WordCloud
    st.title("Word Cloud for Frequent Words")
    df_wc = helper.create_wordcloud(selected_user, df)
    fig, ax= plt.subplots()
    ax.imshow(df_wc)
    st.pyplot(fig)

    # Most Common words
    most_common_df = helper.most_common_words(selected_user, df)

    fig, ax = plt.subplots()

    ax.barh(most_common_df["Words"], most_common_df["Frequency"])
    plt.xticks(rotation = 'vertical')
    st.title("Most Common Words")
    st.pyplot(fig)  

    