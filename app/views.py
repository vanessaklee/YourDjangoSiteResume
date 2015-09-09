"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Vanessa Lee',
    'bio' : 'I am a very, very lucky individual. I am a senior full-stack developer in a small tech department in Austin, TX. We code our data services in Erlang/Elixir/Phoenix and our front-end applications in Ember.js, Python, php, and now Django! In addition to that, I am a single-mother of three amazing boys and an agented fiction author writing books for children and young adults.' ,
    'interests' : 'Currently I am digging deep into the best testing and documentation practices for our software. My team has been lacking in these areas. My kids and I are addictvely listening to the audiobook of <a href="http://www.ernestcline.com/books/rpo/">Ready Player One</a>. I\'m reading <a href="http://books.simonandschuster.com/The-Boy-in-the-Black-Suit/Jason-Reynolds/9781442459502">The Boy in the Black Suit</a>, and I\'ll be moderating some panels at the Texas Book Festival. Come and see me!', 
    'email' : 'vanessaklee@gmail.com', # Leave blank if you'd prefer not to share your email with other conference attendees
    'twitter_username' : 'girlsleuthcom', # No @ symbol, just the handle.
    'github_username' : "vanessaklee", 
    'headshot_url' : 'http://vanessa-lee.com/images/headshot_19.jpg', # Link to your GitHub, Twitter, or Gravatar profile image.
}
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
            })
    )