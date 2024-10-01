from flask import Flask, render_template, redirect, url_for, request, session
from flask_login import login_required, current_user

app = Flask(__name__)

@app.route('/account_integration', methods=["GET"])
@login_required
def account_integration():
    """Render the account integration page."""
    # Check if the user has allready connected their accounts
    tiktok_connected = current_user.tiktok_token is not None
    instagram_connected = current_user.instagram_token is not None
    youtube_connected = current_user.youtube_token is not None

    return render_template(
        "account_integration.html",
        tiktok_connected = tiktok_connected,
        instagram_connected = instagram_connected,
        youtube_connected = youtube_connected
    )

@app.route('/connect_tiktok', methods=['GET'])
@login_required
def connect_tiktok():
    """Redirect the user to TikTok's OAuth page for authentification."""
    tiktok_auth_url = get_tiktok_auth_url()
    return redirect( tiktok_auth_url)

@app.route('/connect_instagram', methods=['GET'])
@login_required
def connect_instagram():
    """Redirect the user to Instagrams's OAuth page for authentification."""
    instagram_auth_url = get_instagram_auth_url()
    return redirect( instagram_auth_url)

@app.route('/connect_youtube', methods=['GET'])
@login_required
def connect_youtube():
    """Redirect the user to Youtube's OAuth page for authentification."""
    youtube_auth_url = get_youtube_auth_url()
    return redirect( youtube_auth_url)

def get_tiktok_auth_url():
    """Generate the TikTok OAuth URL."""
    return "https://www.tiktok.com/auth?client_id=YOUR_CLIENT_ID&redirect_uri={REDIRECT_URI}&response_type=code"

def get_instagram_auth_url():
    """Generate the Instagram OAuth Url"""
    return

def get_youtube_auth_url():
    """Generate the Youtube OAuth URL"""
    return 


@app.route('/')
def home():
    message = "This is rendered from Flask!"
    return render_template('account_integration.html', message=message)
if __name__ == '__main__':
    app.run(debug=True)
