import streamlit as st

st.set_page_config(page_title="Ratio Explorer", page_icon="🔢")

st.title("🔢 Ratio Explorer: Recipes & Ratios")
st.markdown("""
This app helps you understand ratios by scaling a recipe. A ratio compares two quantities. 
Let's see what happens when you change the number of servings!
""")

st.header("The Original Recipe: Lemonade 🍋")
st.info("The original recipe for 1 serving uses **2 parts water** to **1 part lemon juice**.")

st.header("Scale Your Recipe")
servings = st.slider("How many servings do you want?", min_value=1, max_value=20, value=4, step=1)

water_parts = 2 * servings
lemon_juice_parts = 1 * servings

st.markdown("---")

st.header("Your Scaled Recipe")
st.write(f"For **{servings} servings**, you will need:")

st.metric("Water", value=f"{water_parts} parts")
st.metric("Lemon Juice", value=f"{lemon_juice_parts} parts")

st.markdown(f"""
The ratio of water to lemon juice is now **{water_parts}:{lemon_juice_parts}**. 
Even though the numbers are different, this ratio is still proportional to the original 2:1 ratio.
""")

st.markdown("---")
st.subheader("Why Ratios Matter")
st.write("""
Ratios are used everywhere! From mixing paint and building bridges to calculating fuel efficiency and scaling maps. They help us understand the relationship between different quantities.
""")
