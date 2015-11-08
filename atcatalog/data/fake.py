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
english = { 0: (0, u'Welcome!', u'Welcome!', u'./atcatalog/data/audio.mp3'),
            1: (1, u'Hello!', u'Hello!', u'./atcatalog/data/audio.mp3') }

spanish = { 0: (0, u'Hombre!', u'Man!', u'./atcatalog/data/audio.mp3'),
            1: (1, u'¡Hola!', u'Hello!', u'./atcatalog/data/audio.mp3') }

french = {  0: (0, u'Bienvenue!', u'Welcome!', u'./atcatalog/data/audio.mp3'),
            1: (1, u'Bonjour!', u'Good day!', u'./atcatalog/data/audio.mp3') }

german = {  0: (0, u'Hallo!', u'Hello!', u'./atcatalog/data/audio.mp3'),
            1: (1, u'Guten Tag!', u'Good day!', u'./atcatalog/data/audio.mp3') }

portuguese = { 0: (0, u'Olá!', u'Hello!', u'./atcatalog/data/audio.mp3'),
               1: (1, u'Bem-vindo!', u'Welcome!', u'./atcatalog/data/audio.mp3') }

sentences = { 0: english,
              1: spanish,
              2: french,
              3: german,
              4: portuguese}
