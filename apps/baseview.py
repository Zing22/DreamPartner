# -*- coding=utf-8 -*-
from flask import Flask, render_template, url_for
from apps import app

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',title="404"), 404

@app.route('/')
@app.route('/apps')
def index():
	return render_template('index.html',title="Apps Index")
