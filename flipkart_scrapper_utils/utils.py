import yaml
from wordcloud import WordCloud, STOPWORDS
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import pandas as pd
import plotly.io as pio


def read_config(config_path="config.yaml"):
    with open(config_path) as config_file:
        content = yaml.safe_load(config_file)

    return content


def create_wordcloud(data):
    df = pd.DataFrame(data)

    comment_words = ''
    stopwords = set(STOPWORDS)

    for val in df['Comment'].values:
        val = str(val)
        tokens = val.split()
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        comment_words += " ".join(tokens) + " "

    wordcloud = WordCloud(width=1000, height=800,
                          background_color='black',
                          stopwords=stopwords,
                          min_font_size=8).generate(comment_words)

    print(wordcloud)

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()


def plotly_wordcloud(data):
    word_list = []
    freq_list = []
    fontsize_list = []
    position_list = []
    orientation_list = []
    color_list = []

    x = []
    y = []

    new_freq_list = []

    df = pd.DataFrame(data)

    comment_words = ''
    stopwords = set(STOPWORDS)

    for val in df['Comment'].values:
        val = str(val)
        tokens = val.split()
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        comment_words += " ".join(tokens) + " "

    wc = WordCloud(stopwords=stopwords, max_words=200,max_font_size=100)

    wc.generate(comment_words)

    for (word, freq), fontsize, position, orientation, color in wc.layout_:
        word_list.append(word)
        freq_list.append(freq)
        fontsize_list.append(fontsize)
        position_list.append(position)
        orientation_list.append(orientation)
        color_list.append(color)

    for i in position_list:
        x.append(i[0])
        y.append(i[1])

    for i in freq_list:
        new_freq_list.append(i * 100)

    trace = go.Scatter(x=x, y=y, textfont=dict(size=new_freq_list, color=color_list), hoverinfo='text',
                       hovertext=['{0}{1}'.format(w, f) for w, f in zip(word_list, freq_list)], mode="text",
                       text=word_list)

    layout = go.Layout(xaxis=dict(showgrid=False, showticklabels=False, zeroline=False, automargin=True),
                       yaxis=dict(showgrid=False, showticklabels=False, zeroline=False, automargin=True))

    fig = go.Figure(data=[trace], layout=layout)

    return fig


if __name__ == "__main__":
    data = [{"Product_name": "iphone", "Name": "Flipkart Customer", "Rating": "5", "CommentHead": "Terrific",
             "Comment": "Wow superb camera phone Very smooth speed and no lag , iphone is the king always Its a beautiful product"},
            {"Product_name": "iphone", "Name": "Anurag Lad", "Rating": "5", "CommentHead": "Perfect product!",
             "Comment": "The brand is very trustworthy and i got genuine pice at a very low cost.I ordered the green one and trust me the colour was amazing.All the colours but specifically green and purple are nice for look.Thanks to flipkart❤️"},
            {"Product_name": "iphone", "Name": "Vishal Gandhi", "Rating": "5", "CommentHead": "Terrific purchase",
             "Comment": "Awesome phone … value for money.. Happy with battery life.. Awesome camera features… look at the images snapped using the phone… easy to use.. Just feared about getting scratch at back glass… but using cover helped it…"},
            {"Product_name": "iphone", "Name": "Ishu Kumar", "Rating": "5", "CommentHead": "Mind-blowing purchase",
             "Comment": "Guys ,this is just Beast at Every Aspect of Configurations, Full Pack with What You want, Like Best Camera , Best Display, Best Battery for whole Day Use, And Everyone know About Processing Speed👌.."},
            {"Product_name": "iphone", "Name": "Suddha Ram boro", "Rating": "5", "CommentHead": "Awesome",
             "Comment": "Thanks flipkart i trust you got my device perfectly loved it best phone in it's segment"},
            {"Product_name": "iphone", "Name": "Flipkart Customer", "Rating": "5", "CommentHead": "Awesome",
             "Comment": "Excellent product worth for every penny, writing this review after using 7 days, earlier was using iPhone 6Plus now on iPhone 12 😍, faster then anything this else.Excellent Picture quality.Just loved it.!!"},
            {"Product_name": "iphone", "Name": "ANAND S", "Rating": "5", "CommentHead": "Highly recommended",
             "Comment": "My 1st iPhone ever and I’m loving it. Great performance, awesome display, camera is outstanding which comes with heavily priced. But worth it. White color looks super cool. 🎉😊😍"},
            {"Product_name": "iphone", "Name": "Mohammadhusain Dedhrotiya ", "Rating": "5", "CommentHead": "Brilliant",
             "Comment": "Excellent product worth every penny right this review after using 7 days earlier was using phone iPhone 6s now on iPhone 12😍😍 faster than anything this else… excellent picture quality just love it iPhone12"},
            {"Product_name": "iphone", "Name": "Aman Yadav", "Rating": "5", "CommentHead": "Brilliant",
             "Comment": "It’s my first iPhone ever and I bought it with my earned money through part time jobs in college✌️I am a tech freak so you can trust my views -- A14 Bionic is the fastest, most efficient and reliable processor till date- The camera focuses so quickly that you can take DSLR quality photos.- The screen size 6.1 inches is the most comfortable screen size out there and the OLED retina XDR display is so crisp and everything feels real.- The stereo speakers are so clear even on high volume an..."},
            {"Product_name": "iphone", "Name": "Pranjal Dwivedi", "Rating": "5", "CommentHead": "Must buy!",
             "Comment": "Delightful phone, the phone is just a peice of art, sleek, eye catchy, super fast and got everything u need...best one available"},
            {"Product_name": "iphone", "Name": "No Name", "Rating": "No Rating", "CommentHead": "No Comment Heading",
             "Comment": "No comment"}]
    fig = plotly_wordcloud(data)
    pio.write_html(fig, file='test.html', auto_open=True)
    print(fig.to_json())
