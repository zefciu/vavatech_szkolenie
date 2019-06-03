import functools as ft
import invoke

DIRS = [
    'lekcja1',
    'lekcja2',
    'lekcja3',
    'lekcja4',
]


def split_filename(fname):
    bits = fname.rsplit('.', 1)
    if len(bits) == 1:
        return bits[0], ''
    return bits


def task_by_dirs(task):
    @ft.wraps(task)
    def result(ctx):
        for directory in DIRS:
            with ctx.cd(directory):
                task(ctx)
    return result


def listdir(ctx, pattern):
    try:
        result = ctx.run(f'ls {pattern}', hide=True)
    except invoke.exceptions.UnexpectedExit:
        return
    for line in result.stdout.split('\n'):
        if line:
            yield line


@invoke.task
@task_by_dirs
def styles(ctx):
    ctx.run('pygmentize -S manni -f latex > styles.tex')


def pygmentize_factory(filetype):
    def pygmentize(ctx):
        for f in listdir(ctx, f'*.{filetype}'):
            filename, extension = split_filename(f)
            ctx.run(
                f'pygmentize -l {extension} -o {filename}.tex '
                f'{filename}.{extension}'
            )
    pygmentize.__name__ = 'pygmentize_' + filetype
    return pygmentize


pygmentize_pycon = invoke.tasks.Task(task_by_dirs(pygmentize_factory('pycon')))
pygmentize_py = invoke.tasks.Task(task_by_dirs(pygmentize_factory('py')))
pygmentize_bash = invoke.tasks.Task(task_by_dirs(pygmentize_factory('bash')))


@invoke.task(styles, pygmentize_pycon, pygmentize_py, pygmentize_bash)
@task_by_dirs
def make_slides(ctx):
    for f in listdir(ctx, '*.latex'):
        filename, extension = split_filename(f)
        if extension == 'latex':
            ctx.run('latex -output-format pdf {}'.format(f))
