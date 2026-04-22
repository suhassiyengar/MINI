from flask import Flask, request, render_template_string
import threading
import controller

app = Flask(__name__)

HTML = """
<h1>Remote Device Control</h1>

<form method="POST">
    <button name="cmd" value="OPEN_GOOGLE">Open Google</button>
    <button name="cmd" value="OPEN_YOUTUBE">Open YouTube</button>
    <button name="cmd" value="STATUS">Check Status</button>
</form>

<h3>Response:</h3>
<p>{{result}}</p>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        cmd = request.form["cmd"]
        result = controller.send_command(cmd)

    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    threading.Thread(target=controller.start_server, daemon=True).start()
    app.run(port=8000)