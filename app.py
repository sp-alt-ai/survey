import streamlit as st
from datetime import datetime
import pandas as pd
import json

# Page configuration
st.set_page_config(
    page_title="Academic Pressure Survey - Grade 10",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .survey-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 24px;
        padding: 40px;
        margin: 20px 0;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    }
    
    .header-section {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 24px;
        padding: 50px 40px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        border-top: 5px solid;
        border-image: linear-gradient(90deg, #f093fb 0%, #f5576c 50%, #4facfe 100%) 1;
    }
    
    h1 {
        color: #2d3748 !important;
        font-weight: 700 !important;
        font-size: 2.5rem !important;
        margin-bottom: 15px !important;
    }
    
    .subtitle {
        color: #718096;
        font-size: 1.1rem;
        max-width: 600px;
        margin: 0 auto;
    }
    
    .privacy-box {
        background: #edf2f7;
        border-left: 4px solid #667eea;
        padding: 15px 20px;
        margin-top: 20px;
        border-radius: 8px;
        text-align: left;
        font-size: 0.9rem;
        color: #4a5568;
    }
    
    .section-box {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 24px;
        padding: 40px;
        margin-bottom: 25px;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.2);
    }
    
    .section-title {
        color: #2d3748;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .section-icon {
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.2rem;
    }
    
    .section-desc {
        color: #718096;
        margin-bottom: 30px;
        margin-left: 52px;
        font-size: 0.95rem;
    }
    
    .question-box {
        margin-bottom: 30px;
        padding-bottom: 30px;
        border-bottom: 1px solid #e2e8f0;
    }
    
    .question-box:last-child {
        border-bottom: none;
        margin-bottom: 0;
        padding-bottom: 0;
    }
    
    .question-text {
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 15px;
        font-size: 1.05rem;
    }
    
    .required {
        color: #e53e3e;
        margin-left: 4px;
    }
    
    .stRadio > label, .stCheckbox > label {
        font-weight: 500 !important;
        color: #4a5568 !important;
    }
    
    .stRadio > div, .stCheckbox > div {
        background: #f7fafc;
        border-radius: 12px;
        padding: 10px;
        margin-bottom: 8px;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    
    .stRadio > div:hover, .stCheckbox > div:hover {
        border-color: #cbd5e0;
        transform: translateX(5px);
    }
    
    .stTextInput > div > div > input, .stDateInput > div > div > input {
        background: #f7fafc !important;
        border: 2px solid #e2e8f0 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        font-size: 1rem !important;
    }
    
    .stTextInput > div > div > input:focus, .stDateInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    div[data-testid="stFormSubmitButton"] > button {
        width: 100%;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 16px !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        margin-top: 20px !important;
    }
    
    div[data-testid="stFormSubmitButton"] > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4) !important;
    }
    
    .success-message {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 24px;
        padding: 60px 40px;
        text-align: center;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    }
    
    .success-icon {
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 30px;
        color: white;
        font-size: 2.5rem;
    }
    
    .progress-bar {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 16px;
        padding: 25px 30px;
        margin-bottom: 30px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
    }
    
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'progress' not in st.session_state:
    st.session_state.progress = 0

# Calculate progress
def calculate_progress():
    total = 18  # 3 info fields + 15 questions
    answered = 0
    
    # Check info fields
    if st.session_state.get('student_name'): answered += 1
    if st.session_state.get('section'): answered += 1
    if st.session_state.get('date_filled'): answered += 1
    
    # Check radio questions
    radio_questions = ['gender', 'grades', 'workload', 'study_hours', 'grade_effect', 
                      'test_anxiety', 'cheating', 'stress_freq', 'relationships', 
                      'sleep_sacrifice', 'support', 'recommend_changes']
    for q in radio_questions:
        if st.session_state.get(q): answered += 1
    
    # Check checkbox questions (at least one selected)
    checkbox_questions = ['pressure_source', 'symptoms', 'coping']
    for q in checkbox_questions:
        if st.session_state.get(q) and len(st.session_state.get(q)) > 0: answered += 1
    
    return int((answered / total) * 100)

# Header
st.markdown("""
<div class="header-section">
    <h1>Academic Pressure Survey</h1>
    <p class="subtitle">This survey aims to understand the academic pressure experienced by Grade 10 students and its impact on your academic performance and overall well-being.</p>
    <div class="privacy-box">
        <strong>🔒 Confidentiality Notice:</strong> Your responses are completely confidential and will be used for research purposes only. Personal information (Name, Section) is collected only for identification and will not be shared publicly.
    </div>
</div>
""", unsafe_allow_html=True)

# Progress bar
progress = calculate_progress()
st.markdown(f"""
<div class="progress-bar">
    <div style="display: flex; justify-content: space-between; margin-bottom: 12px; font-weight: 600; color: #4a5568;">
        <span>Survey Progress</span>
        <span>{progress}%</span>
    </div>
</div>
""", unsafe_allow_html=True)
st.progress(progress)

# Survey Form
if not st.session_state.submitted:
    with st.form("survey_form"):
        
        # Section 0: Student Information
        st.markdown("""
        <div class="section-box">
            <div class="section-title">
                <div class="section-icon">📝</div>
                Student Information
            </div>
            <div class="section-desc">Required for identification purposes</div>
        """, unsafe_allow_html=True)
        
        st.text_input("Full Name *", key="student_name", placeholder="Enter your full name")
        st.text_input("Section/Class *", key="section", placeholder="e.g., Grade 10 - Section A")
        st.date_input("Date *", key="date_filled", value=datetime.now())
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Section A: Demographics
        st.markdown("""
        <div class="section-box">
            <div class="section-title">
                <div class="section-icon">👤</div>
                Section A: Demographics
            </div>
            <div class="section-desc">Basic information to help us categorize responses</div>
        """, unsafe_allow_html=True)
        
        st.radio("1. What is your gender? *", 
                options=["Male", "Female", "Prefer not to say"], 
                key="gender", index=None)
        
        st.radio("2. What is your average grade range? *", 
                options=["90-100 (Excellent)", "80-89 (Very Good)", "75-79 (Good)", 
                        "Below 75 (Average/Needs Improvement)"], 
                key="grades", index=None)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Section B: Academic Pressure Sources
        st.markdown("""
        <div class="section-box">
            <div class="section-title">
                <div class="section-icon">📚</div>
                Section B: Sources of Academic Pressure
            </div>
            <div class="section-desc">Identify where your academic pressure comes from</div>
        """, unsafe_allow_html=True)
        
        st.radio("3. How often do you feel overwhelmed by academic workload? *", 
                options=["1 - Never", "2 - Rarely", "3 - Sometimes", "4 - Often", "5 - Always"], 
                key="workload", index=None, horizontal=True)
        
        st.multiselect("4. Who or what puts the most pressure on you academically? (Select all that apply) *", 
                      options=["Parents/Guardians", "Teachers", "Peers/Classmates", 
                              "Myself (Self-imposed)", "College/University preparation", 
                              "Fear of low grades"], 
                      key="pressure_source")
        
        st.radio("5. How many hours do you spend studying/doing homework on weekdays? *", 
                options=["0-2 hours", "2-4 hours", "4-6 hours", "More than 6 hours"], 
                key="study_hours", index=None)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Section C: Effects on Academic Performance
        st.markdown("""
        <div class="section-box">
            <div class="section-title">
                <div class="section-icon">📊</div>
                Section C: Effects on Academic Performance
            </div>
            <div class="section-desc">How pressure affects your school performance</div>
        """, unsafe_allow_html=True)
        
        st.radio("6. Has academic pressure affected your grades? *", 
                options=["Yes, it has motivated me to get better grades", 
                        "Yes, it has caused my grades to drop",
                        "No noticeable effect", "Not sure"], 
                key="grade_effect", index=None)
        
        st.radio("7. How often do you experience test anxiety? *", 
                options=["1 - Never", "2 - Rarely", "3 - Sometimes", "4 - Often", "5 - Always"], 
                key="test_anxiety", index=None, horizontal=True)
        
        st.radio("8. Has pressure ever caused you to cheat or consider cheating on exams/assignments? *", 
                options=["Yes", "No, but I've considered it", "No, never"], 
                key="cheating", index=None)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Section D: Effects on Well-being
        st.markdown("""
        <div class="section-box">
            <div class="section-title">
                <div class="section-icon">🧠</div>
                Section D: Effects on Well-being
            </div>
            <div class="section-desc">Impact on your mental and physical health</div>
        """, unsafe_allow_html=True)
        
        st.radio("9. How often do you feel stressed about school? *", 
                options=["1 - Never", "2 - Rarely", "3 - Sometimes", "4 - Often", "5 - Always"], 
                key="stress_freq", index=None, horizontal=True)
        
        st.multiselect("10. Which of the following have you experienced due to academic pressure? (Select all that apply) *", 
                      options=["Sleep problems/Insomnia", "Frequent headaches", 
                              "Loss of appetite or overeating", "Constant fatigue",
                              "Anxiety/Panic attacks", "Feelings of depression/sadness",
                              "Loss of motivation", "None of the above"], 
                      key="symptoms")
        
        st.radio("11. Has academic pressure affected your relationships with family or friends? *", 
                options=["Yes, negatively (more conflicts, less time together)",
                        "Yes, positively (more support, understanding)", "No effect"], 
                key="relationships", index=None)
        
        st.radio("12. How often do you sacrifice sleep to study or complete assignments? *", 
                options=["Never", "Rarely (once a month)", "Sometimes (once a week)",
                        "Often (2-3 times a week)", "Almost every night"], 
                key="sleep_sacrifice", index=None)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Section E: Coping Mechanisms
        st.markdown("""
        <div class="section-box">
            <div class="section-title">
                <div class="section-icon">💪</div>
                Section E: Coping Strategies
            </div>
            <div class="section-desc">How you deal with academic pressure</div>
        """, unsafe_allow_html=True)
        
        st.multiselect("13. What do you do to cope with academic stress? (Select all that apply) *", 
                      options=["Exercise/Sports", "Hobbies (music, art, gaming, etc.)",
                              "Talking to friends", "Talking to family",
                              "Seeking help from school counselor", "Scrolling social media",
                              "Procrastination/Avoidance", "Nothing specific"], 
                      key="coping")
        
        st.radio("14. Do you feel you have adequate support from your school to handle academic pressure? *", 
                options=["Yes, definitely", "Somewhat", "No, not really", 
                        "Not aware of any support"], 
                key="support", index=None)
        
        # Question 15 - NEW
        st.radio("15. Would you recommend changes to the current academic system to reduce student pressure? *", 
                options=["Yes, major changes needed", "Yes, minor adjustments needed",
                        "No, the current system is fine", "Not sure/No opinion"], 
                key="recommend_changes", index=None)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Submit button
        submitted = st.form_submit_button("Submit Survey ✓", use_container_width=True)
        
        if submitted:
            # Validate required fields
            required_fields = ['student_name', 'section', 'date_filled', 'gender', 'grades',
                             'workload', 'pressure_source', 'study_hours', 'grade_effect',
                             'test_anxiety', 'cheating', 'stress_freq', 'symptoms',
                             'relationships', 'sleep_sacrifice', 'coping', 'support', 'recommend_changes']
            
            missing = []
            for field in required_fields:
                value = st.session_state.get(field)
                if not value or (isinstance(value, list) and len(value) == 0):
                    missing.append(field)
            
            if missing:
                st.error("⚠️ Please fill in all required fields before submitting.")
            else:
                # Prepare data
                data = {
                    'timestamp': datetime.now().isoformat(),
                    'student_name': st.session_state.student_name,
                    'section': st.session_state.section,
                    'date_filled': str(st.session_state.date_filled),
                    'gender': st.session_state.gender,
                    'grades': st.session_state.grades,
                    'workload': st.session_state.workload,
                    'pressure_source': ', '.join(st.session_state.pressure_source),
                    'study_hours': st.session_state.study_hours,
                    'grade_effect': st.session_state.grade_effect,
                    'test_anxiety': st.session_state.test_anxiety,
                    'cheating': st.session_state.cheating,
                    'stress_freq': st.session_state.stress_freq,
                    'symptoms': ', '.join(st.session_state.symptoms),
                    'relationships': st.session_state.relationships,
                    'sleep_sacrifice': st.session_state.sleep_sacrifice,
                    'coping': ', '.join(st.session_state.coping),
                    'support': st.session_state.support,
                    'recommend_changes': st.session_state.recommend_changes
                }
                
                # Save to CSV (local storage)
                df = pd.DataFrame([data])
                df.to_csv('survey_responses.csv', mode='a', header=not pd.io.common.file_exists('survey_responses.csv'), index=False)
                
                st.session_state.submitted = True
                st.rerun()

# Success message
if st.session_state.submitted:
    st.markdown("""
    <div class="success-message">
        <div class="success-icon">✓</div>
        <h2 style="color: #2d3748; font-family: 'Inter', sans-serif; margin-bottom: 15px;">Thank You!</h2>
        <p style="color: #718096; font-size: 1.1rem;">Your response has been recorded successfully. Your participation helps us better understand student experiences with academic pressure.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Option to submit another response
    if st.button("Submit Another Response"):
        for key in list(st.session_state.keys()):
            if key not in ['submitted']:
                del st.session_state[key]
        st.session_state.submitted = False
        st.rerun()