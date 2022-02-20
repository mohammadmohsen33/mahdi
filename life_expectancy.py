# importing libraries
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

# Function for making spaces
def space(n,element): # n: number of lines
    for i in range(n):
        element.write("")

# html command for a red line
red_line="""<hr style="height:4px;border:none;color:#DC143C;background-color:#DC143C;"/>"""

# html commnad for a grey line
grey_line="""<hr style="height:1px;border:none;no shade;"/>"""

# Setting page layout
st.set_page_config(layout='wide')

# Loading Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mam127/Life-Expectancy-325/main/Life%20Expectancy%20Data.csv")

# Manipulating Dataset
df.dropna(subset=['Population','Income composition of resources'], inplace=True)
df = df.sort_values('Year')
df = df[(df['Income composition of resources'] !=0) & (df["Country"]!= "Israel")]

# MSBA Logo
html_string = '''<!DOCTYPE html>
<html>
<body>
 <a href="https://www.aub.edu.lb/osb/MSBA/Pages/default.aspx">
  <img src="https://www.aub.edu.lb/osb/research/Darwazah/PublishingImages/OSB%20Stamp%20color-MSBA.png" width=300" height="80" />
 </a>
</body>
</html>'''
st.sidebar.markdown(html_string, unsafe_allow_html=True)
space(4,st.sidebar)

# Section selection
add_selectbox = st.sidebar.selectbox("Choose Section:", ("Overview", "Visualizations", "Meta Data"))
space(16,st.sidebar)

# My name and professor's name
st.sidebar.subheader("Done by [Mahdi Mohammad](https://www.linkedin.com/in/mahdi-mohammad-7b5034201/?originalSubdomain=lb)")
st.sidebar.subheader("Professor [Fouad Zablith](https://www.aub.edu.lb/pages/profile.aspx?memberId=fz13)")


if add_selectbox=="Overview":
    # Title
    col1,col2,col3 = st.columns([1,1,1])
    col2.title("Overview")
    st.write(red_line, unsafe_allow_html=True)
    
    # Content
    st.header("I. Content")
    st.write('''
    The Global Health Observatory (GHO) data repository under World Health Organization (WHO) keeps track of the health status as well as many other 
    related factors for all countries The datasets are made available to public for the purpose of health data analysis. The dataset related to life 
    expectancy, health factors for 193 countries has been collected from the same WHO data repository website and its corresponding economic data was 
    collected from United Nation website. Among all categories of health-related factors only those critical factors were chosen which are more representative. 
    It has been observed that in the past 15 years, there has been a huge development in health sector resulting in improvement of human mortality rates especially 
    in the developing nations in comparison to the past 30 years. Therefore, in this project we have considered data from year 2000-2015 for 193 countries for 
    further analysis. The individual data files have been merged together into a single dataset. On initial visual inspection of the data showed some missing 
    values. As the datasets were from WHO, we found no evident errors. Missing data was handled in R software by using Missmap command. The result indicated 
    that most of the missing data was for population, Hepatitis B and GDP. The missing data were from less known countries like Vanuatu, Tonga, Togo,Cabo Verde 
    etc. Finding all data for these countries was difficult and hence, it was decided that we exclude these countries from the final model dataset. The final 
    merged file(final dataset) consists of 22 Columns and 2938 rows which meant 20 predicting variables.''')
    st.write(grey_line, unsafe_allow_html=True)

    # Inspiration
    st.header("II. Inspiration")
    st.write('''
    The dataset aims to answer the following key questions:
    * What are the predicting variables that actually affect the life expectancy?
    * Should a country having a low life expectancy value increase its healthcare expenditure in order to improve its average lifespan?
    * How do infant and adult mortality rates affect life expectancy?
    * Does life expectancy have a positive or a negative correlation with eating habits, lifestyle, exercise, smoking, drinking alcohol etc.?
    * What is the impact of schooling on the lifespan of humans?
    * Does life expectancy have a positive or a negative relationship with drinking alcohol?
    * Do densely populated countries tend to have lower life expectancy?
    * What is the impact of immunization coverage on life expectancy?
    * How does life expectancy differ between Arab Countries?''')
    st.write(grey_line, unsafe_allow_html=True)

    # Acknowledgements
    st.header("III. Acknowledgements")
    st.write('''The data was collected from WHO and United Nations website with the help of Deeksha Russell and Duan Wang. The data was retrieved from Kaggle.''')

if add_selectbox=="Visualizations":
    # Title
    col1,col2,col3 = st.columns([1,1,1])
    col2.title("Visualizations")
    st.write(red_line, unsafe_allow_html=True)
    
    # Correlation Plot
    st.header("I. Correlation Plot")
    col1,col2,col3=st.columns([6,1,3])
    df1 = df[["Life expectancy ", "Adult Mortality", "infant deaths", "Alcohol", " BMI ","under-five deaths ", "Population", "Income composition of resources",
    "Schooling"]]
    cr = df1.corr(method='pearson')
    fig = go.Figure(go.Heatmap(x=cr.columns, y=cr.columns, z=cr.values.tolist(), colorscale='OrRd', zmin=-1, zmax=1))
    col1.plotly_chart(fig, use_container_width=True, sharing="streamlit")
    space(8,col3)
    html='''<center><p style="border:3px; border-style:solid; border-color:#DC143C; padding: 2em;
    "> <b>This plot aims to discover the linear realationship between the quantitative variables in the dataset.</p>'''
    col3.write(html,unsafe_allow_html=True)
    st.write(grey_line, unsafe_allow_html=True)
    
    # Map Plot
    st.header("II. Map Plot")
    col1,col2,col3=st.columns([6,1,3])
    fig = px.choropleth(df, locations="Country",locationmode="country names", color="Life expectancy ", hover_name="Country", animation_frame="Year",
    color_continuous_scale=px.colors.sequential.OrRd, projection="natural earth", title="Examining Life Exprectancy in the World Over Time")
    col1.plotly_chart(fig, use_container_width=True, sharing="streamlit")
    space(8,col3)
    html='''<center><p style="border:3px; border-style:solid; border-color:#DC143C; padding: 2em;
    "><b>The plot shows a high life expectancy in Canada, Australia, and Europe Countries over time. However, a low life expectancy is observed in the African Countries over time.</p>'''
    col3.write(html,unsafe_allow_html=True)
    st.write(grey_line, unsafe_allow_html=True)

    # 3D Plot
    st.header("III. 3D Plot")
    col1,col2,col3=st.columns([6,1,3])
    fig = go.Figure(data=go.Scatter3d(x=df['Year'], y=df["Income composition of resources"], z=df['Schooling'], text=df['Country'], mode='markers',
    marker=dict(color = df['Life expectancy '], colorscale = 'OrRd', colorbar_title = 'Life<br>Expectancy', line_color='rgb(140, 140, 170)')))
    ## Adding Title to the Axes + General Title
    fig.update_layout(scene={'xaxis':{'title':'Year'},
    'yaxis':{'title':'Income<br>Composition'},
    'zaxis':{'title':'Schooling'}
    }, title='Examining Income, Schooling & Life Expectancy Over Time')
    col1.plotly_chart(fig, use_container_width=True, sharing="streamlit")
    space(8,col3)
    html='''<center><p style="border:3px; border-style:solid; border-color:#DC143C; padding: 2em;
    "><b>The plot shows that as the income composition of resources and the number of schooling years increase, the life expectancy increases.</p>'''
    col3.write(html,unsafe_allow_html=True)
    st.write(grey_line, unsafe_allow_html=True)

    # Bubble Plot
    st.header("IV. Bubble Plot")
    option = st.selectbox(
     'Select the variable on the x-axis',
     ('Adult Mortality', 'infant deaths','Alcohol','percentage expenditure','Hepatitis B', 'Measles ', ' BMI ', 'under-five deaths ',
     'Polio', 'Total expenditure', 'Diphtheria ', " HIV/AIDS", 'GDP', ' thinness  1-19 years', ' thinness 5-9 years', 'Income composition of resources',
     'Schooling'))
    space(2,st)
    col1,col2,col3=st.columns([6,1,3])
    fig = px.scatter(df, x= option, y="Life expectancy ",size="Population", hover_name="Country", size_max=100, color="Status",
    animation_frame="Year", animation_group="Country",
    labels={'Population':"Population", "Income composition of resources":"Income Composition of Resources", "Life expectancy ":"Life Expectancy"},
    title="Examining "+ str(option) +", Population & Life Exprectancy Over Time")
    col1.plotly_chart(fig, use_container_width=True, sharing="streamlit")
    space(8,col3)
    html='''<center><p style="border:3px; border-style:solid; border-color:#DC143C; padding: 2em;
    "><b>The plot helps examining the relation between life expectancy and different variables.</p>'''
    col3.write(html,unsafe_allow_html=True)
    st.write(grey_line, unsafe_allow_html=True)

    # Bar Plot
    st.header("V. Bar Plot")
    year = st.slider('Select a year', 2000, 2015)
    space(1,st)
    arabs = ["Lebanon","Algeria","Bahrain","Comoros","Djibouti","Egypt","Iraq","Jordan","Kuwait","Libya","Mauritania",
    "Morocco","Oman","Qatar","Saudi Arabia","Somalia","Sudan","Syrian Arab Republic","Tunisia","United Arab Emirates","Yemen"]
    arab_countries = st.multiselect('Choose the Arab Countries you want to compare',arabs,arabs)
    space(2,st)
    df = df[df["Year"]==year]
    df2 = pd.DataFrame()
    for c in arab_countries:
        df2 = df2.append(df.loc[df["Country"]== c,:])
    fig = px.bar(df2, x="Country", y='Life expectancy ', color='Income composition of resources', color_continuous_scale='inferno',
    title="Examining Life Expectancy & Income in Some Arab Countries in "+str(year))
    ## Annotating the Plot   
    x_high= df2["Country"][df2['Life expectancy '] == df2['Life expectancy '].max()].to_list()[0]
    x_low= df2["Country"][df2['Life expectancy '] == df2['Life expectancy '].min()].to_list()[0]
    highestAnnotation = {'x':x_high, 'y': df2['Life expectancy '].max(), 'showarrow': True,'arrowhead': 3, 'text': "<b> Highest Life Expectancy </b>", 
    'font' : {'size': 10, 'color': 'black'},'ax':1.5}
    lowestAnnotation = {'x':x_low, 'y': df2['Life expectancy '].min(), 'showarrow': True,'arrowhead': 3, 'text': "<b> Lowest <br> Life <br> Expectancy </b>",
    'font' : {'size': 10, 'color': 'black'}, 'ax':1.5}
    fig.update_layout({'annotations': [highestAnnotation, lowestAnnotation], 'yaxis': {'title':{'text': 'Life Expectancy'}}})
    col1,col2,col3=st.columns([6,1,3])
    col1.plotly_chart(fig, use_container_width=True, sharing="streamlit")
    space(6,col3)
    html='''<center><p style="border:3px; border-style:solid; border-color:#DC143C; padding: 2em;
    "><b>The plot helps comparing life expectancy and income composition of resources in some Arab Countries in differnet years. Note that data about some Arab Countries is missing in certain years.</p>'''
    col3.write(html,unsafe_allow_html=True)

if add_selectbox=="Meta Data":
    # Title
    col1,col2,col3=st.columns([1,1,1])
    st.write(red_line, unsafe_allow_html=True)
    col2.title("Meta Data")

    # Table of data
    st.header("Table of Data")    
    df = pd.read_csv("https://raw.githubusercontent.com/mam127/Life-Expectancy-325/main/Life%20Expectancy%20Data.csv")
    st.write(df)
    st.write(grey_line, unsafe_allow_html=True)

    # Description of Variables
    st.header("Description of Variables")
    col1,col2,col3,col4= st.columns([1,1,1,1])
    if col1.button("Country"):
        col1.write("Name of the countries")
    if col2.button("Year"):
        col2.write("Year of the reported data (from 2000 to 2015)")
    if col3.button("Status"):
        col3.write("Developed or Developing status")
    if col4.button("Life expectancy"):
        col4.write("Life expectancy in years")
    if col1.button("Adult Mortality"):
        col1.write("Adult Mortality Rates of both sexes (probability of dying between 15 and 60 years per 1000 population)")
    if col2.button("Infant Deaths"):
        col2.write("Number of Infant Deaths per 1000 population")
    if col3.button("Alcohol"):
        col3.write("Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)")
    if col4.button("Percentage Expenditure"):
        col4.write("Expenditure on health as a percentage of Gross Domestic Product per capita(%)")
    if col1.button("Hepatitis B"):
        col1.write("Hepatitis B (HepB) immunization coverage among 1-year-olds (%)")
    if col2.button("Measles"):
        col2.write("Measles - number of reported cases per 1000 population")
    if col3.button("BMI"):
        col3.write("Average Body Mass Index of entire population")
    if col4.button("Under-Five Deaths"):
        col4.write("Number of under-five deaths per 1000 population")
    if col1.button("Polio"):
        col1.write('''Polio (Pol3) immunization coverage among 1-year-olds (%)''')
    if col2.button("Total expenditure"):
        col2.write("General government expenditure on health as a percentage of total government expenditure (%)")
    if col3.button("Diphtheria"):
        col3.write("Diphtheria tetanus toxoid and pertussis (DTP3) immunization coverage among 1-year-olds (%)")
    if col4.button("HIV/AIDS"):
        col4.write("Deaths per 1 000 live births HIV/AIDS (0-4 years)")
    if col1.button("GDP"):
        col1.write("Gross Domestic Product per capita (in USD)")
    if col2.button("Population"):
        col2.write("Population of the country")
    if col3.button("Thinness 1-19 Years"):
        col3.write("Prevalence of thinness among children and adolescents for Age 10 to 19 (%)")
    if col4.button("Thinness 5-9 Years"):
        col4.write("Prevalence of thinness among children for Age 5 to 9 (%)")
    if col1.button("Income Comp. of Resources"):
        col1.write("Human Development Index in terms of income composition of resources (index ranging from 0 to 1)")
    if col2.button("Schooling"):
        col2.write("Number of years of schooling")
    st.write(grey_line, unsafe_allow_html=True)
    col1,col2,col3=st.columns([1,3,2])
    html_string = '''<!DOCTYPE html>
<html>
<body>
 <a href="https://www.who.int/">
  <img src="https://logos-download.com/wp-content/uploads/2016/12/World_Health_Organization_logo_logotype.png" width=270" height="100" />
 </a>
</body>
</html>'''
    space(2,col2)
    col2.markdown(html_string, unsafe_allow_html=True)
    html_string = '''<!DOCTYPE html>
<html>
<body>
 <a href="https://www.kaggle.com/kumarajarshi/life-expectancy-who">
  <img src="https://talenthometraining.in/wp-content/uploads/2019/02/Icons-DBMS-01-1024x1024.png" width=120" height="150" />
 </a>
</body>
</html>'''
    col3.markdown(html_string, unsafe_allow_html=True)
    
