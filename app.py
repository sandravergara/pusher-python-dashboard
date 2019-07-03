from flask, render_template, request
from pusher import Pusher

app = Flask(__name__)

pusher = Pusher(
app_id = "814733",
key = "71198b6c72378c71016c",
secret = "2c0ab920339934fc784a",
cluster = "ap1",
ssl=True
)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('orders', method=['POST'])
def order():
    data = request.form
    pusher.trigger(u'order', u.place)