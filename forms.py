# coding: utf-8

from flask.ext.wtf import Form
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import Required, Regexp, ValidationError

def validate_prime(form, field):
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
        
    if gcd(int(field.data), 26) != 1:
        raise ValidationError(u"k2需与26互质") 

class ClassicCryptForm(Form):
    text = TextAreaField(u"请输入原文(仅限英文)")
    cipher = TextAreaField(u"请输入密文(仅限英文)")
    key1 = StringField(u"请输入密钥k1", validators=[Required(),
                            Regexp(r"^[0123456789]+$", message=u"请输入整数")])
    key2 = StringField(u"请输入密钥k2", validators=[Required(),
                            Regexp(r"^[0123456789]+$", message=u"请输入整数"),
                            validate_prime])
    encrypt = SubmitField(u"加密")
    decrypt = SubmitField(u"解密")
    stat = SubmitField(u"统计")

class AESCryptForm(Form):
    text = TextAreaField(u"请输入原文")
    cipher = TextAreaField(u"请输入密文")
    key = StringField(u"请输入密钥", validators=[Required()])
    encrypt = SubmitField(u"加密")
    decrypt = SubmitField(u"解密") 

