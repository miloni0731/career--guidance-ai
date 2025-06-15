import streamlit as st
from pipeline.preference_extractor import PreferenceExtractor
from pipeline.domain_classifier import DomainClassifier
from pipeline.explanation_generator import ExplanationGenerator
from pipeline.fallback_handler import FallbackHandler

# Page config
st.set_page_config(
    page_title="AI Career Guidance Assistant",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS
st.markdown("""
<style>
    .main { padding: 2rem; }
    .stTextArea textarea { font-size: 1.1rem; }
    .response-box, .profile-section, .career-section, .questions-section {
        padding: 1rem; border-radius: 0.5rem; margin: 1rem 0;
    }
    .response-box { background-color: #f0f2f6; }
    .profile-section { background-color: #e6f3ff; }
    .career-section { background-color: #e6ffe6; }
    .questions-section { background-color: #fff2e6; }
</style>
""", unsafe_allow_html=True)

# Session state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
if "current_input" not in st.session_state:
    st.session_state.current_input = ""

# Load components
@st.cache_resource
def load_components():
    return {
        "preference_extractor": PreferenceExtractor(),
        "domain_classifier": DomainClassifier(),
        "explanation_generator": ExplanationGenerator(),
        "fallback_handler": FallbackHandler()
    }

components = load_components()

# Header
st.title("🎯 AI Career Guidance Assistant")
st.markdown("Describe what you enjoy, what you're good at, and what you dislike. We’ll suggest career paths based on that.")

# Input
st.subheader("Tell us about yourself")
user_input = st.text_area(
    "Describe your interests, skills, and preferences:",
    value=st.session_state.current_input,
    height=150,
    placeholder="Example: I love designing and solving puzzles, but I don't like reading too much theory."
)

# Main button
if st.button("Get Career Guidance", type="primary"):
    if user_input.strip():
        st.session_state.current_input = user_input.strip()

        # Step 1: Preference extraction
        preferences = components["preference_extractor"].extract_preferences(user_input)

        # Check if preferences are too empty, fallback
        if not any(preferences.values()):
            st.warning("Your input was unclear. Here are some questions to help refine your preferences.")
            questions = components["preference_extractor"].get_clarification_questions(user_input)
            for q in questions:
                st.write(f"- {q}")
        else:
            # Step 2: Classify to career path
            career_data = components["domain_classifier"].classify(preferences)

            # Step 3: Generate explanation
            explanation = components["explanation_generator"].generate(
                career_path=career_data["career_path"],
                preferences=preferences
            )

            # Step 4: Follow-up questions
            follow_ups = components["fallback_handler"].generate_follow_up(career_data["career_path"])

            # Package response
            result = {
                "career_path": career_data["career_path"],
                "confidence": career_data["confidence"],
                "explanation": explanation,
                "follow_up_questions": follow_ups
            }

            # Display profile
            st.markdown("### Extracted Profile")
            st.markdown('<div class="profile-section">', unsafe_allow_html=True)
            st.write("**Interests:**", ", ".join(preferences["interests"]))
            st.write("**Skills:**", ", ".join(preferences["skills"]))
            st.write("**Traits:**", ", ".join(preferences["traits"]))
            st.markdown('</div>', unsafe_allow_html=True)

            # Display recommendation
            st.markdown("### Career Recommendation")
            st.markdown('<div class="career-section">', unsafe_allow_html=True)
            st.write("**Recommended Career Path:**", result["career_path"])
            st.write("**Confidence:**", f"{result['confidence']:.2f}")
            st.markdown('</div>', unsafe_allow_html=True)

            # Explanation
            st.markdown("### Explanation")
            st.markdown('<div class="response-box">', unsafe_allow_html=True)
            st.write(result["explanation"])
            st.markdown('</div>', unsafe_allow_html=True)

            # Follow-up
            st.markdown("### Follow-up Questions")
            st.markdown('<div class="questions-section">', unsafe_allow_html=True)
            for q in result["follow_up_questions"]:
                st.write(f"- {q}")
            st.markdown('</div>', unsafe_allow_html=True)

            # Store in history
            st.session_state.conversation_history.append({
                "input": user_input,
                "profile": preferences,
                "recommendation": result
            })
    else:
        st.error("Please enter something before clicking the button.")

# History
if st.session_state.conversation_history:
    st.markdown("---")
    st.subheader("Previous Recommendations")
    for i, entry in enumerate(reversed(st.session_state.conversation_history)):
        with st.expander(f"Recommendation {len(st.session_state.conversation_history) - i}"):
            st.write("**Input:**", entry["input"])
            st.write("**Interests:**", ", ".join(entry["profile"]["interests"]))
            st.write("**Skills:**", ", ".join(entry["profile"]["skills"]))
            st.write("**Traits:**", ", ".join(entry["profile"]["traits"]))
            st.write("**Career Path:**", entry["recommendation"]["career_path"])
            st.write("**Confidence:**", f"{entry['recommendation']['confidence']:.2f}")
            st.write("**Explanation:**", entry["recommendation"]["explanation"])
            st.write("**Follow-up Questions:**")
            for q in entry["recommendation"]["follow_up_questions"]:
                st.write(f"- {q}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built with ❤️ by Miloni Panchal</p>
    <p>For: Brainwonders AI Engineering Internship</p>
</div>
""", unsafe_allow_html=True)
