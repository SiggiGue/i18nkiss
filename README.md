#i18nkiss
#Internationalization in keep it simple stupid manner


##Setup
* clone repo.
* cd to repo.
* type `python setup.py install`

## Usage

```python
import i18n

tr = i18n.load_translator('foo.yml')
tr.language = 'en'
tr.fallback = 'de'

_ = tr.t
print(_('greet'))

tr.language = 'de'
print(_('greet'))

language = 'es'
print(_('greet'))

language = 'gr'
print(_('greet'))

language = 'jp'
tr.fallback = 'it'
print(_('greet'))

```

Have Fun,

Siegfried
