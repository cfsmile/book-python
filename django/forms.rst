*****
Forms
*****

Forms
=====

Simple "contact us" form
------------------------
.. code-block:: python

    class ContactUsForm(forms.Form):
        sender = forms.EmailField()
        subject = forms.CharField()
        body = forms.CharField(widget=forms.Textarea)

.. code-block:: python

    class ContactUsView(FormView):
        template_name = 'ksiazkaadresowa/contact-form.html'
        form_class = ContactUsForm
        success_url = '/thank-you.html'


    class ThankYouView(TemplateView):
        template_name = 'ksiazkaadresowa/thank-you.html'



:forms.py:
    .. code-block:: python

        from django import forms


        class ContactForm(forms.Form):
            subject = forms.CharField(max_length=100)
            message = forms.CharField(widget=forms.Textarea)
            sender = forms.EmailField()
            cc_myself = forms.BooleanField(required=False)

            def clean_sender(self):
                data = self.cleaned_data['sender']

                if "fred@example.com" not in data:
                    raise forms.ValidationError("You have forgotten about Fred!")

                # Always return a value to use as the new cleaned data, even if
                # this method didn't change it.
                return data

:views.py:
    .. code-block:: python

        from django.http import HttpResponseRedirect
        from django.shortcuts import render

        from .forms import NameForm

        def get_name(request):
            # if this is a POST request we need to process the form data
            if request.method == 'POST':
                # create a form instance and populate it with data from the request:
                form = NameForm(request.POST)
                # check whether it's valid:
                if form.is_valid():
                    # process the data in form.cleaned_data as required
                    # ...
                    # redirect to a new URL:
                    return HttpResponseRedirect('/thanks/')

            # if a GET (or any other method) we'll create a blank form
            else:
                form = NameForm()

            return render(request, 'name.html', {'form': form})

:form.html:
    .. code-block:: django

        <form action="/your-name/" method="post">
            {% csrf_token %}
            {{ form }}
            <input type="submit" value="Submit">
        </form>

* ``{{ form.as_table }}`` will render them as table cells wrapped in ``<tr>`` tags
* ``{{ form.as_p }}`` will render them wrapped in ``<p>`` tags
* ``{{ form.as_ul }}`` will render them wrapped in ``<li>`` tags

Model Forms
===========
.. code-block:: python

    from django.db import models

    class Person(models.Model):
        first_name = models.CharField(verbose_name=_('First Name'), max_length=30)
        last_name = models.CharField(verbose_name=_('Last Name'), max_length=30, db_index=True)
        phone = models.IntegerField(verbose_name=_('Phone'), null=True, blank=True)
        date_of_birth = models.DateField(verbose_name=_('Date of birth'), null=True, blank=True)
        image = models.ImageField(verbose_name=_('Image'), upload_to='person/', null=True, blank=True)

        def __str__(self):
            return f'{self.first_name} {self.last_name}'

        class Meta:
            verbose_name = _('Person')
            verbose_name_plural = _('People')
            unique_together = ['first_name', 'last_name']

.. code-block:: python

    from django import forms
    from .models import Person


    class PersonForm(forms.ModelForm):
        class Meta:
            model = Person
            fields = ['first_name', 'last_name']

        def clean_first_name(self):
            first_name = self.cleaned_data['first_name']

            if 'x' in first_name:
                raise forms.ValidationError("X in first_name")
            else:
                return first_name


.. code-block:: python

    from .forms import PersonForm
    from django.views.generic import FormView


    class ContactCreate(FormView):
        template_name = 'ksiazkaadresowa/create.html'
        form_class = PersonForm
        success_url = '/contact.html'

        def form_valid(self, form):
            Person.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            return super().form_valid(form)

.. code-block:: django

    <form method="post">
        {% csrf_token %}

        <table>
            {{ form.as_table }}
        </table>

        <input type="submit" value="Send message">
    </form>


Widgets
=======
.. code-block:: python

    from django.forms import ModelForm, Textarea
    from myapp.models import Author


    class AuthorForm(ModelForm):
        class Meta:
            model = Author
            fields = ('name', 'title', 'birth_date')
            widgets = {
                'name': Textarea(attrs={'cols': 80, 'rows': 20}),
            }
