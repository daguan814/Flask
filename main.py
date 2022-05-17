from app import app

if __name__ == "__main__":
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host='127.0.0.1', port=4070, debug=False)
