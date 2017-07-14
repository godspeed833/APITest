from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import request

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10 per minute", "1 per second"],
)
@app.route("/user")
@limiter.limit("3 per day")
def user():
    return "user"

@app.route("/anser")
def anser():
    return "anser"

@app.route("/admin")
@limiter.exempt
def admin():
    return 'admin'
     
if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True