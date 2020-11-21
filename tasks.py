from os import environ
from pathlib import Path
from invoke import task
from sass import compile as sass_compile


def get_venv():
    """Return virtual environment path or throw an error if not found"""
    env = environ.get("VIRTUAL_ENV", None)
    if env:
        return Path(env)
    else:
        raise EnvironmentError("No virtual environment found.")


PKG_NAME = "orbelican"
PKG_PATH = Path(f"pelican/themes/{PKG_NAME}")
VENV_PATH = get_venv()
VENV = str(VENV_PATH.expanduser())

SASS_SRC = PKG_PATH.joinpath("sass").joinpath("themes")
SASS_DEST = PKG_PATH.joinpath("static").joinpath("css")


@task
def sass(c, compress=False):
    """Compile sass files"""
    style = "expanded"
    if compress:
        style = "compressed"
    sass_compile(dirname=(SASS_SRC, SASS_DEST), output_style=style)

@task
def clean(c, dist=False, build=False, css=False):
    """Clean build directories"""
    patterns = []
    if dist:
        patterns.append("dist/")
    if build:
        patterns.append("build/")
    if css:
        patterns.append(SASS_DEST)

    for p in patterns:
        c.run(f"rm -rf {p}")


@task()
def build(c, source=False, wheel=False, egg=False):
    """Build source and wheel package"""
    SF, WF, EF = "", "", ""
    if source:
        SF = "sdist"
    if wheel:
        WF = "bdist_wheel"
    if egg:
        WF = "bdist_egg"
    if source or wheel or egg:
        clean(c, dist=True, build=True, css=True)
        sass(c, compress=True)
        return c.run(f"python setup.py {SF} {WF} {EF}", hide=True, warn=True)


@task
def buildcheck(c):
    """Check if builds are OK"""
    return c.run("twine check dist/*")


@task
def publish(c, prod=False):
    """Publish package on PyPI"""
    build_res = build(c, source=True, wheel=True)
    if build_res.ok:
        build_check_res = buildcheck(c)
        if build_check_res.ok:
            if prod:
                c.run("twine upload dist/*")
            else:
                c.run("twine upload -r testpypi dist/*")