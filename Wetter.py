import streamlit as st

import pandas as pd


# 假设的天气数据集

data = {

    '日期': pd.date_range(start='2021-01-01', periods=10, freq='D'),

    '天气': [

        '晴朗',

        '多云',

        '小雨',

        '晴朗',

        '小雨',

        '阴天',

        '雷阵雨',

        '多云',

        '晴朗',

        '小雨'

    ]

}


# 将数据转换为 DataFrame

df = pd.DataFrame(data)


# 设置 Streamlit 应用的标题

st.title('不同日期的天气展示')


# 创建一个滑动条，用户可以选择一个日期

selected_index = st.slider('选择日期', 0, len(df) - 1)


# 显示所选日期的天气

selected_date = df.iloc[selected_index]['日期']

selected_weather = df.iloc[selected_index]['天气']

st.write(f"日期：{selected_date.strftime('%Y-%m-%d')}，天气：{selected_weather}")