from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt
import streamlit as st 

st.set_option('deprecation.showPyplotGlobalUse',False)

def cloud(image,text, max_words,max_font_size):
    stopwords = set(STOPWORDS)
    stopwords.update(["said", "one", "go"])

    wc = WordCloud(background_color="white", colormap="hot", max_words=max_words, mask=image,
           stopwords=stopwords, max_font_size=max_font_size)
    
    wc.generate(text)

    fig = plt.figure()
    fig.set_figwidth(14) # set width
    fig.set_figheight(18) # set height
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    st.pyplot()

    


def main(): 
    st.write("# Hactiv8 Python DS - WorldCloud")
    st.write("IketutG")
    if st.button("Please Click Me"):
        max_words = st.sidebar.slider("Max Word",1000,3000,2000)
        max_font_size = st.sidebar.slider("Max Font Size",50,350,60)
        image = np.array(Image.open('data/alice_mask.png'))
        text = open('data/alice_novel.txt', 'r').read()
        st.write(cloud(image,text, max_words,max_font_size))

if __name__ == "__main__":
    main()