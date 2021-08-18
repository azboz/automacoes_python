from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='aumentarosseguidores', password='cursoinstagram')

with smart_run(session):
    session.set_do_follow(enabled=True, percentage=100)
    session.set_do_like(enabled=True, percentage=100)

    session.like_by_tags(['udemy'], amount=5)

    comentarios = ['Nice shot!', 'Love your posts']
    session.set_do_comment(enabled=True, percentage=95)
    session.set_comments(comentarios, media='Photo')
    session.join_pods()
