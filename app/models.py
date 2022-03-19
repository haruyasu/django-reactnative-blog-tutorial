from django.db import models

# ブログ
class Blog(models.Model):
    title = models.CharField('タイトル', max_length=255)
    content = models.TextField('内容')
    updated_at = models.DateTimeField('更新日', auto_now=True)
    created_at = models.DateTimeField('作成日', auto_now_add=True)

    class Meta:
        verbose_name = 'ブログ'
        verbose_name_plural = 'ブログ'

    def __str__(self):
        return self.title
