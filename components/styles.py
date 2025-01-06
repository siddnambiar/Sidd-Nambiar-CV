# components/styles.py
def get_styles(theme):
    return f"""
    <style>
        /* Global Styles */
        body {{
            font-family: {theme['fonts']['body']};
            color: {theme['colors']['text']};
            background: linear-gradient(
                135deg, 
                {theme['colors']['background']}, 
                white
            );
        }}

        /* Header Styles */
        .header-container {{
            background: {theme['colors']['card']};
            padding: {theme['spacing']['lg']};
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: {theme['spacing']['lg']};
        }}

        .header-title {{
            background: linear-gradient(
                45deg, 
                {theme['colors']['gradient']['start']}, 
                {theme['colors']['gradient']['end']}
            );
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: {theme['fonts']['heading']};
            font-size: 2.5rem;
            margin-bottom: {theme['spacing']['sm']};
        }}

        /* Card Styles */
        .content-card {{
            background: {theme['colors']['card']};
            border-radius: 10px;
            padding: {theme['spacing']['md']};
            margin-bottom: {theme['spacing']['md']};
            border-left: 4px solid {theme['colors']['primary']};
            transition: transform {theme['animations']['transition']};
        }}

        .content-card:hover {{
            transform: translateX(5px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }}

        /* Publication Card */
        .publication-card {{
            background: {theme['colors']['card']};
            padding: {theme['spacing']['md']};
            border-radius: 8px;
            margin-bottom: {theme['spacing']['sm']};
            border-left: 4px solid {theme['colors']['secondary']};
        }}

        /* Navigation */
        .nav-link {{
            color: {theme['colors']['text']};
            text-decoration: none;
            padding: {theme['spacing']['sm']};
            border-radius: 5px;
            transition: background-color {theme['animations']['transition']};
        }}

        .nav-link:hover {{
            background-color: {theme['colors']['primary']};
            color: white;
        }}

        /* Skills Section */
        .skills-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: {theme['spacing']['md']};
        }}

        .skill-card {{
            background: {theme['colors']['card']};
            padding: {theme['spacing']['md']};
            border-radius: 8px;
            border-top: 4px solid {theme['colors']['accent']};
        }}
    </style>
    """