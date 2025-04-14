import streamlit as st

def normalize_score(score, max_score):
    return (score / max_score) * 100

def calculate_final_grade(test1, test2, participation, weight_test1, weight_test2, weight_part):
    final = (test1 * weight_test1) + (test2 * weight_test2) + (participation * weight_part)
    return final

# Title of the app
st.title("📚 Final Grade Calculator")

# User input for the percentage weights (allow user to customize these)
st.write("Customize the weight percentages for each test and participation (must total 100%):")
weight_test1 = st.slider("Test 1 Weight (%)", 0, 100, 40)
weight_test2 = st.slider("Test 2 Weight (%)", 0, 100, 40)
weight_part = st.slider("Participation Weight (%)", 0, 100, 20)

# Ensure the weights total 100%
if weight_test1 + weight_test2 + weight_part != 100:
    st.warning("The total percentage must be 100%. Adjust the sliders to match 100%.")

# User input for the scores
st.write("Enter your scores and the max possible scores:")

t1_score = st.number_input("Test 1 Score", min_value=0.0)
t1_max = st.number_input("Test 1 Max Score", min_value=1.0)

# Test 2 is optional: Only ask if the score is given
t2_score = st.number_input("Test 2 Score (optional)", min_value=0.0)
t2_max = st.number_input("Test 2 Max Score (optional)", min_value=1.0)

# Participation score
part_score = st.number_input("Participation Score", min_value=0.0)
part_max = st.number_input("Participation Max Score", min_value=1.0)

if st.button("Calculate Final Grade"):
    if t1_score == 0 or t1_max == 0:
        st.error("Test 1 score and max score cannot be 0.")
    else:
        # Normalize scores
        t1 = normalize_score(t1_score, t1_max)
        
        if t2_score != 0 and t2_max != 0:
            t2 = normalize_score(t2_score, t2_max)
        else:
            t2 = 0  # If no second test score, assume it as 0
        
        part = normalize_score(part_score, part_max)

        # Calculate final grade
        final = calculate_final_grade(t1, t2, part, weight_test1 / 100, weight_test2 / 100, weight_part / 100)

        st.success(f" Your final grade is: {final:.2f} out of 100")
