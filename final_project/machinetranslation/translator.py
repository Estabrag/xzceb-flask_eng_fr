'''
This module contains functions to translate english texts 
to french and french text to english
'''

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):

    '''
    Translate English text to french using MyMemoryTranslator

    Args:
    english_text: English text to be translated

    Returns:
    french_text: translated french text
    '''

    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    french_text = translator.translate(english_text)
    return french_text


def french_to_english(french_text):

    '''
    Translate french text to english using MyMemoryTranslator

    Args:
    french_text: french text to be translated

    Returns:
    english_text: translated english text
    '''

    translator = MyMemoryTranslator(source='fr-FR', target='en-US')
    english_text = translator.translate(french_text)
    return english_text
