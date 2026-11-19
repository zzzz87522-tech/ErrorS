import uuid  # для уникальных идентификаторов копий книг

from django.db import models
from django.urls import reverse  # для get_absolute_url


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Введите жанр книги (например, Научная фантастика)")

    def __str__(self):
        return self.name


class Book(models.Model):
    """Модель книги (не конкретная копия)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Краткое описание книги")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13-символьный номер ISBN')
    genre = models.ManyToManyField(Genre, help_text="Выберите жанр для этой книги")

    class Meta:
        ordering = ['title']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """URL страницы конкретной книги."""
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    """Конкретная копия книги, которую можно взять в библиотеке."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный ID этой копии в библиотеке")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Техобслуживание'),
        ('o', 'На руках'),
        ('a', 'Доступна'),
        ('r', 'Зарезервирована'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS,
                              blank=True, default='m',
                              help_text='Доступность книги')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    """Автор книги."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Умер', null=True, blank=True)

    class Meta:
        ordering = ['last_name']


    class Meta:
        ordering = ['title']


    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """URL страницы конкретного автора."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
