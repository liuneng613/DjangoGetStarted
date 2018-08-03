from django.shortcuts import render
from .models import UserMessage

# Create your views here.


def getform(request):
# 查找部分
    # # UserMessage默认的数据管理器objects。
    # # 方法all()是将所有数据返回成一个queryset类型(django的内置类型)
    # all_message = UserMessage.objects.filter(object_id="abcd", address="武汉1")
    #
    # #我们可以对于all_message进行遍历操作
    # for message in all_message:
    #     # 每个message实际就是一个UserMessage对象（这时我们就可以使用对象的相关方法）。
    #     print(message.name)


# # 存储部分
#     user_message = UserMessage()
#     user_message.name = "test02"
#     user_message.message = "blog.ratel.net.cn"
#     user_message.address = "武汉"
#     user_message.email = "ratel@163.com"
#     user_message.object_id = "efgh"
#     user_message.save()


# # 删除部分
#     all_message = UserMessage.objects.filter(name="test01", address="武汉")
#     all_message.delete()
#     for message in all_message:
#         message.delete()


# # 从页面post添加到数据库
#     if request.method == "POST":
#         name = request.POST.get('name', '')
#         message = request.POST.get('message', '')
#         address = request.POST.get('address', '')
#         email = request.POST.get('email', '')
#     user_message = UserMessage()
#     user_message.name = name
#     user_message.message = message
#     user_message.address = address
#     user_message.email = email
#     user_message.object_id = 'ijkl'
#     user_message.save()


# 将数据回填至html中
    message = None
    all_message = UserMessage.objects.filter(name='test02')
    if all_message:
        message = all_message[0]

    return render(request, 'message_form.html', {
        "my_message": message
    })