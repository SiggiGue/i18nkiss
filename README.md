#i18nkiss
#Internationalization in keep it simple stupid manner


##Setup
* clone repo.
* cd to repo.
* type `python setup.py install`

## Usage

--------
This is an example yml file `foo.yml`:

```yaml
de:
    greet: Hallo!
    mynameis: Mein Name ist {name}.
en:
    greet: Hello!
    mynameis: My name is {name}.
es:
    greet: ¡Hola!
    mynameis: Mi nombre est {name}.

```

The file is used in following usage example:

```python
tr = load_translator('foo.yml')
tr.language = 'en'
tr.fallback = 'de'
_ = tr.t
print(_('greet'))
print(_('mynameis').format(name='Siegfried'))

tr.language = 'de'
print(_('greet'))
print(_('mynameis').format(name='Siegfried'))

language = 'es'
print(_('greet'))
print(_('mynameis').format(name='Siegfried'))

language = 'gr'
print(_('greet'))
print(_('mynameis').format(name='Siegfried'))

language = 'jp'
tr.fallback = 'it'
print(_('greet'))
print(_('mynameis').format(name='Siegfried'))
```

Have Fun,

Siegfried
