"""Test's routes definition."""

routes = [
    dict(name='index', pattern='/'),
    dict(name='secret', pattern="/secret"),
    dict(name='very_secret', pattern="/secret/very"),
]
