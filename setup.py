from setuptools import setup, find_packages


setup(
    name='orbelican',
    version='0.1.0',
    packages=find_packages(),
    sass_manifests={
        '.': {
            'sass_path': 'sass/themes',
            'css_path': 'static/css',
            'strip_extension': True,
        },
    },
    setup_requires=['libsass >= 0.20.0'],
    # project metadata
    description='A simple port of orbit-theme for Pelican to build your online resume',
    keywords='pelican pelican-theme orbit-theme resume cv',
    url='https://github.com/LucasVanHaaren/orbelican/')
