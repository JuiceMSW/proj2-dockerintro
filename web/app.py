from flask import Flask
from flask import *

import os.path

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!"


@app.route("/<string:name>")
def file(name):
	if os.path.isfile("./templates/" + name):
		return render_template(name), 200
	elif "~" in name or "//" in name or ".." in name or name.find(".html") == -1 and name.find(".css") == -1:
		abort(403)
	else:
		abort(404)
	# elif "~" in name or "//" in name or ".." in name:
	# 	return render_template("403.html"), 403
	# else:
	# 	return render_template("404.html"), 404

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.errorhandler(403)
def forbidden(e):
	return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
