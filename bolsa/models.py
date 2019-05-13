from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(
            self,
            cpf,
            first_name,
            last_name,
            password=None
    ):
        """
        Cria e salva um usuário com o cpf, primeiro nome, último nome, data de nascimento e senha.
        """
        if not cpf:
            raise ValueError("Número de CPF será usado para login.")

        user = self.model(
            cpf=cpf,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self,
            cpf,
            first_name,
            last_name,
            password
    ):
        """
        Cria e salva superuser, com cpf, primeiro nome, último nome, data de nascimento e senha.
        """
        user = self.create_user(
            cpf,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    cpf = models.BigIntegerField(verbose_name="CPF", unique=True)
    first_name = models.CharField(verbose_name="Primeiro nome", max_length=255)
    last_name = models.CharField(verbose_name="Sobrenome", max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "cpf"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        """Método para tratar se o usuário possui permissões especiais"""
        return True

    def has_module_perms(self, app_label):
        """Método para tratar se o usuário possui permissão para ver a label app"""
        return True

    @property
    def is_staff(self):
        """Se o usuário for um membro do staff?"""
        return self.is_admin


class Ativos(models.Model):
    nome = models.CharField(
        verbose_name="Nome da Ação",
        max_length=255,
    )
    codigo = models.CharField(
        verbose_name="Código do Ativo",
        max_length=5,
        unique=True
    )
    descricao = models.TextField(
        verbose_name="Descrição do Ativo",
        blank=True,
        null=True
    )
    preco = models.FloatField(
        verbose_name="Preço das Ações",
    )
    quantidade = models.IntegerField(
        verbose_name="Quantidade de ações"
    )
