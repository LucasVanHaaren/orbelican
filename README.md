# orbelican

A simple port of [**orbit-theme**](https://github.com/xriley/Orbit-Theme) for the [**Pelican**](https://github.com/getpelican/pelican) static site generator to build your online resume

## Getting started

### Configuration

To avoid problems make sure these configuration variables are filled in `pelicanconf.py`

```python
THEME = "orbelican"

AUTHOR = ''
SITENAME = ''
SITEURL = ''
TIMEZONE = ''
DEFAULT_LANG = ''

PATH = "" # leave this variable empty, there is no content to look for (except data files)
ARTICLE_EXCLUDES = [".env"] # exclude your venv

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# set all these variables on false, because we only want to generate index.html
DEFAULT_PAGINATION = False
LOAD_CONTENT_CACHE = False
TAGS_SAVE_AS = False
AUTHORS_SAVE_AS = False
CATEGORIES_SAVE_AS = False
ARCHIVES_SAVE_AS = False
```

### Customization

#### Data

This theme support [**pelican-data-files**](https://github.com/LucasVanHaaren/pelican-data-files) plugin.

> This plugin loads all the data files found in the project's data/ directory, and makes them accessible [...]

First, fetch theme's sample data with the following command:

```bash
pelican-data-files --fetch orbelican
```

A `data/` folder must have been created, you can modify these files in order to personalize the site.

#### Add custom profile picture and favicon

Copy your best profile picture in your site project in `images/` folder and edit the `config.json` to set proper filename to `profile` attribute. Do the same for customize your favicon.

### Generate your website

You can generate the site with the simple command:

```bash
pelican
```

**Note:** you can also easily serve the site by running the following command:

```bash
pelican -l
```

## Contributing

To build css files from sass, run the task `sass`:

```bash
invoke sass
```

**Note:** make sure you have installed dev dependencies.

## License

>This Bootstrap template [...] is 100% FREE as long as you keep the footer attribution link.

This is a port of [**orbit-theme**](https://github.com/xriley/Orbit-Theme) for Pelican, it can be used for free if you keep the footer attribution link.

>If you'd like to use the template without the attribution link, you can [buy the commercial license](https://themes.3rdwavemedia.com/bootstrap-templates/resume/orbit-free-resume-cv-bootstrap-theme-for-developers/) via the theme website

If you have paid for the license you can hide the footer by setting the configuration variable `SHOW_FOOTER = True` in your `pelicanconf.py`

The above quotes come from the [original theme](https://github.com/xriley/Orbit-Theme#author--license) github repository.
