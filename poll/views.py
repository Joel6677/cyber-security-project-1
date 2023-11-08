from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import Poll
from django.db import connections, connection, transaction
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

import logging
logger = logging.getLogger('polls')


def home(request):
    polls = Poll.objects.all()

    context = {
        'polls' : polls
    }

    logger.info("User accessed the 'home' view")

    return render(request, 'poll/home.html', context)

@login_required
def create(request):

    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            new_poll = form.save(commit=False)
            new_poll.creator = request.user
            new_poll.save()

            logger.info(f"New poll created by user {request.user.username}")

            return redirect('home')
    else:
        form = CreatePollForm()

    context = {'form' : form}
    return render(request, 'poll/create.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html', context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            logger.error("Invalid form option received in 'vote' view")
            return HttpResponse(400, 'Invalid form option')
        poll.save()

        logger.info(f"User {request.user.username} voted in poll {poll_id}")

        return redirect('results', poll.id)
        
    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)
#broken access control
#@login_required
def delete_poll(request, poll_id):
    # Get the poll to be deleted
    poll = Poll.objects.get(pk=poll_id)

    logger.info("User accessed the 'delete_poll' view")

    # if request.user != poll.creator:
    #     raise PermissionDenied("You are not the owner of this poll and cannot delete it.")

    print(request.method)
    if request.method == 'POST':
        # If the request is a POST request, delete the poll
        poll.delete()

        logger.info(f"Poll {poll_id} deleted by user {request.user.username}")

        return redirect('home')  # Redirect to the home page or another appropriate page after deletion

    # If the request is not a POST request, render the confirmation page
    return render(request, 'poll/delete.html', {'poll': poll})






