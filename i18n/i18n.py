# -- coding: utf-8 --
"""This module implements a translator for internationalization usin yaml.
It is a hardcore KISS module!
Have Fun!

Examples
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

"""

import yaml


class Translator(object):
    """Translator allows to load yaml files with translations
    and provates a `translator()` (`t()`).
    """
    def __init__(self, path_yamlfile=None,
                 language='de',
                 fallback='en'):
        """Returns a Translator instance.

        """
        self._language = language
        self._fallback = fallback
        self._path_yamlfiles = []
        self._translationsd = {}
        self.t = self.translate
        if path_yamlfile:
            self.load_translations(path_yamlfile)

    def load_translations(self, path_yamlfile, append=True, encoding='utf-8'):
        """Loads a yaml file into the internal dictionary.
        if `append=False`, the internal dictionary will be overwritten.
        """
        with open(path_yamlfile, encoding=encoding) as f:
            td = yaml.load(f)
            if append:
                self._translationsd.update(td)
                self._path_yamlfiles += [path_yamlfile]
            else:
                self._translationsd = td
                self._path_yamlfiles = [path_yamlfile]
        return True

    def translate(self, key, language=None, fallback=None):
        """Returns translation string from loaded translations."""
        if not language:
            language = self.language
        if not fallback:
            fallback = self.fallback
        if language in self._translationsd:
            if key in self._translationsd[language]:
                return self._translationsd[language][key]
        if fallback in self._translationsd:
            if key in self._translationsd[fallback]:
                return self._translationsd[fallback][key]
        return key

    @property
    def language(self):
        """The language returned by translator.
        """
        return self._language

    @language.setter
    def language(self, value):
        self._language = value

    @property
    def fallback(self):
        """The fallback language if no translation in `language` vailable.
        """
        return self._fallback

    @fallback.setter
    def fallback(self, value):
        self._fallback = value


def load_translator(path):
    """Returns a `Translator` instance with give yaml file `path` loaded.
    to translate use `.translate()` or `.t()` method.
    """
    return Translator(path, language='de', fallback='en')


if __name__ == "__main__":
    tr = load_translator('foo.yml')
    tr.language = 'en'
    tr.fallback = 'de'
    _ = tr.t
    print(_('greet'))
    print(_('mynameis').format(name='Siegfried'))

    tr.language = 'de'
    print(_('greet'))
    print(_('mynameis').format(name='Siegfried'))

    tr.language = 'es'
    print(_('greet'))
    print(_('mynameis').format(name='Siegfried'))

    tr.language = 'gr'
    print(_('greet'))
    print(_('mynameis').format(name='Siegfried'))

    tr.language = 'jp'
    tr.fallback = 'it'
    print(_('greet'))
    print(_('mynameis').format(name='Siegfried'))
