# orbelican

A simple port of **orbit-theme** for **Pelican** to build your online resume

>[**orbit-theme**](https://github.com/xriley/Orbit-Theme) is a free BootStrap resume template for developers

## Getting started

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
PROFILE_NAME = ''
PROFILE_PICTURE = ''
PROFILE_SUMMARY_LABEL = ''
PROFILE_SUMMARY = ''

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
