class ResetPasswordOld(View):

    def get(self, request, pk, token):
        context = {'form': UserForm(pk)}
        return render(request, 'accounts/reset_password.html', context)

    def post(self, request, pk, token):
        # _email = request.POST.get('email')
        # token = urlsafe_base64_encode(force_bytes(_email))
        form = UserForm(request.POST)
        # email = form.data['email']
        # password = form.data['password']
        # confirm_password = form.data['confirm_password']
        msg_no_email = "Este e-mail não está cadastrado."
        msg_diff_pass = "As senhas não conferem."
        pass8 = "A senha deve conter no mínimo 8 caracteres."
        msg_success = "Senha alterada com sucesso."

        if form.is_valid():
            user = User.objects.filter(email=email).first()
            if not user:
                messages.error(request, msg_no_email)
                return redirect('accounts:reset_password')

            if password != confirm_password:
                messages.error(request, msg_diff_pass)
                return redirect('accounts:reset_password')
            elif len(password) < 8:
                messages.error(request, pass8)
                return redirect('accounts:reset_password')
            else:
                user.set_password(password)
                user.save()

            messages.success(request, msg_success)
            return redirect('accounts:login')

        context = {'form': form}
        return render(request, 'accounts/reset_password.html', context)
