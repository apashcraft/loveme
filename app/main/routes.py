from flask import render_template

from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')


@bp.route('/nhd-kent-de')
def nhd_map():
    return render_template('nhd_map.html')
