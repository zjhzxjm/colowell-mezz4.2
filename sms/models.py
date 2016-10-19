from django.db import models
import datetime
from django.conf import settings
from sms.conf import settings as sms_settings
from django.utils.encoding import smart_text
import random
import hashlib
import time
from django.utils.translation import ugettext_lazy as _


if hasattr(random, 'SystemRandom'):
    randrange = random.SystemRandom().randrange
else:
    randrange = random.randrange
MAX_RANDOM_KEY = 18446744073709551616     # 2 << 63


def get_safe_now():
    try:
        from django.utils.timezone import utc
        if settings.USE_TZ:
            return datetime.datetime.utcnow().replace(tzinfo=utc)
    except:
        pass
    return datetime.datetime.now()


class MyProfile(models.Model):
    user = models.OneToOneField("auth.User")
    mobile_phone = models.CharField(_("Telephone number"), max_length=11)

    def __str__(self):
        return "%s" % self.mobile_phone


class Captcha(models.Model):
    challenge = models.CharField(blank=False, max_length=32)
    response = models.CharField(blank=False, max_length=32)
    hashkey = models.CharField(blank=False, max_length=40, unique=True)
    expiration = models.DateTimeField(blank=False)

    def save(self, *args, **kwargs):
        self.response = self.response.lower()
        if not self.expiration:
            self.expiration = get_safe_now() + datetime.timedelta(minutes=int(sms_settings.CAPTCHA_TIMEOUT))
        if not self.hashkey:
            key_ = (
                smart_text(randrange(0, MAX_RANDOM_KEY)) +
                smart_text(time.time()) +
                smart_text(self.challenge, errors='ignore') +
                smart_text(self.response, errors='ignore')
            ).encode('utf8')
            self.hashkey = hashlib.sha1(key_).hexdigest()
            del(key_)
        super(Captcha, self).save(*args, **kwargs)

    def str__(self):
        return self.challenge

    def remove_expired(cls):
        cls.objects.filter(expiration__lte=get_safe_now()).delete()
    remove_expired = classmethod(remove_expired)

    @classmethod
    def generate_key(cls):
        challenge, response = sms_settings.get_challenge()()
        store = cls.objects.create(challenge=challenge, response=response)

        return store.hashkey, challenge


