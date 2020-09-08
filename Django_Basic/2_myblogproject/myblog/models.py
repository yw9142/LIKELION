from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]


class Comment(models.Model):
    # post = models.ForeignKey()객체가 저장되어 있는 변수
    # 댓글(Comment)이 새로 생성될때, 어떠한 게시글(Post)인지를 나타내는 대한 변수 명
    # models.ForeignKey()는 외래키를 설정하는 함수
    post = models.ForeignKey('myblog.Post', on_delete=models.CASCADE)
    # CASCADE: 부모(게시물)가 삭제 되면, 자기 자신(댓글)도 삭제. 게시글에 대한 모델 클래스인Post에 따라 생성된 게시글이 삭제되면, 댓글에 대한 모델 클래스인 Comment에 따라 생성된 댓글도 삭제.
    # PROTECT: 댓글이 존재하면, 게시물 삭제 불가능(ProtectedError발생시킴)
    # SET_NULL: 게시물이 삭제되면, 댓글의 게시물 정보를 NULL로 변경.
    content = models.TextField()

    def __str__(self):
        return self.content
