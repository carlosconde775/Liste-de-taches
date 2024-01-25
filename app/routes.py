from flask import Blueprint, redirect, render_template, request, url_for

main_bp = Blueprint('main', __name__)

tasks = []  # Lista para almacenar tareas
completed_tasks = []  # Lista para almacenar tareas completadas


@main_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html', tasks=tasks, completed_tasks=completed_tasks)

@main_bp.route('/', methods=['POST'])
def add_task():
    new_task = request.form.get('task')
    if new_task:
        tasks.append({'text': new_task, 'completed': False})
    return render_template('index.html', tasks=tasks)

@main_bp.route('/complete/<int:task_index>', methods=['POST'])
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
    return redirect(url_for('main.index'))

@main_bp.route('/delete/<int:task_index>', methods=['POST'])
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for('main.index'))