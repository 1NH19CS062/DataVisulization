from doctest import OutputChecker
from turtle import color
from django.shortcuts import render
from project.models import project
import pandas as pd
from plotly.offline import plot
import plotly.express as px
# Create your views here.

def index(request):
    qs = project.objects.all()
    project_data = [
        {
            'Project': x.name,
            'Start': x.start_date,
            'Finish': x.end_date,
            'Responsible': x.responisble.username,
        }for x in qs
    ]

    df = pd.DataFrame(project_data)
    fig = px.timeline(
        df, x_start="Start",x_end="Finish",y="Project", color="Responsible"
    )

    fig.update_yaxes(autorange="reversed")
    gantt_plot = plot(fig, output_type='div')
    context = {'plot_div':gantt_plot}
    return render(request, 'index.html', context)