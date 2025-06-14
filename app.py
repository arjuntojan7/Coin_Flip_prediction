import streamlit as st
from predictor import CoinFlipPredictor
import plotly.express as px

# Initialize session state
if 'predictor' not in st.session_state:
    st.session_state.predictor = CoinFlipPredictor()

st.set_page_config(page_title="Coin Flip Predictor", page_icon="🪙", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: Black;'>🪙 Coin Flip Predictor</h1>", 
    unsafe_allow_html=True
)
st.markdown("<p style='text-align: center;'>Predict the next coin flip (Heads or Tails) with style!</p>", unsafe_allow_html=True)

# Display your local GIF
# 
# st.image("C:/Mtech_Projects/Internship_projects/image/coin_anime.gif", width=200)


# Display flip history
st.subheader("Flip History")

history = st.session_state.predictor.get_history()

if history:
    badge_str = ""
    for flip in history:
        color = "#2196F3" if flip == "Heads" else "#FF5722"
        badge_str += f"<span style='background-color:{color}; color:white; padding:5px 10px; border-radius:12px; margin:2px; display:inline-block;'>{flip}</span>"
    st.markdown(badge_str, unsafe_allow_html=True)
else:
    st.info("No flips yet.")

# Plot chart of flip history
if history:
    df = {'Flip #': list(range(1, len(history)+1)), 'Outcome': history}
    fig = px.histogram(df, x='Outcome', color='Outcome', title='Flip Outcome Distribution',
                       color_discrete_map={'Heads':'#2196F3', 'Tails':'#FF5722'})
    st.plotly_chart(fig, use_container_width=True)

# Action buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎲 Predict Next Flip"):
        prediction = st.session_state.predictor.predict_next()
        st.success(f"Predicted: **{prediction}**")

with col2:
    if st.button("🪙 Flip the Coin"):
        actual = st.session_state.predictor.flip_coin()
        st.warning(f"Actual Flip Result: **{actual}**")

with col3:
    if st.button("🔄 Reset History"):
        st.session_state.predictor = CoinFlipPredictor()
        st.success("History cleared.")

st.markdown("<hr>", unsafe_allow_html=True)
# st.caption(" ❤️ ")
