from core.views import BaseView, LoginRequiredMixin


class ProfileView(LoginRequiredMixin, BaseView):
    """View for user to sign up.

    Currently this view is not used.

    """

    template_name = 'users/profile.html'
    colors = ('#4A72B7', '#375d9e', '#fefefe')
    title = 'DK - Ваш профиль'
    description = 'DK - Ваш профиль'

    def post(self, request):
        """Update user profile."""
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        avatar = request.FILES.get('avatar')

        if self.user:
            self.user.first_name = first_name
            self.user.last_name = last_name

            if avatar:
                self.user.image = avatar

            self.user.save()

        return self.get(request)
