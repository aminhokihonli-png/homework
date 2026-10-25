import streamlit as st
import random

st.set_page_config(page_title="My webapp", page_icon="https://i.pinimg.com/736x/aa/8c/23/aa8c23121ad14dfdacc93dbf2e925a5c.jpg", layout="wide")

st.title("Nice to meet you on my webapp")

tab1, tab2, tab3, tab4 = st.tabs(["About me", "My tool", "Useful links", "Game"])

with tab1:
    st.header("Meeting the author")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://i.pinimg.com/736x/08/ed/f0/08edf05148b0129ff7ea7e8a431d5f6d.jpg", width=400)
    with col2:
        st.subheader("Hello!, I am a future Python Developer!")
        st.write("I study at small Acadamy IT Step. I make cool webapps and learn streamlit.")

        with st.container():
            st.info("Contacts for conecting")
            st.markdown("- GitHub: [My profile](https://github.com)")
            st.markdown("- E-Mail: ariana@itstep.org")

with tab2:
    st.info("In developing")

with tab3:
    st.header("Useful learning resources")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.info("School📚")
        st.markdown("- Osvita⏳: https://osvita.diia.gov.ua/")
        st.markdown("- Classroom💡: https://classroom.google.com/h/st")
    with col2:
        st.info("Games🎮")
        st.markdown("- Minecraft💻: https://www.minecraft.net/ru-ru")
        st.markdown("- Roblox🖥️: https://about.roblox.com/what-is-roblox")

with tab4:
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False

    st.subheader("Гра🎮: Вгадай число від 1 до 100")
    
    user_guess = st.number_input("Твій варіант:", min_value=1, max_value=100, step=1, key="guess_input")
    
    if st.button("Перевірити"):
        st.session_state.attempts += 1
        
        if user_guess < st.session_state.secret_number:
            st.info("Загадане число більше!📉")
        elif user_guess > st.session_state.secret_number:
            st.info("Загадане число менше!📈")
        else:
            st.success(f"Перемога!🎉 Ти вгадав число {st.session_state.secret_number} за {st.session_state.attempts} спроб!")
            st.session_state.game_over = True
            
    st.write(f"Кількість спроб: {st.session_state.attempts}")

    if st.button("Зіграти знову"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()