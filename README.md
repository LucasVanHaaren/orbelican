# orbelican

A simple port of **orbit-theme** for **Pelican** to build your online resume

>[**orbit-theme**](https://github.com/xriley/Orbit-Theme) is a free BootStrap resume template for developers

## Getting started

### Configuration

To avoid problems make sure this configuration is written in `pelicanconf.py`

```python
THEME = "orbelican"
AUTHOR = ""
SITENAME = ""
SITEURL = ""
PATH = ""
TIMEZONE = ''
DEFAULT_LANG = ''
ARTICLE_EXCLUDES = [".env"] # exclude your venv
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

To build css files from sass, run:

```bash
python setup.py build_sass
```

## License

>This Bootstrap template [...] is 100% FREE as long as you keep the footer attribution link.

This is a port of [**orbit-theme**](https://github.com/xriley/Orbit-Theme) for Pelican, it can be used for free if you keep the footer attribution link.

>If you'd like to use the template without the attribution link, you can [buy the commercial license](https://themes.3rdwavemedia.com/bootstrap-templates/resume/orbit-free-resume-cv-bootstrap-theme-for-developers/) via the theme website

If you have paid for the license you can hide the footer by setting the configuration variable `SHOW_FOOTER = True` in your `pelicanconf.py`

The above quotes come from the [original theme](https://github.com/xriley/Orbit-Theme#author--license) github repository.
