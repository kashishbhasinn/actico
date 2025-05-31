import streamlit as st

# Sidebar navigation and progress tracking
st.sidebar.title("Navigation & Progress Tracking")
sections = ["Introduction", "Internships", "Projects", "What I Bring to the Table", "Why Actico", "Achievements", "Contact & CTA"]

# Track progress (marks viewed sections)
viewed_sections = {
    "Introduction": False,
    "Internships": False,
    "Projects": False,
    "What I Bring to the Table": False,
    "Why Actico": False,
    "Achievements": False,
    "Contact & CTA": False
}

# Sidebar radio button for navigation
section = st.sidebar.radio("Go to", sections)

# Track progress based on section view
viewed_sections[section] = True
progress_percentage = sum(viewed_sections.values()) / len(viewed_sections) * 100

# Progress bar
st.sidebar.progress(progress_percentage / 100)

# Main Content
st.title("🇩🇪 Kashish's Internship Portfolio – Actico Edition")

if section == "Introduction":
    st.header("👋 Willkommen! – Introduction")
    st.markdown("""
    Hello! I'm Kashish, a passionate tech enthusiast with a love for cultural experiences. My journey in tech began with my first exposure to Germany in 2019, and 
    since then, I have focused on honing my skills in AI, ML, and product development. With internships at organizations like DRDO and Dr. Oetker, and a deep dive 
    into the world of AI, I aim to bring creativity and technical precision to every challenge.
    """)

elif section == "Internships":
    st.header("💼 Internships")
    st.markdown("""
    **🔬 DRDO – Summer Research Intern (AI)**  
    During my time at DRDO, I worked on building a Retrieval-Augmented Generation (RAG) system using LangChain, ChromaDB, and HuggingFaceEmbeddings. I also presented 
    insights on vector databases like FAISS, Pinecone, and Vespa, collaborating with the LLM team to improve operational efficiency.

    **📈 IIM Research Internship**  
    Worked on market analysis, behavioral data exploration, and business insights development, contributing to key strategic decisions.

    **🛒 Dr. Oetker Product Internship**  
    A product-based internship with one of Germany's leading FMCG brands. I contributed to research and strategy, building a deeper understanding of product workflows.
    """)

elif section == "Projects":
    st.header("🚀 Projects")
    st.markdown("""
    **1. Consumer Attitudes Toward Data Privacy in Social Media Marketing**  
    A data-driven project analyzing user concerns regarding data collection and privacy breaches. Using MS Excel and Power BI, I identified trends and patterns in user behavior.

    **2. Sensitivity Analysis Using MS Excel**  
    I conducted sensitivity analysis for a toy company to evaluate the impact of changing variables on profit margins, providing strategic recommendations for product pricing.

    **3. Profitability Enhancement Strategy**  
    A business case study using the MECE principle to enhance profitability for a multinational technology company.

    **4. AI-Driven Sentiment Analysis API**  
    Building a sentiment analysis API for reviews, comments, and social media posts, with a focus on deployment using Flask and AWS SageMaker.
    """)

elif section == "What I Bring to the Table":
    st.header("💡 What I Bring to the Table")
    st.markdown("""
    - **AI & ML Expertise**: Extensive experience in building AI systems, including sentiment analysis, image recognition, and NLP models.
    - **Cross-Cultural Awareness**: A strong connection to Germany through my time at Goethe PASCH Youth Camps, which enhanced my intercultural communication skills.
    - **Problem-Solving**: A keen interest in tackling complex problems with creative solutions, as demonstrated in my research and internship experiences.
    - **Hands-On Experience**: Real-world experience in deploying machine learning models and building end-to-end solutions for various projects.
    """)

elif section == "Why Actico":
    st.header("🎯 Why Actico?")
    st.markdown("""
    Actico’s focus on cutting-edge technology and data analytics aligns perfectly with my passion for creating innovative solutions.  
    My diverse technical background, combined with my cross-cultural experiences, positions me uniquely to contribute to Actico’s mission.  
    I'm eager to leverage my skills in AI, machine learning, and data-driven decision-making to help Actico deliver high-impact solutions for clients.
    """)

elif section == "Achievements":
    st.header("🏆 Achievements")
    st.markdown("""
    **1. Top Performer – FIT 2 German Exam**: I topped the Goethe Institute's FIT 2 German exam in 2019, showcasing my commitment to learning and cultural engagement.
    
    **2. AWS DeepRacer Program Graduate**: Completed the AWS DeepRacer program and gained foundational knowledge in AI and reinforcement learning.

    **3. Dr. Oetker Internship Award**: Awarded a product internship at Dr. Oetker during my 12th grade, where I gained valuable product development and marketing insights.

    **4. AI Summer School @ IIIT Delhi**: Participated in the AI Summer School 2023, learning advanced concepts like federated learning and coresets.

    **5. Research Internships at DRDO and IIM**: Gained hands-on experience in AI, machine learning, market research, and data analysis during internships at DRDO and IIM.
    """)

elif section == "Contact & CTA":
    st.header("📞 Contact & CTA")
    st.markdown("""
    If you're interested in collaborating with me or learning more about my work, feel free to reach out!

    **Email**: [your_email@example.com]  
    **LinkedIn**: [linkedin.com/in/your-profile]  
    **GitHub**: [github.com/your-profile]  

    *Let’s connect and create something amazing together!*
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Crafted with ❤️ by Techie Barbie")

