#i18nkiss
#Internationalization in keep it simple stupid manner

This is a keep ist simple internationalization tool with a Translator instance suporting yaml-files containing translation definitions. It does support templating due to the .format() method in python strings. For the simplicity the support of pluralization is not provided. In that case you should consider using the more complex `gettext` module.

##Setup
* clone this repo.
* cd to the cloned repo.
* type `python setup.py install`

## Usage

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
import i18n

# use the Translator class directly:
tr = i18n.Translator('foo.yml', language='de', fallback='en')

# or use the load_translator() function:
tr = i18n.load_translator('foo.yml')
tr.language = 'en'
tr.fallback = 'de'
_ = tr.t

print(_('greet'))
print(_('mynameis').format(name='Siegfried'))

Hello!
My name is Siegfried.

tr.language = 'de'
print(_('greet'))
print(_('mynameis').format(name='Tom'))

Hallo!
Mein Name ist Tom.

tr.language = 'es'
print(_('greet'))
print(_('mynameis').format(name='Jack'))

¡Hola!
Mi nombre est Jack.


# Behaviour on not supported languages:
tr.language = 'jp'
tr.fallback = 'it'
print(_('greet'))
print(_('mynameis').format(name='what'))

greet
mynameis

```

Have Fun!

BSD licensed.
