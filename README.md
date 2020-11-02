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
