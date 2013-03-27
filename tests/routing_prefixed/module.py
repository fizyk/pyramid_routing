prefix = '{var}'

routes = [
    dict(name='module_index', pattern='/'),
    dict(name='module_secret', pattern="/secret"),
    dict(name='module_very_secret', pattern="/secret/very"),
]
