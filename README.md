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

### With pelican-data-files

This theme support [**pelican-data-files**](https://github.com/LucasVanHaaren/pelican-data-files) plugin.

You can fill in your information by installing this plugin and copying the data folder to your project root directory (next to content for example), then fill in your informations.

### Without plugin

If you don't use **pelican-data-files**, you have to set data as Pelican settings.
Paste and fill in these following data in your `pelicanconf.py`.

```python
DATA_CONFIG = {
    "theme": {
        "color": "",
        "browser_color": "",
        "show_footer": True
    },
    "site": {
        "favicon": "",
        "profile": "",
        "description": "",
        "robots": "",
        "google_analytics": ""
    }
}

DATA_PROFILE = {
    "info": {
        "firstname": "",
        "lastname": "",
        "tagline": "",
        "age": "",
        "email": "",
        "phone": "",
        "address": "",
        "driving_license": ""
    },
    "contact": {
        "telegram": "",
        "website": "",
        "linkedin": "",
        "github": "",
        "gitlab": "",
        "bitbucket": "",
        "twitter": "",
        "stackoverflow": "",
        "codewars": "",
        "goodreads": ""
    },
    "languages": {
        "title": "",
        "list": [
            {
                "idiom": "",
                "level": ""
            }
        ]
    }
}

DATA_RESUME = {
    "summary": {
        "title": "",
        "content": ""
    },
    "education": {
        "title": "",
        "list": [
            {
                "degree": "",
                "date": "",
                "university": "",
                "details": ""
            }
        ]
    },
    "experiences": {
        "title": "",
        "list": [
            {
                "title": "",
                "company": "",
                "date": "",
                "details": ""
            }
        ]
    },
    "projects": {
        "title": "",
        "content": "",
        "list": [
            {
                "title": "",
                "tagline": "",
                "link": ""
            }
        ]
    },
    "skills": {
        "title": "",
        "list": [
            {
                "name": "",
                "level": ""
            }
        ]
    }
}
```

### Customization

#### Add custom profile picture and favicon

Copy your best profile picture in your site project in `images` folder and set `PROFILE_PICTURE = '<FILENAME>'`. Do the same for customize your favicon.

## Contributing

To build css files from sass, make sur you have install dev dependencies and run the task `sass`:

```bash
pip install -e .[dev] # run this if you haven't already
invoke sass
```

## License

>This Bootstrap template [...] is 100% FREE as long as you keep the footer attribution link.

This is a port of [**orbit-theme**](https://github.com/xriley/Orbit-Theme) for Pelican, it can be used for free if you keep the footer attribution link.

>If you'd like to use the template without the attribution link, you can [buy the commercial license](https://themes.3rdwavemedia.com/bootstrap-templates/resume/orbit-free-resume-cv-bootstrap-theme-for-developers/) via the theme website

If you have paid for the license you can hide the footer by setting the configuration variable `SHOW_FOOTER = True` in your `pelicanconf.py`

The above quotes come from the [original theme](https://github.com/xriley/Orbit-Theme#author--license) github repository.
