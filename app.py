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

# --- Resources Section ---
st.markdown("---")
st.header("5. Resources for Further Learning 📚")

st.subheader("Practice Your Skills")
st.markdown("""
- **Interactive Quiz:** Test your knowledge of ratios, proportions, and percentages with this quiz. [Link to Practice Quiz](https://www.ixl.com/math/grade-6/ratios-and-proportions-quiz)
- **Practice Problems:** Work through a series of ratio word problems to become a proportional reasoning expert. [Link to Practice Problems](https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-ratios-prop-topic/6th-ratios-intro/e/ratio-word-problems)
""")

st.subheader("Video Tutorials & Articles")
st.markdown("""
- **Video: What are Ratios?** A quick and clear video explanation of the basics of ratios. [Link to Educational Video](https://www.youtube.com/watch?v=FjIuE94R1qg)
- **Article: The Definition of Ratio:** A detailed article explaining ratios and their different forms. [Link to Article](https://www.mathsisfun.com/definitions/ratio.html)
""")

st.subheader("Worldly Connections 🌐")
st.markdown("""
- **Currency Exchange Rates:** Learn how ratios are used to compare the value of different currencies around the world. [Link to Live Exchange Rates](https://www.xe.com/currencyconverter/)
- **Scale on Maps:** Discover how cartographers use scale ratios to represent large distances on a small map. [Link to Article on Map Scales](https://www.nationalgeographic.org/encyclopedia/map-scale/)
- **Art and Architecture:** Explore how the golden ratio, a special type of ratio, has been used in art and architecture for centuries to create aesthetically pleasing designs. [Link to Article on the Golden Ratio](https://www.britannica.com/science/golden-ratio)
""")
