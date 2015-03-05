import pytest

import i18n


def test_load_translator():
    tr = i18n.load_translator('foo.yml')
    tr.language = 'en'
    tr.fallback = 'de'
    _ = tr.t
    assert _('greet') == 'Hello!'

    tr.language = 'de'
    assert _('greet') == 'Hallo!'

    tr.language = 'es'
    assert _('greet') == '¡Hola!'

    tr.language = 'gr'
    assert _('greet') == 'Hallo!'

    tr.language = 'jp'
    tr.fallback = 'it'
    assert _('greet') == 'greet'


if __name__ == '__main__':
    pytest.main()
