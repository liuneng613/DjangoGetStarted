"""
verbose_name = "pizza"
class Meta，内嵌于 UserMessage 这个类的定义中
如果 class Publisher 是顶格的，那么 class Meta 在它之下要缩进4个空格－－按 Python 的传统
你可以在任意一个 模型 类中使用 Meta 类，来设置一些与特定模型相关的选项。
如：设置ordering = ['name']，默认地都会按 name 字段排序
    models.ForeignKey     # 外键
    models.DateTimeField  # 时间字段
    models.IntegerField   # 整型
    models.IPAddressField # IP地址
    models.FileField      # 上传文件
    models.ImageField     # 图片

"""

from django.db import models

# Create your models here.


# 继承于django.db.models.Model
class UserMessage(models.Model):
    # 设置最大长度，verbose_name在后台显示字段会用到
    name = models.CharField(max_length=20, verbose_name=u"用户名")
    # Django提供内置的邮箱字段会帮忙验证` default_validators = [validators.validate_email]`
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"联系地址")
    message = models.CharField(max_length=500, verbose_name=u"留言信息")
    object_id = models.CharField(max_length=50, primary_key=True, default="", verbose_name="主键")


    class Meta:
        verbose_name = u"用户留言信息"
        # db_table ，这里我们让它自动生成所以不用指定
