from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def support_app(request):
    context = {'page': 'Home'}
    data = [
        {'group_name': 'Technical Issues1', 'group_id': 1},
        {'group_name': 'Technical Issues2', 'group_id': 2},
        {'group_name': 'Appointment Issues1', 'group_id': 3},
        {'group_name': 'Appointment Issues2', 'group_id': 4},
        {'group_name': 'Payment Issues', 'group_id': 5}
    ]
    return render(request, 'support_app.html', context={'page': 'Home', 'data': data})

@login_required

def user_greeting(request):
    return render(request, 'user_greeting.html')


@login_required
def support_detail(request, group_id):
    support_group = get_object_or_404(SupportGroup, id = group_id)
    messages = Message.objects.filter(support_group=support_group)
    context = {'group': support_group, 'messages': messages, 'group_id': support_group.id}
    return render(request, 'support_detail.html', context)

@login_required
def send_message(request, group_id):
    if request.method == 'POST':
        support_group = get_object_or_404(SupportGroup, id=group_id)
        text = request.POST.get('message', '')
        
        if text:
            Message.objects.create(
                sender=request.user,
                support_group=support_group,
                text= text
            )

    return redirect('support_detail', group_id=group_id)



