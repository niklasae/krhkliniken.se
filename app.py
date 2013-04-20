from flask import Flask
from flask import render_template

from flask.ext.assets import Bundle
from flask.ext.assets import Environment

from flask_flatpages import FlatPages

app = Flask(__name__)


# ~~~ CONFIG ~~~
app.config.from_pyfile('settings.cfg')


# ~~~ PAGES ~~~
pages = FlatPages(app)


# ~~~ ASSETS ~~~
app.config['ASSETS_DEBUG'] = True
app.config['COFFEE_NO_BARE'] = True  # webassets doc says the opposite...
assets = Environment(app)

# COFFEESCRIPT & JAVASCRIPT
js = Bundle(
    # coffeescripts
    Bundle('dynamic/*.coffee', filters='coffeescript', output='generated/krh.coffee.%(version)s.js', debug=False),
    filters=('jsmin', 'jspacker'),
    output='generated/krh.coffee.%(version)s.min.js')
# Add minified js to register below
assets.register('all_js', js, 'js/libs/bootstrap.min.js', 'js/libs/less-1.3.3.min.js')

# FIXME: Sort out the less stuff, so it's nicer
# LESS
# https://github.com/miracle2k/webassets/pull/131
# Due to a bug in webassets, we wil run into problems with less files not being updated properly.
# TODO:
#   1. Upgrade to latest webassets/Flask-Assets (0.8?)
#   2. Remove js/less-X.X.X.min.js
#   2. Add to CSS section below
#   3. Test a update
# Until then, we'll have to use less.js and debug=True
# less = Bundle('dynamic/*.less', filters='less', output='gen/krh.less.%(version)s.css', debug=True)
# assets.register('all_less', less)

css = Bundle('generated/*.css')
assets.register('all_css', css)


# ~~~ BASE HELPER ~~~


def base_template_renderer(template, page):
    base = pages.get('base')
    return render_template(template, base=base, page=page)


# ~~~ ROUTES ~~~
@app.route("/")
def index():
    page = pages.get_or_404('index')
    return base_template_renderer('index.html', page=page)


@app.route('/om-oss/')
def about():
    page = pages.get_or_404('about')
    return base_template_renderer('about.html', page=page)


@app.route('/om-kiropraktik/')
def info():
    page = pages.get_or_404('info')
    return base_template_renderer('info.html', page=page)


@app.route('/priser/')
def prices():
    page = pages.get_or_404('prices')
    return base_template_renderer('prices.html', page=page)


@app.route('/akuta-behandlingar/')
def emergency():
    page = pages.get_or_404('emergency')
    return base_template_renderer('emergency.html', page=page)


@app.route('/vanliga-fragor/')
def faq():
    page = pages.get_or_404('faq')
    return base_template_renderer('faq.html', page=page)


@app.route('/kontakt/')
def contact():
    page = pages.get_or_404('contact')
    return base_template_renderer('contact.html', page=page)


@app.route('/boka/')
def book():
    page = pages.get_or_404('book')
    return base_template_renderer('book.html', page=page)


@app.route('/style.css')
def compressed_css():
    return '/* ... */', 200, {'Content-Type': 'text/css; charset=utf-8'}
