from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Users
from .forms import LoginForm

def home(request):
    return render(request, 'index.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


def login(request):
    if request.method == 'GET':
        form = LoginForm()
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')

    return render(request, 'login.html', {'form' : form})



"""
# 로그인 정보 함수 버전
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        errMsg = {}

        if not (username and password):
            errMsg['error'] = "모든 값을 입력하세요"
        else:
            user = Users.objects.get(username = username)
            if check_password(password, user.password):
                request.session['user'] = user.id
                return redirect('/')
            else:
                errMsg['error'] = "비밀번호를 다시 입력하세요"
        return render(request, 'login.html', errMsg)
"""
            


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('re-password', None)
        useremail = request.POST.get('useremail', None)
        errorMsg = {}

        if not (username and useremail and password and repassword):
            errorMsg['error'] = "모든 값을 입력해야 합니다."
        elif password != repassword:
            errorMsg['error'] = "비밀번호가 다릅니다."
        else:
            user = Users(
                username = username,
                password = make_password(password),
                useremail = useremail
            )
            user.save()
            return redirect('/')

        return render(request, 'register.html', errorMsg)