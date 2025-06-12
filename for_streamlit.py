import streamlit as st
#import matplotlib.pyplot as plt
import pandas as pd
from project import wages
from project import df
from project import fig_0, fig_1, fig_2

# Настройка страницы
st.set_page_config(
    page_title="Анализ зарплат в России",
    page_icon="📊",
    layout="wide"
)

# Приветствие
st.markdown(
    """
    <style>
    .big-font {
        font-size:24px !important;
        color: #1f77b4;
    }
    .formula {
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #1f77b4;
        font-family: monospace;
        margin: 10px 0;
    }
    .section-header {
        font-size:20px !important;
        color: #1f77b4;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="big-font">Добро пожаловать в приложение для анализа зарплат!</p>', 
            unsafe_allow_html=True)
st.title("Анализ зарплат в России")
st.subheader("2000 - 2024 годы")
st.caption("В области добычи полезных ископаемых, образования и строительства")
st.divider()

# Проверка данных
st.write("Данные по номинальной зарплате за каждый год")
st.dataframe(wages.head())

# Добавляем разделитель перед новым блоком
st.divider()
st.markdown(
    """
    <style>
    .big-font {
        font-size:24px !important;
        color: #1f77b4;
    }
    .formula {
        background-color: var(--secondary-background-color);
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #1f77b4;
        font-family: monospace;
        margin: 10px 0;
        color: var(--text-color);
    }
    .section-header {
        font-size:20px !important;
        color: #1f77b4;
        margin-top: 20px;
    }
    .highlight {
        background-color: rgba(31, 119, 180, 0.2);
        padding: 2px 5px;
        border-radius: 3px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# А в секции с формулой измените на это:
st.markdown("""
### Методология расчета реальных зарплат

Для перевода номинальных зарплат в реальные используется <span class="highlight">Индекс Потребительских Цен (CPI)</span>:

<div class="formula">
Реальная зарплата = (Номинальная зарплата / CPI) × 100
</div>

Где:
- <b>Номинальная зарплата</b> - зарплата в текущих ценах
- <b>CPI</b> (Consumer Price Index) - индекс потребительских цен, где базовый год = 100 %
- <b>Реальная зарплата</b> - зарплата в ценах базового года

В нашем анализе мы использовали следующие параметры:
- Базовый год: <span class="highlight">2000</span>
- Источник данных: <span class="highlight">Росстат</span>

""", unsafe_allow_html=True)

# Кнопка для отображения преобразованных данных
if st.button("Посмотреть преобразованные данные"):
    st.markdown('<p class="section-header">Преобразованные данные с учетом инфляции</p>', 
                unsafe_allow_html=True)
    st.dataframe(df)



# Создаем вкладки для графиков
tab1, tab2, tab3 = st.tabs(["Номинальные зарплаты", "Реальные зарплаты", "Сравнение отраслей"])

with tab1:

        st.markdown('<p class="section-header">График номинальных зарплат по отраслям</p>', 
                    unsafe_allow_html=True)
        
        if fig_0 is not None:
            fig_0.set_size_inches(10, 5)
            st.pyplot(fig_0, use_container_width=True)    
        else:
            st.warning("График номинальных зарплат не доступен")

with tab2:
        st.markdown('<p class="section-header">График реальных зарплат с учетом инфляции</p>', 
                    unsafe_allow_html=True)
        
        if fig_1 is not None:
            fig_1.set_size_inches(10, 5)
            st.pyplot(fig_1, use_container_width=True)
            

        else:
            st.warning("График реальных зарплат не доступен")

with tab3:
        st.markdown('<p class="section-header">Сравнение роста зарплат по отраслям</p>', 
                    unsafe_allow_html=True)
        
        if fig_2 is not None:
            fig_2.set_size_inches(10, 5)
            st.pyplot(fig_2, use_container_width=True)
            

        else:
            st.warning("График сравнения не доступен")

