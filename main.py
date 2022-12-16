from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route("/")
def index():
  items = load_candidates_from_json()
  return render_template('list.html', items=items)


@app.route("/candidate/<int:candidate_id>")
def get_candidate_by_id(candidate_id):
    item = get_candidate(candidate_id)
    return render_template('single.html', item=item)


@app.route("/search/<candidate_name>")
def get_candidate_by_name(candidate_name):
    items = get_candidates_by_name(candidate_name)
    return render_template('search.html', items=items)


@app.route("/skill/<skill_name>")
def get_candidate_by_skill(skill_name):
    skill = skill_name
    items = get_candidates_by_skill(skill_name)
    return render_template('skill.html', items=items, skill=skill)


if __name__ == '__main__':
    app.run(debug=True)
