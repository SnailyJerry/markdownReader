import streamlit as st
import os

# 设置页面为宽屏模式
st.set_page_config(layout="wide")

# 设置页面标题
st.title("🐌 蜗牛格式阅读器")

# 文件上传组件
uploaded_files = st.file_uploader(
    "请在这里上传您的 Markdown (.md) 文件",
    type="md",
    accept_multiple_files=True
)

if uploaded_files:
    # 获取上传文件的文件名列表
    file_names = [file.name for file in uploaded_files]
    
    # 创建一个字典来存储文件名和文件内容的映射
    file_map = {file.name: file for file in uploaded_files}

    # 文件选择下拉框
    selected_file_name = st.selectbox("请选择要阅读的文件", file_names)

    if selected_file_name:
        # 获取选定的文件对象
        selected_file = file_map[selected_file_name]
        
        # 读取并解码文件内容
        markdown_content = selected_file.getvalue().decode("utf-8")
        
        # 使用 st.markdown 展示内容
        st.markdown("---")
        st.header(f"正在阅读: {selected_file_name}")
        st.markdown(markdown_content, unsafe_allow_html=True)

else:
    st.info("上传文件后，您可以在此预览 Markdown 内容。")
