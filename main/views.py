from accounts.models import ProjectInfo
from django.shortcuts import render, redirect, get_object_or_404
from .models import vacations
from .serializers import vacationSerializer
from rest_framework import viewsets
from .forms import VacationForm
from django.http import JsonResponse
from django.template.loader import render_to_string


class VacationViewSet(viewsets.ModelViewSet):
    queryset = vacations.objects.all().order_by('from_date_time')
    def get_queryset(self):
        return vacations.objects.filter(user_name=self.request.user).order_by('from_date_time')
    serializer_class = vacationSerializer


def index(request):
    p_info = ProjectInfo.objects.all()
    if request.user.is_authenticated:
        return render(request, 'index.html', {'p_info': p_info})
    # if not go back to login page
    else:
        return redirect('login')

def vacation_create(request):
    data = dict()
    if request.method == 'POST':
        form = VacationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)  # Return an object without saving to the DB
            obj.user_name = request.user
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False

    else:
        form = VacationForm()
    context = {
        'form': form
    }
    data['html_form'] = render_to_string('vacation_create.html', context, request=request)
    return JsonResponse(data)


def vacation_update(request):
    p_info = ProjectInfo.objects.all()
    v_id = request.GET["v_id"]
    vac_info = vacations.objects.filter(id=v_id)

    if request.user.is_authenticated:

        if request.method == 'POST':  # if user posted data and clicked on submit retrieve the below

            from_date_time = request.POST['from_date']
            to_date_time = request.POST['to_date']
            description = request.POST['vac_type']

            vacations.objects.filter(id=v_id).update(from_date_time=from_date_time, to_date_time=to_date_time, description=description)

            # messages.info(request, 'Success! Vacation Updated.')
            return redirect('index')

        return render(request, 'vacation_update.html', {'p_info': p_info, 'vac_infos': vac_info})
    # if not go back to login page
    else:
        return redirect('login')


def delete_vacation(request):
    obj = vacations.objects.get(id=request.GET["v_id"]) # Get id from link and select object
    obj.delete()
    return redirect('index')
