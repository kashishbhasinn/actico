import streamlit as st
from datetime import datetime

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
        color: black;
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
    .timeline-item {
        border-left: 3px solid #D4AF37;
        padding-left: 20px;
        margin: 15px 0;
        position: relative;
    }
    .timeline-item::before {
        content: '•';
        color: #D4AF37;
        font-size: 20px;
        position: absolute;
        left: -12px;
        top: 0;
    }
    .skill-bar {
        background-color: #f0f0f0;
        border-radius: 10px;
        overflow: hidden;
        margin: 5px 0;
    }
    .skill-fill {
        background: linear-gradient(90deg, #D4AF37, #B8860B);
        height: 25px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        padding-left: 10px;
        color: white;
        font-weight: bold;
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
st.sidebar.metric("Internships", "4+", "IIM Bangalore, DRDO, Dr. Oetker, Arogo AI IIT Kharagpur")

# Main content based on navigation
if current_section == "🏠 Home & Introduction":
    st.markdown('<h1 class="main-header">Kashish Bhasin</h1>', unsafe_allow_html=True)
    
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
    
    # Timeline visualization using HTML/CSS
    st.markdown("### 📅 German Journey Timeline")
    
    timeline_events = [
        ("June 1, 2019", "Flight to Hamburg via Zurich", "Cultural Immersion Begins - Unexpected stopover in beautiful Zurich"),
        ("June 2019", "PASCH Camp - Sankt Peter-Ording", "Quatschköpfer Group - B1.2 level with international peers"),
        ("July 2019", "B1.2 Certification Achievement", "Highest level certification in camp - Language mastery achieved"),
        ("August 2019", "Cultural Integration Complete", "Lifelong friendships formed with Vietnam, Thailand, Singapore peers"),
        ("2020-2021", "Continued German Excellence", "FIT 2 Topper → Dr. Oetker Internship opportunity")
    ]
    
    for date, event, impact in timeline_events:
        st.markdown(f"""
        <div class="timeline-item">
            <h4>{date}</h4>
            <h5>{event}</h5>
            <p>{impact}</p>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🎵 Cultural Highlights")
        st.write("**Favorite German Song:** *An der Nordseeküste*")
        st.write("**Camp Activities:** Werwolf, Baseball, Cultural Nights")
        st.write("**International Bonds:** Vietnam, Thailand, Singapore")
        st.write("**Achievement:** B1.2 Level - Highest in camp")
        st.write("**Special Memory:** Singing German songs together")
        st.write("**Roommates:** Haong Ha My (Vietnam) & Bharati (India)")
    
    with col2:
        st.markdown("### 🏆 German Achievements")
        st.markdown("""
        **2019 - PASCH Scholarship**  
        Cultural Exchange Program
        
        **2019 - B1.2 Certification**  
        Language Proficiency Excellence
        
        **2020 - German FIT 2 Topper**  
        Academic Achievement Recognition
        
        **2021 - Dr. Oetker Internship**  
        Professional German Connection
        """)
        
        st.markdown("### 🌍 Locations Visited")
        st.write("• **Hamburg** - K-Pop Street Play, Cultural exploration")
        st.write("• **Büsum** - Phanomania science center")
        st.write("• **Tönning** - Shopping and ice cream adventures")
        st.write("• **Westküstenpark** - Wildlife and nature")
        st.write("• **Nordsee beaches** - Unforgettable coastal experiences")

elif current_section == "🤖 AI/ML Journey":
    st.markdown('<h2 class="section-header">Artificial Intelligence & Machine Learning Expertise</h2>', unsafe_allow_html=True)
    
    # AI Journey progression using HTML progress bars
    st.markdown("### 🚀 AI/ML Learning Progression")
    
    learning_stages = [
        ("2020: German FIT 2 Victory", "Foundation in logical thinking and problem-solving", 20),
        ("2021: AWS DeepRacer Mastery", "Reinforcement learning and autonomous systems", 40),
        ("2022: Udacity AI Scholarship", "Comprehensive AI/ML curriculum completion", 60),
        ("2023: AISS Program at IIITD", "Advanced research in federated learning", 80),
        ("2024: Professional Applications", "Real-world implementation at IIM & DRDO", 100)
    ]
    
    for stage, description, progress_val in learning_stages:
        st.markdown(f"""
        <div style="margin: 20px 0;">
            <h4>{stage}</h4>
            <p>{description}</p>
            <div class="skill-bar">
                <div class="skill-fill" style="width: {progress_val}%">{progress_val}%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h4>🏆 AWS DeepRacer Achievement</h4>
            <p>Mastered reinforcement learning fundamentals through hands-on autonomous racing simulation, 
            developing deep understanding of reward functions and model optimization.</p>
            <ul>
                <li><strong>Reinforcement Learning:</strong> Q-learning, Policy gradients</li>
                <li><strong>Model Training:</strong> Hyperparameter optimization</li>
                <li><strong>Simulation:</strong> Virtual track navigation</li>
                <li><strong>Performance:</strong> Competitive racing algorithms</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🎓 Core Technical Skills")
        skills = [
            ("Machine Learning", 85),
            ("Deep Learning", 80),
            ("Python Programming", 90),
            ("Data Analysis", 85),
            ("Research Methodology", 75),
            ("AI Ethics", 70)
        ]
        
        for skill, level in skills:
            st.markdown(f"""
            <div style="margin: 10px 0;">
                <strong>{skill}</strong>
                <div class="skill-bar">
                    <div class="skill-fill" style="width: {level}%">{level}%</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h4>🔬 AISS 2023 Research Insights</h4>
            <p>Explored cutting-edge concepts in federated learning and coresets at IIITD's Artificial Intelligence Summer School, 
            recognizing the need for balanced AI research addressing both business and social dimensions.</p>
            <ul>
                <li><strong>Federated Learning:</strong> Distributed model training</li>
                <li><strong>Coresets:</strong> Efficient dataset representation</li>
                <li><strong>AI Ethics:</strong> Social impact considerations</li>
                <li><strong>Research Balance:</strong> Business vs. social applications</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🧠 Research Interests")
        st.write("• **Federated Learning**: Privacy-preserving distributed AI")
        st.write("• **Coresets**: Optimal dataset subset selection")
        st.write("• **AI Ethics**: Social and medical applications")
        st.write("• **Autonomous Systems**: Self-driving algorithms")
        st.write("• **Decision Making**: Automated business processes")
        st.write("• **Cross-cultural AI**: International perspectives")

elif current_section == "💼 Professional Experience":
    st.markdown('<h2 class="section-header">Professional Journey & Internships</h2>', unsafe_allow_html=True)
    
    # Experience cards with detailed information
    experiences = [
        {
            'company': 'Dr. Oetker',
            'role': 'Product Intern',
            'period': '12th Grade (2021)',
            'description': 'Secured prestigious product internship through Goethe Institute connections, applying German language skills and cultural understanding in professional setting. Worked on product development initiatives while experiencing German corporate culture firsthand.',
            'skills': ['Product Development', 'German Business Culture', 'Cross-cultural Communication', 'Project Management']
        },
        {
            'company': 'IIM (Indian Institute of Management)',
            'role': 'Research Intern',
            'period': 'Recent (2023)',
            'description': 'Conducted advanced research in management and technology intersection, developing analytical and strategic thinking capabilities. Focused on AI applications in business decision-making and organizational efficiency.',
            'skills': ['Research Methodology', 'Data Analysis', 'Strategic Thinking', 'Business Intelligence']
        },
        {
            'company': 'DRDO (Defense Research)',
            'role': 'Technical Intern',
            'period': 'Recent (2024)',
            'description': 'Contributed to defense technology research, applying AI/ML knowledge to critical national security applications. Worked on advanced algorithms and security protocols while maintaining highest confidentiality standards.',
            'skills': ['Defense Technology', 'AI Applications', 'Security Protocols', 'Algorithm Development']
        }
    ]
    
    for i, exp in enumerate(experiences):
        st.markdown(f"""
        <div class="highlight-box">
            <h3>🏢 {exp['company']} - {exp['role']}</h3>
            <p><strong>📅 Period:</strong> {exp['period']}</p>
            <p>{exp['description']}</p>
            
        </div>
        """, unsafe_allow_html=True)
        
        
        st.markdown(f"**🛠️ Skills Developed:** {', '.join(exp['skills'])}")
        st.markdown("---")
    
    # Professional development summary
    st.markdown("""
    <div class="highlight-box">
        <h3>💼 Professional Development Summary</h3>
        <p>My diverse internship portfolio demonstrates versatility across product development, research, and technology sectors. 
        The combination of German corporate experience at Dr. Oetker, academic research excellence at IIM, and cutting-edge 
        technology work at DRDO provides a unique foundation for contributing to Actico's innovative solutions.</p>
    </div>
    """, unsafe_allow_html=True)

elif current_section == "📝 Cover Letter":
    st.markdown('<h2 class="section-header">Cover Letter for Actico</h2>', unsafe_allow_html=True)
    
    # Interactive feedback section
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Proven Cultural Alignment with Germany", "8", "Authentic Connection")
        st.write("As a PASCH scholar with a B1.2 Goethe-Institut certification and internship experience at Dr. Oetker, I have developed a strong understanding of German work culture, communication norms, and professional etiquette. This foundation enables me to integrate seamlessly into Actico's international environment.")
    with col2:
        st.metric("Technical Expertise in AI & Decision Intelligence", "High", "Perfect Match")
        st.write("With hands-on experience in developing AI/ML systems—including a RAG system at DRDO and sentiment analysis pipelines—I bring deep technical skills that align with Actico’s focus on decision automation, intelligent software systems, and data-driven innovation.")
    with col3:
        st.metric("Cross-Cultural Collaboration & Global Perspective", "Strong", "Effective Global Teamwork")
        st.write("My background includes active engagement in international student exchanges, multilingual communication, and building bridges across diverse cultures. This enhances my ability to collaborate effectively within global teams and contribute to Actico’s culturally inclusive and client-focused mission.")

elif current_section == "🎯 Why Actico?":
    st.markdown('<h2 class="section-header">Why Actico is the Perfect Match</h2>', unsafe_allow_html=True)
    
    reasons = [
        {
            'title': '🇩🇪 German Team Culture Alignment',
            'description': 'My PASCH experience and cultural immersion have prepared me to seamlessly integrate with German work culture and communication styles. Having lived and learned in Germany, I understand the values of precision, collaboration, and innovation that drive German teams.',
        },
        {
            'title': '🤖 AI/ML Technical Expertise Match',
            'description': 'Actico\'s focus on intelligent decision management perfectly aligns with my expertise in AI/ML, federated learning, and ethical AI considerations. My background spans from theoretical research to practical applications.',
        },
        {
            'title': '🔄 Decision Automation Passion',
            'description': 'My research background and understanding of AI applications in business contexts align perfectly with Actico\'s automated decision-making solutions. I\'ve seen firsthand how intelligent systems can transform organizations.',
        },
        {
            'title': '🌟 Unique Value Proposition',
            'description': 'The combination of German cultural understanding, international perspective, and cutting-edge AI/ML skills creates a unique profile that can contribute to Actico\'s global vision while respecting German operational excellence.',
        }
    ]
    
    for reason in reasons:
        st.markdown(f"""
        <div class="highlight-box">
            <h3>{reason['title']}</h3>
            <p>{reason['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        
    # Final value proposition
    st.markdown("""
    <div class="highlight-box">
        <h3>🎯 My Commitment to Actico</h3>
        <p><strong>Immediate Contributions I Can Make:</strong></p>
        <ul>
            <li><strong>German Language Bridge:</strong> Seamless communication with German team members</li>
            <li><strong>Cultural Translator:</strong> Help bridge any international perspectives with German methodology</li>
            <li><strong>Technical Innovation:</strong> Apply cutting-edge AI/ML research to practical decision systems</li>
            <li><strong>Fresh Perspective:</strong> Bring international research insights to German precision</li>
            <li><strong>Rapid Integration:</strong> Pre-existing cultural understanding means faster onboarding</li>
        </ul>
        
    </div>
    """, unsafe_allow_html=True)
    
    # Final call to action
    st.markdown("""
    <div style="text-align: center; margin-top: 3rem; padding: 2rem; background: linear-gradient(135deg, #FFF8DC, #F5F5DC); border-radius: 15px; border: 2px solid #D4AF37;">
        <h2 style="color: #D4AF37; margin-bottom: 1rem;">Ready to Contribute to Actico's Success!</h2>
        <p style="font-size: 1.3rem; color: #8B4513; margin-bottom: 1rem;">
            <strong>"Wo deutsche Präzision auf globale Innovation trifft"</strong><br>
            <em>Where German Precision Meets Global Innovation</em>
        </p>
        <p style="font-size: 1.1rem; color: #8B4513;">
            Bringing together German cultural understanding, AI/ML technical expertise, 
            and international research perspective to drive intelligent automation forward.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #8B4513; padding: 1rem;">
    <p>🇩🇪 <strong>Erstellt mit Leidenschaft für Deutschland und Innovation</strong> • 🤖 <strong>Powered by AI/ML Expertise</strong></p>
    <p><em>"Von PASCH Scholar zu AI Professional - Eine Reise der kontinuierlichen Innovation"</em></p>
    <p><em>From PASCH Scholar to AI Professional - A Journey of Continuous Innovation</em></p>
</div>
""", unsafe_allow_html=True)
