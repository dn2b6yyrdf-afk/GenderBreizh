from flask import Flask, render_template

app = Flask(__name__)

TACHES_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQmCFj0BkD0VNzy7U27D-I3UR0Xak4Ox0CPVBJsD374ADIFeZPHYgYOa-vDYXT7IMs-Gq1gN64BMli9/pubhtml?gid=387754883&single=true"
FOURNITURES_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQmCFj0BkD0VNzy7U27D-I3UR0Xak4Ox0CPVBJsD374ADIFeZPHYgYOa-vDYXT7IMs-Gq1gN64BMli9/pubhtml?gid=0&single=true"

@app.route("/")
def taches():
    return render_template("taches.html", sheet_url=TACHES_URL)

@app.route("/fournitures")
def fournitures():
    return render_template("fournitures.html", sheet_url=FOURNITURES_URL)

if __name__ == "__main__":
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)