def render_header(profile):
    return f"""
    <div class="header-container">
        <h1 class="header-title">{profile['name']}</h1>
        <h3>{profile['title']}</h3>
        <p>{profile['bio']}</p>
        
        <div class="contact-info">
            <a href="mailto:{profile['contact']['email']}">
                <i class="fas fa-envelope"></i> {profile['contact']['email']}
            </a>
            <a href="https://{profile['contact']['website']}" target="_blank">
                <i class="fas fa-globe"></i> {profile['contact']['website']}
            </a>
            <a href="https://twitter.com/{profile['contact']['twitter']}" target="_blank">
                <i class="fab fa-twitter"></i> {profile['contact']['twitter']}
            </a>
        </div>
    </div>
    """