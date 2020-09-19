from django.shortcuts import redirect


class RequireLoginMixin:

    def dispatch(self, request, *args, **kwargs):
        print("User", request.user)
        if not request.user.is_authenticated:
            print("is authenticated")
            return redirect("login")
        return super(RequireLoginMixin, self).dispatch(request, *args, **kwargs)
