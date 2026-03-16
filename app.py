import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
import json
import os

# Page configuration
st.set_page_config(
    page_title="Academic Pressure Survey - Grade 10",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for DARK MODE
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        font-family: 'Inter', sans-serif;
    }

    .stApp, .stMarkdown, .stText, p, h1, h2, h3, h4, h5, h6, label, span, div {
        color: #e2e8f0 !important;
    }

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

    .stRadio label, .stCheckbox label, .stMultiSelect label, 
    .stTextInput label, .stDateInput label {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
    }

    .stRadio > div[role="radiogroup"] > label,
    .stCheckbox > div > label {
        color: #e2e8f0 !important;
        font-weight: 500 !important;
        background: rgba(51, 65, 85, 0.6);
        border-radius: 12px;
        padding: 12px 15px;
        margin-bottom: 8px;
        border: 2px solid rgba(255, 255, 255, 0.1);
    }

    .stRadio > div[role="radiogroup"] > label:hover,
    .stCheckbox > div > label:hover {
        border-color: #667eea;
        background: rgba(102, 126, 234, 0.2);
    }

    .stTextInput > div > div > input, 
    .stDateInput > div > div > input {
        background: rgba(51, 65, 85, 0.8) !important;
        border: 2px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        padding: 15px !important;
        font-size: 1rem !important;
        color: #f1f5f9 !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: #94a3b8 !important;
    }

    .stMultiSelect > div > div > div {
        background: rgba(51, 65, 85, 0.8) !important;
        border: 2px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: #f1f5f9 !important;
    }

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

    .stAlert > div {
        background: rgba(254, 215, 215, 0.1) !important;
        border-left: 4px solid #f87171 !important;
        color: #fca5a5 !important;
    }

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

    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
    }

    /* Dashboard specific styles */
    .dashboard-card {
        background: rgba(30, 41, 59, 0.95);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #667eea !important;
    }

    .stat-label {
        color: #94a3b8 !important;
        font-size: 0.9rem;
    }

    .download-btn {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%) !important;
        color: white !important;
        padding: 10px 20px !important;
        border-radius: 8px !important;
        text-decoration: none !important;
        display: inline-block !important;
        margin-top: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# DATA STORAGE OPTIONS
# Option 1: Local CSV file (works on Streamlit Cloud but resets on redeploy)
# Option 2: Google Sheets (persistent)
# Option 3: JSON file (better for this use case)

DATA_FILE = 'survey_data.json'

def load_data():
    """Load existing survey data"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    """Save survey data"""
    existing = load_data()
    existing.append(data)
    with open(DATA_FILE, 'w') as f:
        json.dump(existing, f, indent=2)
    return existing

def get_dataframe():
    """Convert data to pandas DataFrame"""
    data = load_data()
    if not data:
        return pd.DataFrame()
    return pd.DataFrame(data)

# Initialize session state
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# SIDEBAR NAVIGATION
st.sidebar.markdown("## 📊 Navigation")
page = st.sidebar.radio("Go to:", ["📝 Take Survey", "📈 View Dashboard"])

if page == "📝 Take Survey":
    # SURVEY PAGE

    def calculate_progress():
        total = 18
        answered = 0
        if st.session_state.get('student_name'): answered += 1
        if st.session_state.get('section'): answered += 1
        if st.session_state.get('date_filled'): answered += 1

        radio_qs = ['gender', 'grades', 'workload', 'study_hours', 'grade_effect', 
                   'test_anxiety', 'cheating', 'stress_freq', 'relationships', 
                   'sleep_sacrifice', 'support', 'recommend_changes']
        for q in radio_qs:
            if st.session_state.get(q): answered += 1

        checkbox_qs = ['pressure_source', 'symptoms', 'coping']
        for q in checkbox_qs:
            if st.session_state.get(q) and len(st.session_state.get(q)) > 0: answered += 1

        return int((answered / total) * 100)

    # Header
    st.markdown("""
    <div class="header-section">
        <h1 class="header-title">Academic Pressure Survey</h1>
        <p class="header-subtitle">This survey aims to understand the academic pressure experienced by Grade 10 students.</p>
        <div class="privacy-box">
            <span style="color: #e2e8f0;"><strong style="color: #f1f5f9;">🔒 Confidentiality Notice:</strong> Your responses are completely confidential and will be used for research purposes only.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Progress bar
    progress = calculate_progress()
    st.markdown(f'<div class="section-box"><div style="display: flex; justify-content: space-between; margin-bottom: 10px;"><span>Survey Progress</span><span>{progress}%</span></div></div>', unsafe_allow_html=True)
    st.progress(progress)

    if not st.session_state.submitted:
        with st.form("survey_form"):

            # Student Information
            st.markdown('<div class="section-box">', unsafe_allow_html=True)
            st.markdown('<div class="section-title"><div class="section-icon">📝</div><span style="color: #f1f5f9;">Student Information</span></div>', unsafe_allow_html=True)
            st.text_input("Full Name", key="student_name", placeholder="Enter your full name")
            st.text_input("Section/Class", key="section", placeholder="e.g., Grade 10 - Section A")
            st.date_input("Date", key="date_filled", value=datetime.now())
            st.markdown('</div>', unsafe_allow_html=True)

            # Section A
            st.markdown('<div class="section-box">', unsafe_allow_html=True)
            st.markdown('<div class="section-title"><div class="section-icon">👤</div><span style="color: #f1f5f9;">Section A: Demographics</span></div>', unsafe_allow_html=True)
            st.markdown('<p class="question-text">1. What is your gender? <span class="required">*</span></p>', unsafe_allow_html=True)
            st.radio("Gender", options=["Male", "Female", "Prefer not to say"], key="gender", index=None, label_visibility="collapsed")
            st.markdown('<p class="question-text">2. What is your average grade range? <span class="required">*</span></p>', unsafe_allow_html=True)
            st.radio("Grades", options=["90-100 (Excellent)", "80-89 (Very Good)", "75-79 (Good)", "Below 75 (Average/Needs Improvement)"], key="grades", index=None, label_visibility="collapsed")
            st.markdown('</div>', unsafe_allow_html=True)

            # Section B
            st.markdown('<div class="section-box">', unsafe_allow_html=True)
            st.markdown('<div class="section-title"><div class="section-icon">📚</div><span style="color: #f1f5f9;">Section B: Sources of Academic Pressure</span></div>', unsafe_allow_html=True)
            st.markdown('<p class="question-text">3. How often do you feel overwhelmed by academic workload? <span class="required">*</span></p>', unsafe_allow_html=True)
            st.radio("Workload", options=["1 - Never", "2 - Rarely", "3 - Sometimes", "4 - Often", "5 - Always"], key="workload", index=None, label_visibility="collapsed", horizontal=True)
            st.markdown('<p class="question-text">4. Who or what puts the most pressure on you? (Select all) <span class="required">*</span></p>', unsafe_allow_html=True)
            st.multiselect("Pressure", options=["Parents/Guardians", "Teachers", "Peers/Classmates", "Myself (Self-imposed)", "College/University preparation", "Fear of low grades"], key="pressure_source", label_visibility="collapsed")
            st.markdown('<p class="question-text">5. How many hours do you spend studying on weekdays? <span class="required">*</span></p>', unsafe_allow_html=True)
            st.radio("Hours", options=["0-2 hours", "2-4 hours", "4-6 hours", "More than 6 hours"], key="study_hours", index=None, label_visibility="collapsed")
            st.markdown('</div>', unsafe_allow_html=True)

            # Section C
            st.markdown('<div class="section-box">', unsafe_allow_html=True)
            st.markdown('<div class="section-title"><div class="section-icon">📊</div><span style="color: #f1f5f9;">Section C: Effects on Academic Performance</span></div>', unsafe_allow_html=True)
            st.markdown('<p class="question-text">6. Has academic pressure affected your grades? <span class="required">*</span></p>', unsafe_allow_html=True)
            st.radio("Effect", options=["Yes, improved", "Yes, declined", "No effect", "Not sure"], key="grade_effect", index=None, label_visibility="collapsed")
            st.markdown('<p class="question-text">7. How often do you experience test anxiety? <span class="required">*</span></p>', unsafe_allow_html=True)
            st.radio("Anxiety", options=["1 - Never", "2 - Rarely", "3 - Sometimes", "4 - Often", "5 - Always"], key="test_anxiety", index=None, label_visibility="collapsed", horizontal=True)
            st.markdown('<p class="question-text">8. Has pressure caused you to consider cheating? <span class="required">*</span></p>', unsafe_allow_html=True)
            st.radio("Cheating", options=["Yes", "No, but considered it", "No, never"], key="cheating", index=None, label_visibility="collapsed")
            st.markdown('</div>', unsafe_allow_html=True)

            # Section D
            st.markdown('<div class="section-box">', unsafe_allow_html=True)
            st.markdown('<div class="section-title"><div class="section-icon">🧠</div><span style="color: #f1f5f9;">Section D: Effects on Well-being</span></div>', unsafe_allow_html=True)
            st.markdown('<p class="question-text">9. How often do you feel stressed? <span class="required">*</span></p>', unsafe_allow_html=True)
            st.radio("Stress", options=["1 - Never", "2 - Rarely", "3 - Sometimes", "4 - Often", "5 - Always"], key="stress_freq", index=None, label_visibility="collapsed", horizontal=True)
            st.markdown('<p class="question-text">10. Symptoms experienced (Select all) <span class="required">*</span></p>', unsafe_allow_html=True)
            st.multiselect("Symptoms", options=["Sleep problems", "Headaches", "Appetite changes", "Fatigue", "Anxiety", "Depression", "Loss of motivation", "None"], key="symptoms", label_visibility="collapsed")
            st.markdown('<p class="question-text">11. Effect on relationships? <span class="required">*</span></p>', unsafe_allow_html=True)
            st.radio("Relationships", options=["Yes, negatively", "Yes, positively", "No effect"], key="relationships", index=None, label_visibility="collapsed")
            st.markdown('<p class="question-text">12. How often do you sacrifice sleep? <span class="required">*</span></p>', unsafe_allow_html=True)
            st.radio("Sleep", options=["Never", "Rarely", "Sometimes", "Often", "Almost every night"], key="sleep_sacrifice", index=None, label_visibility="collapsed")
            st.markdown('</div>', unsafe_allow_html=True)

            # Section E
            st.markdown('<div class="section-box">', unsafe_allow_html=True)
            st.markdown('<div class="section-title"><div class="section-icon">💪</div><span style="color: #f1f5f9;">Section E: Coping Strategies</span></div>', unsafe_allow_html=True)
            st.markdown('<p class="question-text">13. Coping strategies (Select all) <span class="required">*</span></p>', unsafe_allow_html=True)
            st.multiselect("Coping", options=["Exercise/Sports", "Hobbies", "Talking to friends", "Talking to family", "School counselor", "Social media", "Procrastination", "Nothing specific"], key="coping", label_visibility="collapsed")
            st.markdown('<p class="question-text">14. Do you have adequate school support? <span class="required">*</span></p>', unsafe_allow_html=True)
            st.radio("Support", options=["Yes, definitely", "Somewhat", "No, not really", "Not aware"], key="support", index=None, label_visibility="collapsed")
            st.markdown('<p class="question-text">15. Recommend changes to academic system? <span class="required">*</span></p>', unsafe_allow_html=True)
            st.radio("Changes", options=["Yes, major changes", "Yes, minor adjustments", "No, system is fine", "Not sure"], key="recommend_changes", index=None, label_visibility="collapsed")
            st.markdown('</div>', unsafe_allow_html=True)

            submitted = st.form_submit_button("Submit Survey ✓", use_container_width=True)

            if submitted:
                required = ['student_name', 'section', 'date_filled', 'gender', 'grades',
                           'workload', 'pressure_source', 'study_hours', 'grade_effect',
                           'test_anxiety', 'cheating', 'stress_freq', 'symptoms',
                           'relationships', 'sleep_sacrifice', 'coping', 'support', 'recommend_changes']

                missing = [f for f in required if not st.session_state.get(f) or 
                          (isinstance(st.session_state.get(f), list) and len(st.session_state.get(f)) == 0)]

                if missing:
                    st.error("⚠️ Please fill in all required fields.")
                else:
                    data = {
                        'timestamp': datetime.now().isoformat(),
                        'student_name': st.session_state.student_name,
                        'section': st.session_state.section,
                        'date_filled': str(st.session_state.date_filled),
                        'gender': st.session_state.gender,
                        'grades': st.session_state.grades,
                        'workload': st.session_state.workload,
                        'pressure_source': st.session_state.pressure_source,
                        'study_hours': st.session_state.study_hours,
                        'grade_effect': st.session_state.grade_effect,
                        'test_anxiety': st.session_state.test_anxiety,
                        'cheating': st.session_state.cheating,
                        'stress_freq': st.session_state.stress_freq,
                        'symptoms': st.session_state.symptoms,
                        'relationships': st.session_state.relationships,
                        'sleep_sacrifice': st.session_state.sleep_sacrifice,
                        'coping': st.session_state.coping,
                        'support': st.session_state.support,
                        'recommend_changes': st.session_state.recommend_changes
                    }
                    save_data(data)
                    st.session_state.submitted = True
                    st.rerun()

    if st.session_state.submitted:
        st.markdown("""
        <div class="success-box">
            <div class="success-icon">✓</div>
            <div class="success-title">Thank You!</div>
            <div class="success-text">Your response has been recorded successfully.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Submit Another Response"):
            for key in list(st.session_state.keys()):
                if key not in ['submitted']:
                    del st.session_state[key]
            st.session_state.submitted = False
            st.rerun()

else:
    # DASHBOARD PAGE
    st.markdown("""
    <div class="header-section">
        <h1 class="header-title">📊 Survey Dashboard</h1>
        <p class="header-subtitle">View responses and analyze data for your research</p>
    </div>
    """, unsafe_allow_html=True)

    df = get_dataframe()

    if df.empty:
        st.warning("No data collected yet. Responses will appear here once students submit the survey.")
    else:
        # Statistics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f'<div class="dashboard-card"><div class="stat-number">{len(df)}</div><div class="stat-label">Total Responses</div></div>', unsafe_allow_html=True)
        with col2:
            male_count = len(df[df['gender'] == 'Male'])
            st.markdown(f'<div class="dashboard-card"><div class="stat-number">{male_count}</div><div class="stat-label">Male Students</div></div>', unsafe_allow_html=True)
        with col3:
            female_count = len(df[df['gender'] == 'Female'])
            st.markdown(f'<div class="dashboard-card"><div class="stat-number">{female_count}</div><div class="stat-label">Female Students</div></div>', unsafe_allow_html=True)
        with col4:
            high_stress = len(df[df['stress_freq'].isin(['4 - Often', '5 - Always'])])
            st.markdown(f'<div class="dashboard-card"><div class="stat-number">{high_stress}</div><div class="stat-label">High Stress Students</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # PIE CHARTS
        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📈 Pie Charts for Research</div>', unsafe_allow_html=True)

        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            # Gender Distribution
            gender_counts = df['gender'].value_counts()
            fig1 = px.pie(values=gender_counts.values, names=gender_counts.index, 
                         title="Gender Distribution", color_discrete_sequence=['#667eea', '#764ba2', '#f093fb'])
            fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                            font_color='#e2e8f0', title_font_color='#f1f5f9')
            st.plotly_chart(fig1, use_container_width=True)

            # Grade Effect
            grade_effect_counts = df['grade_effect'].value_counts()
            fig2 = px.pie(values=grade_effect_counts.values, names=grade_effect_counts.index,
                         title="Effect of Pressure on Grades", color_discrete_sequence=['#48bb78', '#f5576c', '#4facfe', '#f093fb'])
            fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                            font_color='#e2e8f0', title_font_color='#f1f5f9')
            st.plotly_chart(fig2, use_container_width=True)

        with chart_col2:
            # Stress Frequency
            stress_counts = df['stress_freq'].value_counts()
            fig3 = px.pie(values=stress_counts.values, names=stress_counts.index,
                         title="Stress Frequency Distribution", color_discrete_sequence=['#48bb78', '#4facfe', '#667eea', '#f093fb', '#f5576c'])
            fig3.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                            font_color='#e2e8f0', title_font_color='#f1f5f9')
            st.plotly_chart(fig3, use_container_width=True)

            # Sleep Sacrifice
            sleep_counts = df['sleep_sacrifice'].value_counts()
            fig4 = px.pie(values=sleep_counts.values, names=sleep_counts.index,
                         title="Sleep Sacrifice Frequency", color_discrete_sequence=['#48bb78', '#4facfe', '#667eea', '#f093fb', '#f5576c'])
            fig4.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                            font_color='#e2e8f0', title_font_color='#f1f5f9')
            st.plotly_chart(fig4, use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # Additional Analysis
        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📊 Additional Analysis</div>', unsafe_allow_html=True)

        analysis_col1, analysis_col2 = st.columns(2)

        with analysis_col1:
            # Pressure Sources (exploded list)
            all_sources = []
            for sources in df['pressure_source']:
                if isinstance(sources, list):
                    all_sources.extend(sources)
            if all_sources:
                source_counts = pd.Series(all_sources).value_counts()
                fig5 = px.bar(x=source_counts.index, y=source_counts.values, 
                             title="Sources of Academic Pressure", 
                             color_discrete_sequence=['#667eea'])
                fig5.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                                font_color='#e2e8f0', title_font_color='#f1f5f9',
                                xaxis_title="Source", yaxis_title="Count")
                st.plotly_chart(fig5, use_container_width=True)

        with analysis_col2:
            # Coping Strategies
            all_coping = []
            for strategies in df['coping']:
                if isinstance(strategies, list):
                    all_coping.extend(strategies)
            if all_coping:
                coping_counts = pd.Series(all_coping).value_counts()
                fig6 = px.bar(x=coping_counts.index, y=coping_counts.values,
                             title="Coping Strategies Used",
                             color_discrete_sequence=['#764ba2'])
                fig6.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                                font_color='#e2e8f0', title_font_color='#f1f5f9',
                                xaxis_title="Strategy", yaxis_title="Count")
                st.plotly_chart(fig6, use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # Raw Data Table
        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📋 Raw Data</div>', unsafe_allow_html=True)

        # Convert lists to strings for display
        display_df = df.copy()
        for col in ['pressure_source', 'symptoms', 'coping']:
            if col in display_df.columns:
                display_df[col] = display_df[col].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)

        st.dataframe(display_df, use_container_width=True)

        # Download buttons
        col1, col2 = st.columns(2)
        with col1:
            csv = display_df.to_csv(index=False)
            st.download_button(label="📥 Download CSV", data=csv, file_name="survey_data.csv", mime="text/csv", use_container_width=True)
        with col2:
            json_str = df.to_json(orient='records', indent=2)
            st.download_button(label="📥 Download JSON", data=json_str, file_name="survey_data.json", mime="application/json", use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)