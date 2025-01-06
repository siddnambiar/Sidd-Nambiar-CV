import streamlit as st
import pandas as pd
from config.theme import THEME
from config.data import PortfolioData

def init_page():
    st.set_page_config(page_title="Portfolio", layout="wide")
    st.markdown('''
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    ''', unsafe_allow_html=True)

def render_header():
    st.markdown('''
        <div class="header">
            <h1>Siddhartha Nambiar, PhD</h1>
            <h3>Senior Lead Data Scientist & Operations Research Expert</h3>
            <p>Specializing in healthcare analytics, supply chain modeling, and operational efficiency optimization.</p>
            <div class="contact-info">
                <a href="mailto:SiddharthaNambiar@Gmail.Com">
                    <i class="fas fa-envelope"></i> SiddharthaNambiar@Gmail.Com
                </a>
                <a href="https://www.snambiar.com" target="_blank">
                    <i class="fas fa-globe"></i> www.snambiar.com
                </a>
                <a href="https://twitter.com/@SiddNambiar" target="_blank">
                    <i class="fab fa-twitter"></i> @SiddNambiar
                </a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

def render_sidebar(news):
    st.sidebar.header("Navigate to")
    sections = ["Experience", "Publications", "Research Portfolio", "Technical Skills", "Education"]
    selection = st.sidebar.radio("", sections)
    
    st.sidebar.header("Recent News")
    for item in news:
        st.sidebar.markdown(f'''
            <div class="news-card">
                <i class="fas fa-{item['icon']}"></i>
                <strong>{item['date']}</strong><br/>
                {item['content']}
            </div>
        ''', unsafe_allow_html=True)
    
    return selection

def render_experience(experiences):
    st.header("Professional Experience")
    for exp in experiences:
        content = f"""
        <div style="background: white; padding: 1.5rem; border-radius: 8px; 
                    border-left: 4px solid #4A90E2; margin: 1rem 0;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h4 style="margin-top:0">{exp['title']} at {exp['company']}</h4>
            <strong>{exp['period']}</strong>
            {''.join(f"<p style='margin:0.5rem 0'>• {point}</p>" for point in exp['points'])}
        </div>
        """
        st.markdown(content, unsafe_allow_html=True)

def render_publications(publications):
    st.header("Research Publications")
    years = sorted(publications['Year'].unique(), reverse=True)
    selected_year = st.selectbox("Filter by Year", years)
    filtered_pubs = publications[publications['Year'] == selected_year]
    
    for _, pub in filtered_pubs.iterrows():
        link_html = f'<a href="{pub["Link"]}" target="_blank">Link</a>' if pub["Link"] else ""
        st.markdown(f'''
            <div class="publication-card">
                <h4>{pub['Title']}</h4>
                <p><strong>Authors:</strong> {pub['Authors']}</p>
                <p><strong>Journal:</strong> {pub['Journal']} ({pub['Year']}) {link_html}</p>
                <p><strong>Abstract:</strong> {pub['Abstract']}</p>
            </div>
        ''', unsafe_allow_html=True)


def render_research(portfolio):
    st.header("Featured Research Projects")
    for project in portfolio:
        content = f"""
        <div style="background: white; padding: 1.5rem; border-radius: 8px; 
                    border-left: 4px solid #FF6B6B; margin: 1rem 0;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h4 style="margin-top:0">{project['title']}</h4>
            <strong>{project['period']}</strong>
            <p>{project['description']}</p>
            {''.join(f"<p>• {point}</p>" for point in project['highlights'])}
        </div>
        """
        st.markdown(content, unsafe_allow_html=True)

def render_skills(skills):
    st.header("Technical Skills")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Core Technologies")
        for skill in skills['core']:
            st.markdown(f"• **{skill['category']}:** {skill['items']}")
    
    with col2:
        st.subheader("Methodologies")
        for method in skills['methodologies']:
            st.markdown(f"• **{method['category']}:** {method['items']}")

def render_education(education):
    st.header("Education")
    
    for degree in education['degrees']:
        content = f"""
        <div style="background: white; padding: 1.5rem; border-radius: 8px; 
                    border-left: 4px solid #6C63FF; margin: 1rem 0;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h4 style="margin-top:0">{degree['title']}</h4>
            <p><strong>{degree['institution']}</strong> ({degree['year']})</p>
            {f"<p><em>{degree['thesis']}</em></p>" if degree.get('thesis') else ''}
            {f"<p>Advisor: {degree['advisor']}</p>" if degree.get('advisor') else ''}
        </div>
        """
        st.markdown(content, unsafe_allow_html=True)

    
def apply_styles():
    st.markdown('''
        <style>
            .header {
                position: sticky;
                top: 0;
                z-index: 100;
                background: white;
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                margin-bottom: 2rem;
            }
            .header h1 {
                background: linear-gradient(45deg, #4A90E2, #50E3C2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: 'Poppins', sans-serif;
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            .contact-info {
                display: flex;
                gap: 1rem;
                align-items: center;
                margin-top: 1rem;
            }
            .contact-info a {
                display: flex;
                align-items: center;
                gap: 0.5rem;
                color: #2C3E50;
                text-decoration: none;
                transition: color 0.3s;
            }
            .contact-info a:hover {
                color: #4A90E2;
            }
            .news-card {
                background: white;
                padding: 1rem;
                border-radius: 8px;
                margin-bottom: 1rem;
                border-left: 4px solid #4A90E2;
            }
            .publication-card {
                background: white;
                padding: 1.5rem;
                border-radius: 8px;
                margin-bottom: 1rem;
                border-left: 4px solid #50E3C2;
            }
        </style>
    ''', unsafe_allow_html=True)

def main():
    init_page()
    apply_styles()
    
    data = PortfolioData()
    render_header()
    
    selection = render_sidebar(data.get_news())
    
    if selection == "Experience":
        render_experience(data.get_experience())
    elif selection == "Publications":
        render_publications(data.get_publications())
    elif selection == "Research Portfolio":
        render_research(data.get_research_portfolio())
    elif selection == "Technical Skills":
        render_skills(data.get_skills())
    elif selection == "Education":
        render_education(data.get_education())

if __name__ == "__main__":
    main()