import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Actico Internship Portfolio",
    page_icon="🇩🇪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for German-inspired styling
st.markdown("""
<style>
    .main-header {
        color: #D4AF37;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #B8860B;
        border-bottom: 3px solid #D4AF37;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .highlight-box {
        background: linear-gradient(135deg, #FFF8DC, #F5F5DC);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #D4AF37;
        margin: 1rem 0;
    }
    .german-quote {
        font-style: italic;
        color: #8B4513;
        text-align: center;
        font-size: 1.2rem;
        margin: 1rem 0;
    }
    .progress-container {
        background-color: #f0f0f0;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("## 🇩🇪 Portfolio Navigation")
st.sidebar.markdown("---")

# Progress tracking
sections = [
    "🏠 Home & Introduction",
    "🇩🇪 German Connection",
    "🤖 AI/ML Journey", 
    "💼 Professional Experience",
    "📝 Cover Letter",
    "🎯 Why Actico?"
]

# Progress bar in sidebar
progress_placeholder = st.sidebar.empty()
current_section = st.sidebar.selectbox("Navigate to:", sections)

# Calculate progress based on selected section
current_index = sections.index(current_section)
progress = (current_index + 1) / len(sections)

with progress_placeholder.container():
    st.markdown("### 📊 Portfolio Progress")
    st.progress(progress)
    st.caption(f"Section {current_index + 1} of {len(sections)} ({int(progress * 100)}% complete)")

# Sidebar stats
st.sidebar.markdown("---")
st.sidebar.markdown("### 📈 Quick Stats")
st.sidebar.metric("German Proficiency", "B1.2", "PASCH Scholar")
st.sidebar.metric("AI/ML Projects", "5+", "AWS Certified")
st.sidebar.metric("Internships", "3", "IIM, DRDO, Dr. Oetker")

# Main content based on navigation
if current_section == "🏠 Home & Introduction":
    st.markdown('<h1 class="main-header">Welcome to My Actico Portfolio</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="german-quote">"Ich habe eine besondere Verbindung zu Deutschland"</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3>🚀 Aspiring AI/ML Engineer & German Enthusiast</h3>
        <p>Combining technical expertise in Artificial Intelligence with deep cultural appreciation for Germany, 
        I bring a unique perspective to innovative technology solutions. My journey spans from PASCH scholarship 
        in Germany to cutting-edge AI research and practical industry experience.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key highlights
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🇩🇪 German Heritage")
        st.write("• PASCH Scholar 2019")
        st.write("• German B1.2 Certified")
        st.write("• Cultural Immersion in SPO")
        st.write("• Deep appreciation for German culture")
    
    with col2:
        st.markdown("### 🤖 AI/ML Expertise")
        st.write("• AWS DeepRacer Champion")
        st.write("• Udacity AI Scholarship")
        st.write("• AISS 2023 Participant")
        st.write("• Federated Learning Research")
    
    with col3:
        st.markdown("### 💼 Professional Impact")
        st.write("• Product Intern at Dr. Oetker")
        st.write("• Research at IIM")
        st.write("• DRDO Collaboration")
        st.write("• FIT 2 German Topper")

elif current_section == "🇩🇪 German Connection":
    st.markdown('<h2 class="section-header">Meine Besondere Verbindung zu Deutschland</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h4>🏕️ PASCH Experience - Sankt Peter-Ording 2019</h4>
        <p>My transformative journey began on June 1st, 2019, when I embarked on an unforgettable German immersion 
        experience that shaped my cultural understanding and language skills.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Timeline visualization
    timeline_data = {
        'Date': ['June 1, 2019', 'June 2019', 'July 2019', 'August 2019', '2020-2021'],
        'Event': ['Flight to Hamburg via Zurich', 'PASCH Camp - SPO', 'B1.2 Certification', 'Cultural Integration', 'Continued German Studies'],
        'Impact': ['Cultural Immersion Begins', 'Quatschköpfer Group', 'Language Mastery', 'Lifelong Friendships', 'Academic Excellence']
    }
    
    df_timeline = pd.DataFrame(timeline_data)
    st.markdown("### 📅 German Journey Timeline")
    st.dataframe(df_timeline, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🎵 Cultural Highlights")
        st.write("**Favorite German Song:** *An der Nordseeküste*")
        st.write("**Camp Activities:** Werwolf, Baseball, Cultural Nights")
        st.write("**Friendships:** International bonds with Vietnam, Thailand, Singapore")
        st.write("**Achievements:** B1.2 Level - Highest in camp")
    
    with col2:
        st.markdown("### 🏆 German Achievements")
        achievements = {
            'Achievement': ['PASCH Scholarship', 'German FIT 2 Topper', 'B1.2 Certification', 'Dr. Oetker Internship'],
            'Year': [2019, 2020, 2019, 2021],
            'Significance': ['Cultural Exchange', 'Academic Excellence', 'Language Proficiency', 'Professional Application']
        }
        st.dataframe(pd.DataFrame(achievements), use_container_width=True)

elif current_section == "🤖 AI/ML Journey":
    st.markdown('<h2 class="section-header">Artificial Intelligence & Machine Learning Expertise</h2>', unsafe_allow_html=True)
    
    # AI Journey progression chart
    fig = go.Figure(data=go.Scatter(
        x=['2020: FIT 2 Victory', '2021: AWS DeepRacer', '2022: Udacity Scholarship', '2023: AISS Program', '2024: Advanced Research'],
        y=[1, 2, 3, 4, 5],
        mode='lines+markers',
        line=dict(color='#D4AF37', width=4),
        marker=dict(color='#B8860B', size=12),
        name='AI/ML Proficiency Growth'
    ))
    
    fig.update_layout(
        title="AI/ML Learning Progression",
        xaxis_title="Timeline",
        yaxis_title="Expertise Level",
        showlegend=False,
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h4>🏆 AWS DeepRacer Achievement</h4>
            <p>Mastered reinforcement learning fundamentals through hands-on autonomous racing simulation, 
            developing deep understanding of reward functions and model optimization.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🎓 Key Learning Areas")
        st.write("• **Federated Learning**: Distributed AI training")
        st.write("• **Coresets**: Efficient dataset representation")
        st.write("• **Reinforcement Learning**: AWS DeepRacer")
        st.write("• **Ethics in AI**: Social impact considerations")
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h4>🔬 AISS 2023 Research Insights</h4>
            <p>Explored cutting-edge concepts in federated learning and coresets, recognizing the need for 
            balanced AI research addressing both business and social dimensions.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📊 Technical Skills")
        skills_data = {
            'Skill': ['Machine Learning', 'Deep Learning', 'Python', 'Data Analysis', 'Research'],
            'Proficiency': [85, 80, 90, 85, 75]
        }
        skills_df = pd.DataFrame(skills_data)
        st.bar_chart(skills_df.set_index('Skill'))

elif current_section == "💼 Professional Experience":
    st.markdown('<h2 class="section-header">Professional Journey & Internships</h2>', unsafe_allow_html=True)
    
    # Experience cards
    experiences = [
        {
            'company': 'Dr. Oetker',
            'role': 'Product Intern',
            'period': '12th Grade',
            'description': 'Secured prestigious product internship through Goethe Institute connections, applying German language skills and cultural understanding in professional setting.',
            'skills': ['Product Development', 'German Business Culture', 'Cross-cultural Communication']
        },
        {
            'company': 'IIM (Indian Institute of Management)',
            'role': 'Research Intern',
            'period': 'Recent',
            'description': 'Conducted advanced research in management and technology intersection, developing analytical and strategic thinking capabilities.',
            'skills': ['Research Methodology', 'Data Analysis', 'Strategic Thinking']
        },
        {
            'company': 'DRDO (Defense Research)',
            'role': 'Technical Intern',
            'period': 'Recent',
            'description': 'Contributed to defense technology research, applying AI/ML knowledge to critical national security applications.',
            'skills': ['Defense Technology', 'AI Applications', 'Security Protocols']
        }
    ]
    
    for exp in experiences:
        st.markdown(f"""
        <div class="highlight-box">
            <h4>🏢 {exp['company']} - {exp['role']}</h4>
            <p><strong>Period:</strong> {exp['period']}</p>
            <p>{exp['description']}</p>
            <p><strong>Key Skills:</strong> {', '.join(exp['skills'])}</p>
        </div>
        """, unsafe_allow_html=True)

elif current_section == "📝 Cover Letter":
    st.markdown('<h2 class="section-header">Cover Letter for Actico</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3>Sehr geehrte Damen und Herren,</h3>
        
        <p>with great enthusiasm, I am writing to express my strong interest in the internship opportunity at Actico. 
        As someone who has cultivated both technical expertise in AI/ML and a deep cultural connection to Germany, 
        I believe I would bring a unique and valuable perspective to your innovative team.</p>
        
        <p><strong>Ich habe eine besondere Verbindung zu Deutschland</strong> - this connection began in 2019 when I was 
        selected as a PASCH Scholar and spent an transformative summer in Sankt Peter-Ording. Living among international 
        peers, achieving B1.2 German proficiency, and immersing myself in German culture shaped not only my language 
        skills but also my appreciation for German precision, innovation, and collaborative work ethic.</p>
        
        <p>My technical journey perfectly aligns with Actico's focus on intelligent automation and decision management. 
        As the FIT 2 German examination topper, I secured early recognition that led to a product internship at 
        Dr. Oetker - demonstrating how my German connection opens professional opportunities. My AI/ML expertise, 
        developed through AWS DeepRacer mastery, Udacity AI scholarship, and participation in IIITD's Artificial 
        Intelligence Summer School, provides me with practical knowledge of federated learning, coresets, and 
        ethical AI considerations.</p>
        
        <p>What makes me particularly excited about Actico is the opportunity to work with an entirely German team, 
        allowing me to utilize my cultural understanding and language skills while contributing to cutting-edge 
        decision automation technology. My diverse internship experience at IIM and DRDO has prepared me to tackle 
        complex challenges with both analytical rigor and creative problem-solving.</p>
        
        <p>I am confident that my unique combination of German cultural affinity, AI/ML technical skills, and 
        proven ability to thrive in international environments would make me a valuable addition to your team. 
        I look forward to the opportunity to contribute to Actico's mission while further developing my skills 
        in your innovative German work environment.</p>
        
        <p>Vielen Dank für Ihre Zeit und Überlegung. I eagerly await the opportunity to discuss how my passion 
        for both German culture and artificial intelligence can contribute to Actico's continued success.</p>
        
        <p><strong>Mit freundlichen Grüßen,</strong><br>
        [Your Name]</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive feedback section
    st.markdown("### 📝 Cover Letter Feedback")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("German References", "5", "Excellent")
    with col2:
        st.metric("Technical Alignment", "High", "Perfect Match")
    with col3:
        st.metric("Cultural Connection", "Strong", "Authentic")

elif current_section == "🎯 Why Actico?":
    st.markdown('<h2 class="section-header">Why Actico is the Perfect Match</h2>', unsafe_allow_html=True)
    
    reasons = [
        {
            'title': '🇩🇪 German Team Culture',
            'description': 'My PASCH experience and cultural immersion have prepared me to seamlessly integrate with German work culture and communication styles.'
        },
        {
            'title': '🤖 AI/ML Alignment',
            'description': 'Actico\'s focus on intelligent decision management perfectly matches my expertise in AI/ML, federated learning, and ethical AI considerations.'
        },
        {
            'title': '🔄 Decision Automation',
            'description': 'My research background and understanding of AI applications in business contexts align with Actico\'s automated decision-making solutions.'
        },
        {
            'title': '🌟 Innovation Opportunity',
            'description': 'The chance to contribute to cutting-edge technology while working in German language and cultural environment represents my ideal career development.'
        }
    ]
    
    for reason in reasons:
        st.markdown(f"""
        <div class="highlight-box">
            <h4>{reason['title']}</h4>
            <p>{reason['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Final call to action
    st.markdown("""
    <div style="text-align: center; margin-top: 3rem;">
        <h3 style="color: #D4AF37;">Ready to Contribute to Actico's Success!</h3>
        <p style="font-size: 1.2rem; color: #8B4513;">
            Bringing German cultural understanding, AI/ML expertise, and international perspective to your team.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #8B4513; padding: 1rem;">
    <p>🇩🇪 Erstellt mit Leidenschaft für Deutschland und Innovation • 🤖 Powered by AI/ML Expertise</p>
    <p><em>"Wo Technologie auf Kultur trifft" - Where Technology Meets Culture</em></p>
</div>
""", unsafe_allow_html=True)
