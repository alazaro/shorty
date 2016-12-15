import logging

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models

from utils.users import get_random_string, get_random_user, NoUsersException


logger = logging.getLogger(__name__)


class ShortURL(models.Model):
    original = models.URLField(
        null=False,
        blank=False,
        unique=True,
        db_index=True,
        verbose_name='URL',
        help_text='URL to be shortened'
    )

    short = models.CharField(
        null=False, blank=False, unique=True, db_index=True, max_length=100)
    submitter = models.ForeignKey(
        'auth.User', related_name='urls')

    def __str__(self):
        return '{0} -> {1}'.format(self.short, self.original)

    def get_absolute_url(self):
        return reverse('url_info', args=[self.short])

    def clean(self, *args, **kwargs):
        if not self.submitter_id:
            try:
                self.submitter = get_random_user()
            except NoUsersException as e:
                raise ValidationError(e)
        if not self.short:
            self.short = get_random_string()
        try:
            return super().validate_unique(*args, **kwargs)
        except ValidationError as e:
            if (settings.REASSIGN_SHORT_IF_EXISTS and
                    'short' in e.message_dict):
                self.short = None
                return self.clean(*args, **kwargs)

            raise

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
