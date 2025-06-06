import random
import streamlit as st

EASY_LEVEL = 50
MEDIUM_LEVEL = 100
HARD_LEVEL = 200

def game_logic(range: int):
    user = st.number_input("Enter a number: ", value=1.0, step=.05, format="%f")
    submit = st.button("Submit")
    
    if "attempts" and "score" not in st.session_state:
        st.session_state['attempts'] = 0
        st.session_state['score'] = 0
        st.text(f"Initail Attempts: {st.session_state['attempts']}")
        st.text(f"Initial Score: {st.session_state['score']}")
            
    if submit:
        comp = random.randint(1,range)
        st.text(f"Computer Choose {comp}")
        
        if user > comp:
            st.success("You guessed higher!")
            st.session_state['attempts'] +=1 

        elif user < comp:
            st.success("You guessed lower!")
            st.session_state['attempts'] +=1 

        elif user == comp:
            st.success("You guessed it right!")
            st.session_state['score'] +=1 
            st.write(f":blue-background[Score]: :blue[{st.session_state['score']}]")
            st.write(f":blue-background[Total Attempts]: :blue[{st.session_state['attempts']}]")
        else:
            st.success("Invalid Input")

def main():
    st.header("🔢 Number Guessing Game")
    options = ["Easy (1-50 numbers)", "Medium (1-100 numbers)", "Hard (1-200 numbers)"]
    difficulty = st.selectbox("Difficulty Level", options)
    
    if difficulty == options[0]:
        game_logic(EASY_LEVEL)
    elif difficulty == options[1]:
        game_logic(MEDIUM_LEVEL)
    elif difficulty == options[2]: 
        game_logic(HARD_LEVEL)
    else:
        print("No Option Available")

    
if __name__ == '__main__':
    main()