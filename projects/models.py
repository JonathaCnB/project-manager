from django.db import models
from django.urls import reverse
from users.models import User


class Project(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Nome do projeto",
        unique=True,
    )
    start_date = models.DateField(verbose_name="Data de início")
    end_date = models.DateField(verbose_name="Data de término")
    is_active = models.BooleanField(default=True)
    value = models.DecimalField(
        verbose_name="Valor do projeto",
        max_digits=7,
        decimal_places=2,
    )
    CHOICE_STATUS_RISK = (
        ("0", "Baixo"),
        ("1", "Médio"),
        ("2", "Alto"),
    )
    risk = models.CharField(
        max_length=1,
        verbose_name="Risco ",
        choices=CHOICE_STATUS_RISK,
    )
    participants = models.ManyToManyField(User, verbose_name="Participantes")

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        db_table = "projects_project"

    def get_absolute_url(self):
        return reverse("projects:index")

    def __str__(self) -> str:
        return self.name
