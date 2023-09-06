from django.db import models
from django.utils.text import slugify

from common.utils import from_cyrillic_to_eng


class Topic(models.Model):
    """
    Generic Topics for FAQ question grouping
    """
    name = models.CharField(
        max_length=150,
        verbose_name='Тема'
    )
    slug = models.SlugField(  # под вопросов, в зависимости будет ли у нас под каждый вопрос/ответ свой url
        max_length=150,
        verbose_name='Slug'
    )

    class Meta:
        verbose_name = 'Тема вопросов'
        verbose_name_plural = 'Темы вопросов'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/faq/' + str(self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(from_cyrillic_to_eng(str(self.name)))
        super().save(*args, **kwargs)


class Question(models.Model):
    ANSWERED = 1
    NOT_ANSWERED = 0
    STATUS_CHOICES = (
        (ANSWERED, 'Отвечен'),
        (NOT_ANSWERED, 'Не отвечен'),
    )

    text_question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(
        blank=True,
        null=True,
        verbose_name='Ответ'
    )
    topic = models.ForeignKey(
        to=Topic,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Тема'
    )
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=100
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=NOT_ANSWERED,
        verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Вопросы/Ответы'
        verbose_name_plural = 'Вопросы/Ответы'
        ordering = ()

    def __str__(self):
        question_len = round(len(str(self.text_question)) / 3)
        if question_len:
            return f'{self.pk}) {self.text_question[:question_len]}... ({self.status})'
        return '<Empty>'

    def is_answered(self):
        return self.status == Question.ANSWERED