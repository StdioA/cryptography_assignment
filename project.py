# coding: utf-8

import re
from flask import Flask, render_template, request, url_for
from flask.ext.bootstrap import Bootstrap

from forms import *
from form_exec import *
import cryptlib

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config["SECRET_KEY"] = "WTForm is What-The-F**k-form"
app.config["BOOTSTRAP_SERVE_LOCAL"] = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/crypt/<crypt_type>", methods=["GET", "POST"])
def crypt(crypt_type):
    crypt_forms = {
        "classic": ClassicCryptForm,
        "des": DESCryptForm,
    }
    subtitles = {
        "classic": u"古典加密——仿射密码",
        "des": u"DES加密",
    }
    
    form = (crypt_forms[crypt_type])()                                          # 对提交的表单进行处理（如加密）
    other_params = {}

    if request.method == "POST":
        if form.validate_on_submit():
            form, other_params = exec_form(crypt_type, form)

    return render_template(crypt_type+"_crypt.html", 
                        form=form,
                        subtitle=subtitles[crypt_type],
                        **other_params)

if __name__ == "__main__":
    app.run(debug=True)
