# coding: utf-8

import os
from flask import Flask, render_template, request, url_for, abort
from flask.ext.bootstrap import Bootstrap

from config import config
from forms import *
from form_exec import *
import cryptlib

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config.from_object(config[os.getenv("FLASK_CONFIG") or "default"])

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/crypt/<crypt_type>", methods=["GET", "POST"])
def crypt(crypt_type):
    crypt_forms = {
        "classic": ClassicCryptForm,
        "des": DESCryptForm,
        "rsa": RSACryptForm,
    }
    subtitles = {
        "classic": u"古典加密——仿射密码",
        "des": u"DES加密",
        "rsa": u"RSA加密",
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

@app.route("/prime_test", methods=["POST"])
def prime_test():
    from cryptlib.RSA import is_prime
    try:
        number = int(request.form["number"])
        times = int(request.form["times"])
    except ValueError:
        abort(400)
    return str(is_prime(number, times))


if __name__ == "__main__":
    app.run()
