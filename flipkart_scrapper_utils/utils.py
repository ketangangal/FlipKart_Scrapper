import yaml
from wordcloud import WordCloud, STOPWORDS
import plotly.graph_objs as go
import pandas as pd


def read_config(config_path="config.yaml"):
    with open(config_path) as config_file:
        content = yaml.safe_load(config_file)

    return content


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

    wc = WordCloud(stopwords=stopwords, max_words=200, max_font_size=100)

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
