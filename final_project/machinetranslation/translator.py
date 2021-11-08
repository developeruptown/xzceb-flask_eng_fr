#!/usr/bin/python
""" Translator Module """
import os
from ibm_watson import LanguageTranslatorV3 , ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

class Translator():
    """Translator Class that holds all the methods and attributes to translate languages"""
    def __init__(self):
        """ Innitialize Translator class and set api key, api url, watson
            authenticator and language translator attribs right away """
        self.service_api_key=os.environ['apikey']
        self.service_api_url=os.environ['url']

        self.authenticator = IAMAuthenticator(self.service_api_key) #IAM Authenticator Instance
        self.language_translator=LanguageTranslatorV3(
                                    version='2018-05-01',
                                    authenticator=self.authenticator
                                )
        #set the service URL for languange translator instance
        self.language_translator.set_service_url(self.service_api_url)
        #disable the ssl verification for local host, will impletment a different
        self.language_translator.set_disable_ssl_verification(True)

    def e2f_translator_function(self, english_text):
        """ Translate English to French using Watson Language Translator """
        try:
            translation = self.language_translator.translate(
                text=english_text,
                model_id='en-fr').get_result()
            return translation.get("translations")[0].get('translation')

        except ApiException as ex:
            if ex.code == 400 and \
            ex.message == "Unable to validate payload size, the 'text' is empty.":
                return "Text to Translate cannot be empty"
            return "Method failed with status code " + str(ex.code) + ": " + ex.message

    def f2e_translator_function(self,french_text):
        """ Translate French To English using Watson Language Translator """
        try:
            translation = self.language_translator.translate(
                text=french_text,
                model_id='fr-en').get_result()
            return  translation.get("translations")[0].get('translation')
        except ApiException as ex:
            if ex.code == 400 and \
            ex.message == "Unable to validate payload size, the 'text' is empty.":
                return "Text to Translate cannot be empty"

            return "Method failed with status code " + str(ex.code) + ": " + ex.message
