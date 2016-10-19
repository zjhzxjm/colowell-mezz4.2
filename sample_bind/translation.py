from modeltranslation.translator import translator, TranslationOptions
from .models import Bind, Code


class TranslateBind(TranslationOptions):
    fields = ()


class TranslateCode(TranslationOptions):
    fields = ()

translator.register(Code, TranslateCode)
translator.register(Bind, TranslateBind)