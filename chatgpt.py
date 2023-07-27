import streamlit as st
# from pyPDF
from streamlit_extras.add_vertical_space import add_vertical_space

# sidebar content,配置边栏信息
with st.sidebar:
    st.title("LLM Chat APP")
    st.markdown('''
    ## 介绍
    利用langchain+ steamlit + openai 构建的智能聊天机器人
    ''')
    add_vertical_space(5)
    st.write('Made with ♥ by cheers')
def main():
    st.write('Welcome')
    st.header('chat with pdf')
    # upload pdf
    pdf = st.file_uploader('upload pdf here',type='pdf')

    text = '' # 设置字符串类型
    if pdf is not None:
        pdf_reader = PdfReader(pdf)

        text = ""
        for page in pdf_reader.pages:
            text += page.extra_text

        text_splitter = Recursion



if __name__ == '__main__':
    main()
