from modeltranslation.translator import translator, TranslationOptions
from .models import MyProfile


class TranslateMyProfile(TranslationOptions):
    fields = ()

translator.register(MyProfile, TranslateMyProfile)
