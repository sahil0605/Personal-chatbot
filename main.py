import streamlit as st
from streamlit_chat import message
from bardapi import Bard
token = 'XwitUVn4DiaU1wsaoGDnDm3SxxmWd_eyVgk917rUKPZlHIfgyzyz4aWrcA5KyVVthV6wBg.'

def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']

    return response

#function to recieve queries
def get_text():
    input_text = st.text_input('My Bot:','Hey whasup',key='input')
    return input_text
#project title
st.title('Personal Tutoring Bot')
#data-testid ='stAppViewContainer'
# url = 'https://images.unsplash.com/photo-1618890334461-c33a04c4c916?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=387&q=80'
changes = '''
<style>
[data-testid ='stAppViewContainer']
{
background-image:url('https://images.unsplash.com/photo-1548850174-70a1cf2c5f09?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=387&q=80');
background-size:cover;
}
</style>
'''
st.markdown(changes ,unsafe_allow_html=True)

if 'generated' not in st.session_state:
    st.session_state['generated']=[]
if 'past' not in st.session_state:
    st.session_state['past']=[]

#accepting user input
user_input = get_text()
if user_input:
       print(user_input)
       output = generate_response(user_input)
       print(output)
       st.session_state.past.append(user_input)
       st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1,-1,-1):
     message(st.session_state['generated'][i],key=str(i))
     message(st.session_state['past'][i], key="user_"+str(i),is_user=True)

