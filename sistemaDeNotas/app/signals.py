from security.models.UserProfile import UserProfile
from django.contrib.auth.models import User
from django.db.models import signals


def create_user_profile_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


def password_change_signal(sender, instance, **kwargs):
    try:
        user = User.objects.get(username=instance.username)
        if not user.password == instance.password:
            profile = user.profile
            profile.force_password_change = False
            profile.save()
    except User.DoesNotExist:
        pass


signals.pre_save.connect(password_change_signal, sender=User, dispatch_uid='app.models')
signals.post_save.connect(create_user_profile_signal, sender=User, dispatch_uid='app.models')
