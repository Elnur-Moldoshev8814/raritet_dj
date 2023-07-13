from django.http import HttpResponse
from .models import Book, Filial


def all_books(request):
    names = Filial.objects.all()
    res = ''
    for name in names:
        res += f"{name.name} <br>"
    return HttpResponse(res)



def detail_location(request, location):
    location = Book.objects.all()

    return HttpResponse("hk")

# def author_detail(request, login):
#     author = Author.objects.get(login=login)  # SELECT * FROM Author where login = '1ypen'
#     return HttpResponse(f"{author.first_name} <br> {author.last_name} <br> {author.bio}")

#
#     authors = Author.objects.all()
    # res = ''
    # for author in authors:
    #     res += f"{author.login} <br>"
    # return HttpResponse(res)