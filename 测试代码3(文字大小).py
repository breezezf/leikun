# 2. Markdown 文本
# 导入 streamlit 后，就可以直接使用 st.markdown() 初始化，调用不同的方法，就可以往文档对象中填入内容

# st.title()#：文章大标题
# st.header()#：一级标题
# st.subheader()#：二级标题

# st.code()#：代码，同时可设置代码的语言，显示的时候会高亮

# st.caption()#：小字体文本
import streamlit as st
st.markdown('初始化')
st.title('大标题')
st.header('一级标题')
st.subheader("二级标题")
st.write('正常')
st.caption("小字体")


# 展示代码，有高亮效果
