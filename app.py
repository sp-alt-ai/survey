
# Generate dark mode Streamlit code with light gray text

dark_mode_code = '''import streamlit as st
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Academic Pressure Survey - Grade 10",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for DARK MODE with light gray text
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Main dark background */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Force all text to be LIGHT GRAY */
    .stApp, .stMarkdown, .stText, p, h1, h2, h3, h4, h5, h6, label, span, div {
        color: #e2e8f0 !important;
    }
    
    /* Header section - dark */
    .header-section {
        background: rgba(30, 41, 59, 0.95);
        border-radius: 24px;
        padding: 50px 40px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
        border-top: 5px solid #667eea;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .header-title {
        color: #f1f5f9 !important;
        font-weight: 700 !important;
        font-size: 2.5rem !important;
        margin-bottom: 15px !important;
        font-family: 'Inter', sans-serif;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .header-subtitle {
        color: #cbd5e1 !important;
        font-size: 1.1rem;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    .privacy-box {
        background: rgba(51, 65, 85, 0.8);
        border-left: 4px solid #667eea;
        padding: 15px 20px;
        margin-top: 20px;
        border-radius: 8px;
        text-align: left;
        font-size: 0.9rem;
        color: #e2e8f0 !important;
    }
    
    .privacy-box strong {
        color: #f1f5f9 !important;
    }
    
    /* Progress bar - dark */
    .progress-container {
        background: rgba(30, 41, 59, 0.95);
        border-radius: 16px;
        padding: 25px 30px;
        margin-bottom: 30px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .progress-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 12px;
        font-weight: 600;
        color: #e2e8f0 !important;
        font-size: 0.95rem;
    }
    
    /* Section boxes - dark */
    .section-box {
        background: rgba(30, 41, 59, 0.95);
        border-radius: 24px;
        padding: 40px;
        margin-bottom: 25px;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .section-title {
        color: #f1f5f9 !important;
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
        font-weight: 600;
    }
    
    .section-desc {
        color: #94a3b8 !important;
        margin-bottom: 30px;
        margin-left: 52px;
        font-size: 0.95rem;
    }
    
    /* Question text */
    .question-text {
        font-weight: 600;
        color: #f1f5f9 !important;
        margin-bottom: 15px;
        font-size: 1.05rem;
    }
    
    .required {
        color: #f87171 !important;
        margin-left: 4px;
        font-weight: 700;
    }
    
    /* Form elements - dark theme */
    .stRadio label, .stCheckbox label, .stMultiSelect label, 
    .stTextInput label, .stDateInput label {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
    }
    
    /* Radio and checkbox options - dark */
    .stRadio > div[role="radiogroup"] > label,
    .stCheckbox > div > label {
        color: #e2e8f0 !important;
        font-weight: 500 !important;
        background: rgba(51, 65, 85, 0.6);
        border-radius: 12px;
        padding: 12px 15px;
        margin-bottom: 8px;
        border: 2px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .stRadio > div[role="radiogroup"] > label:hover,
    .stCheckbox > div > label:hover {
        border-color: #667eea;
        background: rgba(102, 126, 234, 0.2);
    }
    
    /* Text inputs - dark */
    .stTextInput > div > div > input, 
    .stDateInput > div > div > input {
        background: rgba(51, 65, 85, 0.8) !important;
        border: 2px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        padding: 15px !important;
        font-size: 1rem !important;
        color: #f1f5f9 !important;
    }
    
    .stTextInput > div > div > input::placeholder,
    .stDateInput > div > div > input::placeholder {
        color: #94a3b8 !important;
    }
    
    .stTextInput > div > div > input:focus, 
    .stDateInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2) !important;
    }
    
    /* Multiselect - dark */
    .stMultiSelect > div > div > div {
        background: rgba(51, 65, 85, 0.8) !important;
        border: 2px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: #f1f5f9 !important;
    }
    
    /* Calendar popup dark */
    .stDateInput > div > div > div > div {
        background: #1e293b !important;
        color: #e2e8f0 !important;
    }
    
    /* Success message - dark */
    .success-box {
        background: rgba(30, 41, 59, 0.95);
        border-radius: 24px;
        padding: 60px 40px;
        text-align: center;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.1);
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
        font-weight: 700;
    }
    
    .success-title {
        color: #f1f5f9 !important;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 15px;
    }
    
    .success-text {
        color: #cbd5e1 !important;
        font-size: 1.1rem;
    }
    
    /* Error message - dark */
    .stAlert > div {
        background: rgba(254, 215, 215, 0.1) !important;
        border-left: 4px solid #f87171 !important;
        color: #fca5a5 !important;
    }
    
    /* Submit button */
    .stFormSubmitButton > button {
        width: 100%;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 16px !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        margin-top: 20px !important;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    /* Streamlit default overrides for dark */
    .css-1d391kg, .css-1lcbmhc, .css-1v3fvcr {
        background: transparent !important;
    }
    
    /* Ensure all Streamlit text is light */
    .css-10trblm, .css-1q8dd3e, .css-81oif8 {
        color: #e2e8f0 !important;
    }
    
    /* Help text */
    .css-1aehpvj {
        color: #94a3b8 !important;
    }
    
    /* Date picker calendar */
    .css-1uixxpy {
        background: #1e293b !important;
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

# Header with light text on dark background
st.markdown("""
<div class="header-section">
    <h1 class="header-title">Academic Pressure Survey</h1>
    <p class="header-subtitle">This survey aims to understand the academic pressure experienced by Grade 10 students and its impact on your academic performance and overall well-being.</p>
    <div class="privacy-box">
        <span style="color: #e2e8f0;"><strong style="color: #f1f5f9;">🔒 Confidentiality Notice:</strong> Your responses are completely confidential and will be used for research purposes only. Personal information (Name, Section) is collected only for identification and will not be shared publicly.</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Progress bar
progress = calculate_progress()
st.markdown(f"""
<div class="progress-container">
    <div class="progress-header">
        <span style="color: #e2e8f0;">Survey Progress</span>
        <span style="color: #e2e8f0;">{progress}%</span>
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
                <span style="color: #f1f5f9;">Student Information</span>
            </div>
            <div class="section-desc">Required for identification purposes</div>
        """, unsafe_allow_html=True)
        
        st.text_input("Full Name", key="student_name", placeholder="Enter your full name")
        st.text_input("Section/Class", key="section", placeholder="e.g., Grade 10 - Section A")
        st.date_input("Date", key="date_filled", value=datetime.now())
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Section A: Demographics
        st.markdown("""
        <div class="section-box">
            <div class="section-title">
                <div class="section-icon">👤</div>
                <span style="color: #f1f5f9;">Section A: Demographics</span>
            </div>
            <div class="section-desc">Basic information to help us categorize responses</div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="question-text">1. What is your gender? <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.radio("Gender", 
                options=["Male", "Female", "Prefer not to say"], 
                key="gender", index=None, label_visibility="collapsed")
        
        st.markdown('<p class="question-text">2. What is your average grade range? <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.radio("Grades", 
                options=["90-100 (Excellent)", "80-89 (Very Good)", "75-79 (Good)", 
                        "Below 75 (Average/Needs Improvement)"], 
                key="grades", index=None, label_visibility="collapsed")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Section B: Academic Pressure Sources
        st.markdown("""
        <div class="section-box">
            <div class="section-title">
                <div class="section-icon">📚</div>
                <span style="color: #f1f5f9;">Section B: Sources of Academic Pressure</span>
            </div>
            <div class="section-desc">Identify where your academic pressure comes from</div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="question-text">3. How often do you feel overwhelmed by academic workload? <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.radio("Workload", 
                options=["1 - Never", "2 - Rarely", "3 - Sometimes", "4 - Often", "5 - Always"], 
                key="workload", index=None, label_visibility="collapsed", horizontal=True)
        
        st.markdown('<p class="question-text">4. Who or what puts the most pressure on you academically? (Select all that apply) <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.multiselect("Pressure Sources", 
                      options=["Parents/Guardians", "Teachers", "Peers/Classmates", 
                              "Myself (Self-imposed)", "College/University preparation", 
                              "Fear of low grades"], 
                      key="pressure_source", label_visibility="collapsed")
        
        st.markdown('<p class="question-text">5. How many hours do you spend studying/doing homework on weekdays? <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.radio("Study Hours", 
                options=["0-2 hours", "2-4 hours", "4-6 hours", "More than 6 hours"], 
                key="study_hours", index=None, label_visibility="collapsed")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Section C: Effects on Academic Performance
        st.markdown("""
        <div class="section-box">
            <div class="section-title">
                <div class="section-icon">📊</div>
                <span style="color: #f1f5f9;">Section C: Effects on Academic Performance</span>
            </div>
            <div class="section-desc">How pressure affects your school performance</div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="question-text">6. Has academic pressure affected your grades? <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.radio("Grade Effect", 
                options=["Yes, it has motivated me to get better grades", 
                        "Yes, it has caused my grades to drop",
                        "No noticeable effect", "Not sure"], 
                key="grade_effect", index=None, label_visibility="collapsed")
        
        st.markdown('<p class="question-text">7. How often do you experience test anxiety? <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.radio("Test Anxiety", 
                options=["1 - Never", "2 - Rarely", "3 - Sometimes", "4 - Often", "5 - Always"], 
                key="test_anxiety", index=None, label_visibility="collapsed", horizontal=True)
        
        st.markdown('<p class="question-text">8. Has pressure ever caused you to cheat or consider cheating on exams/assignments? <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.radio("Cheating", 
                options=["Yes", "No, but I've considered it", "No, never"], 
                key="cheating", index=None, label_visibility="collapsed")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Section D: Effects on Well-being
        st.markdown("""
        <div class="section-box">
            <div class="section-title">
                <div class="section-icon">🧠</div>
                <span style="color: #f1f5f9;">Section D: Effects on Well-being</span>
            </div>
            <div class="section-desc">Impact on your mental and physical health</div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="question-text">9. How often do you feel stressed about school? <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.radio("Stress Frequency", 
                options=["1 - Never", "2 - Rarely", "3 - Sometimes", "4 - Often", "5 - Always"], 
                key="stress_freq", index=None, label_visibility="collapsed", horizontal=True)
        
        st.markdown('<p class="question-text">10. Which of the following have you experienced due to academic pressure? (Select all that apply) <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.multiselect("Symptoms", 
                      options=["Sleep problems/Insomnia", "Frequent headaches", 
                              "Loss of appetite or overeating", "Constant fatigue",
                              "Anxiety/Panic attacks", "Feelings of depression/sadness",
                              "Loss of motivation", "None of the above"], 
                      key="symptoms", label_visibility="collapsed")
        
        st.markdown('<p class="question-text">11. Has academic pressure affected your relationships with family or friends? <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.radio("Relationships", 
                options=["Yes, negatively (more conflicts, less time together)",
                        "Yes, positively (more support, understanding)", "No effect"], 
                key="relationships", index=None, label_visibility="collapsed")
        
        st.markdown('<p class="question-text">12. How often do you sacrifice sleep to study or complete assignments? <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.radio("Sleep Sacrifice", 
                options=["Never", "Rarely (once a month)", "Sometimes (once a week)",
                        "Often (2-3 times a week)", "Almost every night"], 
                key="sleep_sacrifice", index=None, label_visibility="collapsed")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Section E: Coping Mechanisms
        st.markdown("""
        <div class="section-box">
            <div class="section-title">
                <div class="section-icon">💪</div>
                <span style="color: #f1f5f9;">Section E: Coping Strategies</span>
            </div>
            <div class="section-desc">How you deal with academic pressure</div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="question-text">13. What do you do to cope with academic stress? (Select all that apply) <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.multiselect("Coping", 
                      options=["Exercise/Sports", "Hobbies (music, art, gaming, etc.)",
                              "Talking to friends", "Talking to family",
                              "Seeking help from school counselor", "Scrolling social media",
                              "Procrastination/Avoidance", "Nothing specific"], 
                      key="coping", label_visibility="collapsed")
        
        st.markdown('<p class="question-text">14. Do you feel you have adequate support from your school to handle academic pressure? <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.radio("Support", 
                options=["Yes, definitely", "Somewhat", "No, not really", 
                        "Not aware of any support"], 
                key="support", index=None, label_visibility="collapsed")
        
        st.markdown('<p class="question-text">15. Would you recommend changes to the current academic system to reduce student pressure? <span class="required">*</span></p>', 
                   unsafe_allow_html=True)
        st.radio("Recommend Changes", 
                options=["Yes, major changes needed", "Yes, minor adjustments needed",
                        "No, the current system is fine", "Not sure/No opinion"], 
                key="recommend_changes", index=None, label_visibility="collapsed")
        
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
                
                # Save to CSV
                df = pd.DataFrame([data])
                df.to_csv('survey_responses.csv', mode='a', 
                         header=not pd.io.common.file_exists('survey_responses.csv'), index=False)
                
                st.session_state.submitted = True
                st.rerun()

# Success message
if st.session_state.submitted:
    st.markdown("""
    <div class="success-box">
        <div class="success-icon">✓</div>
        <div class="success-title">Thank You!</div>
        <div class="success-text">Your response has been recorded successfully. Your participation helps us better understand student experiences with academic pressure.</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Submit Another Response", type="primary"):
        for key in list(st.session_state.keys()):
            if key not in ['submitted']:
                del st.session_state[key]
        st.session_state.submitted = False
        st.rerun()
'''

# Save to file
with open('/mnt/kimi/output/app_dark_mode.py', 'w', encoding='utf-8') as f:
    f.write(dark_mode_code)

print("✅ Dark Mode Streamlit code saved!")
print("\n🌙 Dark Mode Features:")
print("- Deep navy blue gradient background (#1a1a2e → #16213e → #0f3460)")
print("- Light gray text (#e2e8f0) for main content")
print("- Lighter gray (#f1f5f9) for headings")
print("- Medium gray (#94a3b8) for descriptions")
print("- Dark card backgrounds with subtle borders")
print("- Red accent (#f87171) for required fields")
print("- Purple gradient buttons maintained")
print("\n📁 File saved to: /mnt/kimi/output/app_dark_mode.py")
print("\n⚠️ Remember to also create requirements.txt:")
print("   streamlit")
print("   pandas")
