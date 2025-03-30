from flask import Flask, render_template, url_for

app = Flask(__name__)

about_info = {
    'name': 'Кужель  Владислав',
    'description': 'Студент 4го курсу ркеб '
                   'навчаюсь на спеціальності - інженерія програмного забезпечення',
    'email': 'kvladyslav@gmail.com',
    'git': 'https://github.com/Kuzhell',
}

education_info = [
    {
        'degree': 'закінчені 9 класів школи',
        'university': 'НВК12',
        'year': '2021',
        'description': 'загальна середня освіта.'
    },
]

projects_data = [
    {
        'id': 'project1',
        'title': 'Лабораторна робота 9 з дисципліни дата інженерія ',
        'image': 'static/323.png',
        'repo_url': 'https://github.com/Kuzhell/data-engeniring/blob/main/9.py'
    },
]

@app.route('/')
def index():
    return render_template('index.html', about=about_info)

@app.route('/about')
def about():
    return render_template('about.html', about=about_info)

@app.route('/education')
def education():
    return render_template('education.html', education=education_info, about=about_info)

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=projects_data, about=about_info)

@app.route('/projects/<project_id>')
def project(project_id):
    project = next((p for p in projects_data if p['id'] == project_id), None)
    if project:
        return render_template('project_template.html', project=project, about=about_info)
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)