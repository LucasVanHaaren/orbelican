# orbelican

A simple port of **orbit-theme** for **Pelican** to build your online resume

>[**orbit-theme**](https://github.com/xriley/Orbit-Theme) is a free BootStrap resume template for developers

## Getting started

To build css files from sass, run:

```bash
python setup.py build_sass
```

```python
THEME = 'orbelican'
THEME_COLOR = 'blue' # ['blue','green','red','purple','grey']

# SITE CONFIG
SITENAME = ''
SITEURL = ''
SITEDESCRIPTION = ''
SITEFAVICON = ''
SITEROBOTS = ''

# PROFILE
PROFILE_FIRSTNAME = ''
PROFILE_LASTNAME = ''
PROFILE_AGE = ''
PROFILE_PICTURE = ''
PROFILE_SUMMARY_LABEL = ''
PROFILE_SUMMARY = ''
PROFILE_EDUCATIONS_LABEL = ''
PROFILE_EDUCATIONS = [
    {
        'degree': '',
        'time': '',
        'university': '',
        'details': '',
    }
]
PROFILE_EXPERIENCES_LABEL = ''
PROFILE_EXPERIENCES = [
    {
        'title': '',
        'time': '',
        'company': '',
        'details': ''
    }
]
PROFILE_PROJECTS_LABEL = ''
PROFILE_PROJECTS_INTRO = ''
PROFILE_PROJECTS = [
    {
        'title': '',
        'link': '',
        'tagline': ''
    }
]
PROFILE_SKILLS_LABEL = ''
PROFILE_SKILLS = [
    {
        'name': '',
        'level': '',
    }
]

# SIDEBAR
SIDEBAR_EMAIL = ''
SIDEBAR_PHONE = ''
SIDEBAR_TELEGRAM = ''
SIDEBAR_WEBSITE = ''
SIDEBAR_LINKEDIN = ''
SIDEBAR_GITHUB = ''
SIDEBAR_GITLAB = ''
SIDEBAR_BITBUCKET = ''
SIDEBAR_TWITTER = ''
SIDEBAR_STACKOVERFLOW = ''
SIDEBAR_CODEWARS = ''
SIDEBAR_GOODREADS = ''
SIDEBAR_DRIVINGLICENSE = ''
SIDEBAR_ADDRESS = ''

SIDEBAR_LANGUAGES_LABEL = ''
SIDEBAR_LANGUAGES = [
    {
        'idiom': '',
        'level': ''
    }
]


# EXTRA FEATURES
BROWSER_COLOR = ''
GOOGLE_ANALYTICS = ''
SHOW_FOOTER = True
```

### Customization

#### Add a profile picture

Copy your best profile picture in your site project in `images` folder and set `PROFILE_PICTURE = '<FILENAME>'`. Do the same for customize your favicon.

## License

>This Bootstrap template [...] is 100% FREE as long as you keep the footer attribution link.

This is a port of [**orbit-theme**](https://github.com/xriley/Orbit-Theme) for Pelican, it can be used for free if you keep the footer attribution link.

>If you'd like to use the template without the attribution link, you can [buy the commercial license](https://themes.3rdwavemedia.com/bootstrap-templates/resume/orbit-free-resume-cv-bootstrap-theme-for-developers/) via the theme website

If you have paid for the license you can hide the footer by setting the configuration variable `SHOW_FOOTER = True` in your `pelicanconf.py`

The above quotes come from the [original theme](https://github.com/xriley/Orbit-Theme#author--license) github repository.
