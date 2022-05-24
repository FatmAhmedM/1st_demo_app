import streamlit as st
import joblib


def main():
    html_tamplete = """
    <div style = "background-color:Lightblue; padding:5px">
    <h1 style="color:Black";text-align:center> Predict houses' prices (1st-demo)  </h1>
    </div>
    """
    st.markdown(html_tamplete,unsafe_allow_html =True)
    
    model = joblib.load("demo_RegModel")
    p1 = st.number_input('What is the house area ?')
    p2 = st.slider(' How many bedrooms ?',1,20)
    p3 = st.slider('Age of the house ?',0,50)
    if st.button('Predict'):
        pred = model.predict([[p1,p2,p3]])
        st.success(f'The price is : {pred[0]} $')
    
if __name__ == '__main__' :
    main()
    
    
