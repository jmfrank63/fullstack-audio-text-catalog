# coding=utf-8
'''
Contains fakedata for initial development
'''
__author__ = u'johannesfrank'

#some languages
languages = { 0: u'english',
              1: u'spanish',
              2: u'french',
              3: u'german',
              4: u'portuguese'}

# sid : sentence tuple (user_id, text, translation, audio_path)
english = { 0: (0, u'Welcome!', u'Welcome!', u'audio/welcome.mp3'),
            1: (1, u'Hello!', u'Hello!', u'audio/hello.mp3') }

spanish = { 0: (0, u'Hombre!', u'Man!', u'audio/hombre.mp3'),
            1: (1, u'¡Hola!', u'Hello!', u'audio/hola.mp3') }

french = {  0: (0, u'Bienvenue!', u'Welcome!', u'audio/bienvenue.mp3'),
            1: (1, u'Bonjour!', u'Good day!', u'audio/bonjour.mp3') }

german = {  0: (0, u'Hallo!', u'Hello!', u'audio/hallo.mp3'),
            1: (1, u'Guten Tag!', u'Good day!', u'audio/guten_tag.mp3') }

portuguese = { 0: (0, u'Olá!', u'Hello!', u'audio/ola.mp3'),
               1: (1, u'Bem-vindo!', u'Welcome!', u'audio/bem-vindo.mp3') }

sentences = { 0: english,
              1: spanish,
              2: french,
              3: german,
              4: portuguese}
