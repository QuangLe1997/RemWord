import random

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .forms import UserForm, TopicForm, VocabularyForm, PredictForm
from .models import Topic, Vocabulary

# AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def create_topic(request):
    if not request.user.is_authenticated:
        return render(request, 'music/login.html')
    else:
        form = TopicForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.topic_logo = request.FILES['topic_logo']
            file_type = topic.topic_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'topic': topic,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'music/create_topic.html', context)
            topic.save()
            return render(request, 'music/detail.html', {'topic': topic})
        context = {
            "form": form,
        }
        return render(request, 'music/create_topic.html', context)


def create_vocabulary(request, topic_id):
    form = VocabularyForm(request.POST or None, request.FILES or None)
    topic = get_object_or_404(Topic, pk=topic_id)
    print(form.data)
    if form.is_valid():
        topics_vocabularys = topic.vocabulary_set.all()
        for s in topics_vocabularys:
            if s.vocabulary_title == form.cleaned_data.get("vocabulary_title"):
                context = {
                    'topic': topic,
                    'form': form,
                    'error_message': 'You already added that vocabulary',
                }
                return render(request, 'music/create_vocabulary.html', context)
        vocabulary = form.save(commit=False)
        vocabulary.topic = topic
        vocabulary.save()
        return render(request, 'music/detail.html', {'topic': topic})
    context = {
        'topic': topic,
        'form': form,
    }
    return render(request, 'music/create_vocabulary.html', context)


def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    topic.delete()
    topics = Topic.objects.filter(user=request.user)
    return render(request, 'music/index.html', {'topics': topics})


def delete_vocabulary(request, topic_id, vocabulary_id, local_delete=1):
    topic = get_object_or_404(Topic, pk=topic_id)
    vocabulary = Vocabulary.objects.get(pk=vocabulary_id)
    vocabulary.delete()
    if int(local_delete) == 0:
        return render(request, 'music/detail.html', {'topic': topic})
    if int(local_delete) == 1:
        try:
            topics = Topic.objects.filter(user=request.user)
            vocabulary_ids = []
            for topic in topics:
                for vocabulary in topic.vocabulary_set.all():
                    vocabulary_ids.append(vocabulary.pk)
            users_vocabularys = Vocabulary.objects.filter(pk__in=vocabulary_ids)

        except Exception as e:
            users_vocabularys = []
        return render(request, 'music/vocabularys.html', {
            'vocabulary_list': users_vocabularys,
            'filter_by': 'all',
        })


def detail(request, topic_id):
    print('chay ham detal')
    if not request.user.is_authenticated:
        return render(request, 'music/login.html')
    else:
        user = request.user
        topic = get_object_or_404(Topic, pk=topic_id)
        return render(request, 'music/detail.html', {'topic': topic, 'user': user})


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'music/login.html')
    else:
        topics = Topic.objects.filter(user=request.user)
        vocabulary_results = Vocabulary.objects.all()
        query = request.GET.get("q")
        if query:
            topics = topics.filter(
                Q(topic_title__icontains=query)
            ).distinct()
            vocabulary_results = vocabulary_results.filter(
                Q(vocabulary_title__icontains=query)
            ).distinct()
            return render(request, 'music/index.html', {
                'topics': topics,
                'vocabularys': vocabulary_results,
            })
        else:
            return render(request, 'music/index.html', {'topics': topics})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                topics = Topic.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'topics': topics})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                topics = Topic.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'topics': topics})
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)


def vocabularys(request, filter_by):
    # print(filter_by)
    if not request.user.is_authenticated:
        return render(request, 'music/login.html')
    else:
        try:
            vocabulary_ids = []
            for topic in Topic.objects.filter(user=request.user):
                for vocabulary in topic.vocabulary_set.all():
                    vocabulary_ids.append(vocabulary.pk)
            users_vocabularys = Vocabulary.objects.filter(pk__in=vocabulary_ids)

        except Topic.DoesNotExist:
            users_vocabularys = []
        return render(request, 'music/vocabularys.html', {
            'vocabulary_list': users_vocabularys,
            'filter_by': filter_by,
        })


def compare_vocabualry(request, topic_id, type_compare):
    type_compare = int(type_compare)
    tempalte = ['music/etovn.html', 'music/VN2E.html', 'music/Story2E.html', 'music/Story2VN.html']
    if not request.user.is_authenticated:
        return render(request, 'music/login.html')
    else:
        form = PredictForm(request.POST or None, request.FILES or None)
        topic = get_object_or_404(Topic, pk=topic_id)
        a = list(topic.vocabulary_set.all())
        ran = None
        if len(a) > 0:
            ran = random.choice(a)
        if request.method == 'POST':
            predict = form.save(commit=False)
            predict.user = request.user
            ran_old = form.cleaned_data['vocabulary']
            if type_compare % 2 == 0:
                compare = ran_old.mean
            else:
                compare = ran_old.vocabulary_title
            if form.cleaned_data['predict_txt'] == compare:
                ran_old.rating = (ran_old.num_false + 1) * 100.0 / (ran_old.num_show + 1)
                ran_old.num_true += 1
                ran_old.num_show += 1
                ran_old.save()
                predict.result = 1
                res = True
                message = 'Greate !!!'
            else:
                ran_old.rating = (ran_old.num_false + 1) * 100.0 / (ran_old.num_show + 1)
                ran_old.num_false += 1
                ran_old.num_show += 1
                ran_old.save()
                predict.result = 0
                res = False
                message = compare
            predict.vocabulary = ran_old
            predict.save()
            context = {
                "topic": topic,
                "form": form,
                "result": res,
                "error_message": message,
                "link": ran_old
            }
            print(context)
            return render(request, tempalte[type_compare], context)
        context = {
            "topic": topic,
            "new_word": ran,
            "form": form,
        }
        return render(request, tempalte[type_compare], context)


def update_voca():
    pass


def add_example():
    pass
