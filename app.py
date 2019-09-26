from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

app = Flask(__name__)


# playlists = [
#    {'title': 'Cat Videos', 'description': 'Cats acting weird'},
#    {'title': '80\'s Music', 'description': 'Don\'t stop believing!'},
#    {'title': 'Rap Music', 'description': 'HYPHY!'}
# ]

@app.route("/")
def playlists_index():
    return render_template(
        "playlists_index.html",
        playlists=playlists.find()
    )


if __name__ == "__main__":
    app.run(debug=True)
