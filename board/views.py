from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm
from users.models import Users
from django.core.paginator import Paginator
from django.http import Http404
from tag.models import Tag


def board_write(request):
    if not request.session.get('user'):
        return redirect('/users/login')

    if request.method == "GET":
        form = BoardForm()

    elif request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = Users.objects.get(pk = user_id)
            new_board = Board(
                title = form.cleaned_data['title'],
                contents = form.cleaned_data['contents'],
                writer = user
            )
            new_board.save()

            ### 태그 추가 부분 ###
            tags = form.cleaned_data['tag'].split(',')
            for tag in tags:
                if not tag : 
                    continue
                else:
                    tag = tag.strip()
                    tag_, created = Tag.objects.get_or_create(name = tag)
                    new_board.tag.add(tag_)


            return redirect('/board/list')

    return render(request, 'board_write.html', {'form' :form})

def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 6)
    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards':boards})


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    return render(request, 'board_detail.html', {'board' : board})

