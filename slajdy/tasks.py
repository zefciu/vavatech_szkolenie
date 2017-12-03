import os
import invoke

FILES = os.listdir()

def split_filename(fname):
    bits = fname.rsplit('.', 1)
    if len(bits) == 1:
        return bits[0], ''
    return bits

@invoke.task
def styles(ctx):
    ctx.run('pygmentize -S manni -f latex > styles.tex')

def pygmentize_factory(filetype):
    def pygmentize(ctx):
        for f in FILES:
            filename, extension = split_filename(f)
            if extension == filetype:
                ctx.run(
                    'pygmentize -l {extension} -o {filename}.tex {filename}.{extension}'.format(
                        extension=extension,
                        filename=filename,
                    )
                )
    pygmentize.__name__ = 'pygmentize_' + filetype
    return pygmentize

pygmentize_pycon = invoke.tasks.Task(pygmentize_factory('pycon'))
pygmentize_py = invoke.tasks.Task(pygmentize_factory('py'))
pygmentize_bash = invoke.tasks.Task(pygmentize_factory('bash'))

@invoke.task(styles, pygmentize_pycon, pygmentize_py, pygmentize_bash)
def make_slides(ctx):
    for f in FILES:
        filename, extension = split_filename(f)
        if extension == 'latex':
            ctx.run('latex -output-format pdf {}'.format(f))
