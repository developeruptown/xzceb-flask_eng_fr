""" Translator Server """
import json
from flask import Flask, render_template, request
from machinetranslation import translator

translator= translator.Translator()

app = Flask("Web Translator",static_url_path='/static')

@app.route("/englishToFrench")
def englishToFrench():
    """English to French Translating route that takes @textToTranslate as parameter"""
    textToTranslate = request.args.get('textToTranslate')
    return translator.e2f_translator_function(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    """French to English Translating route that takes @textToTranslate as parameter"""
    textToTranslate = request.args.get('textToTranslate')
    return translator.f2e_translator_function(textToTranslate)

@app.route("/")
def renderIndexPage():
    """Root URl that return the main template file"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
