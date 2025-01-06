import streamlit as st

def render_sidebar(news_items):
    st.sidebar.header("Recent News")
    
    for item in news_items:
        icon_color = {
            "promotion": "success",
            "publication": "primary"
        }.get(item['type'], "info")
        
        st.sidebar.markdown(
            f"""<div class="content-card">
                <i class="fas fa-{item['icon']} text-{icon_color}"></i>
                <strong>{item['date']}</strong><br/>
                {item['content']}
            </div>""",
            unsafe_allow_html=True
        )