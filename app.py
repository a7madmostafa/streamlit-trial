import streamlit as st

st.title('Hello World')
st.header("this is the header")
st.markdown("Hi is the markdown")
st.subheader("Hi is the subheader")
st.caption("this is the caption")
st.code(''' if x == 5:
    print('Hello')''')
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
st.markdown("<h1 style='text-align: center; color: blue;'>Colorful and centered</h1>", unsafe_allow_html=True)


st.image("https://kidcitystores.com/cdn/shop/files/colle2.jpg", width= 200, caption="hi")


import pandas as pd

df = pd.DataFrame({'k':[1,2,3,4,5], 'v':[10,20,30,40,50]})
st.dataframe(df)
st.table(df)




if st.checkbox('show data frame'):
    st.dataframe(df)

st.button('Click')

st.radio('Pick your gender',['Male','Female'])

gender = st.selectbox('Pick your gender',['Male','Female'])


if gender == 'Male':
    st.write('He is male')
else:
    st.write('She is female')


st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])


st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])

st.slider('Pick a number', 0,50, step=10)


num1 = st.number_input('Pick a number1', 0,10)
num2 = st.number_input('Pick a number2', 0,10)
sum = num1 + num2
st.write("Sum", sum)

st.text_input('Email address')


date = st.date_input('Travelling date')
# total_price = df[df.order_date == date]['total_price'][0]
# st.write('Total Sales', total_price)

st.time_input('School time')

st.text_area('Description')

st.file_uploader('Upload a photo')

st.color_picker('Choose your favorite color')


st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))


st.sidebar.title("This is the sidebar")
st.sidebar.header("This is the header")
st.sidebar.button("Click2")
st.sidebar.checkbox("Yes2")
st.sidebar.radio("Pick your gender2: ", ['male', 'female'])


# import matplotlib.pyplot as plt
# import numpy as np

# rand=np.random.normal(1, 2, size=20)
# fig, ax = plt.subplots()
# ax.hist(rand, bins=15)

# st.markdown("<h1 style='text-align: center; color: red;'>Matplotlib Figure</h1>", unsafe_allow_html=True)

# st.pyplot(fig)

# import plotly.express as px

# rand=np.random.normal(1, 2, size=20)
# fig = px.histogram(rand, nbins=15)
# st.write(' # Plotly Histogram')
# st.plotly_chart(fig)

# df = pd.DataFrame({'k':[1,2,3,4,5], 'v':[10,20,30,40,50]})
# st.write(' # Plotly Bar Chart')
# fig2 =px.bar(df, x='k', y='v', width=300)
# st.plotly_chart(fig2)

# st.write(' # Plotly Line Chart')
# st.plotly_chart(px.line(df, x='k', y='v'))
