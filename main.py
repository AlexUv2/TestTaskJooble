from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import string
from random import choices


#TODO: Убрать проверку в шаблоне.


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///links.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    full_url = db.Column(db.String(150), nullable=False, unique=True)
    short_url = db.Column(db.String(30), unique=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    time_life = db.Column(db.Integer, default=90)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def generate_short_url(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=6))

        url = self.query.filter_by(short_url=short_url).first()

        if url:
            return self.generate_short_url()
        return short_url

    def __repr__(self):
        return f'{self.id}, {self.short_url}'
        # return f'id:{self.id}, fullUrl:{self.full_url}, shtUrl:{self.short_url}, crtime:{self.create_time}, lftime:{self.time_life}'


@app.route('/')
def index():
    check_links()
    return render_template('index.html')


@app.route('/create-link', methods=['GET', 'POST'])
def create_link():
    check_links()
    if request.method == 'POST':
        full_url = request.form['full_url']
        time_life = request.form['time_life']

        link = Links(full_url=full_url, time_life=time_life)

        try:
            db.session.add(link)
            db.session.commit()
            return redirect("/links")
        except:
            return ('Wrong values')
    else:
        return render_template('create_link.html')


@app.route('/links/')
def links_list():
    check_links()
    links = Links.query.order_by(Links.create_time.desc()).all()
    return render_template('links.html', links=links, timedelta=timedelta, datetime=datetime)


@app.route('/links/<int:id>')
def link_detail(id):
    check_links()
    link = Links.query.get_or_404(id)
    active_until = link.create_time + timedelta(days=link.time_life)
    return render_template('links-detail.html', link=link, active_untill=active_until)


@app.route('/links/<string:short_url>')
def redirect_to_url(short_url):
    check_links()
    link = Links.query.filter_by(short_url=short_url).first_or_404()
    return redirect(link.full_url)


@app.route('/links/<int:id>/del')
def link_delete(id):
    check_links()
    link = Links.query.get_or_404(id)
    try:
        db.session.delete(link)
        db.session.commit()
        return redirect('/links')
    except:
        return 'Can\'t delete it'

#
# @app.errorhandler(404)
# def link_not_found():  # !!!!!!!!!!!!!РАЗОБРАТЬСЯ ПОЧЕУ НЕ РАБОТАЕТ!!!!!!!!!!!!
#     return 'No such links', 404


def check_links():
    links = Links.query.all()
    for link in links:
        if link.create_time + timedelta(days=link.time_life) < datetime.utcnow():
            db.session.delete(link)
            db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
