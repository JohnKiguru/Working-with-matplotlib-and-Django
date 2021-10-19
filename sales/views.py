import pandas
from django.shortcuts import render
from django.views.generic import ListView

from .forms import SalesSearchForm
from .models import *
# Create your views here.
from .utils import get_chart


def sales(request):
    sales_df = None

    chart = None
    no_data = None
    search_form = SalesSearchForm(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        results_by = request.POST.get('results_by')
        print(date_from, date_to, chart_type)
        sales_qs = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        

        if len(sales_qs) > 0:
            sales_df = pandas.DataFrame(sales_qs.values())
            print(sales_df)

            sales_df['created'] = sales_df['created'].apply(lambda x: x.strftime('%d/%m/%Y'))
            sales_df.rename({'customer_id': 'customer', 'salesman_id': 'salesman', 'id': 'sales_id'}, axis=1,
                            inplace=True)




            chart = get_chart(chart_type, sales_df, results_by)

            sales_df = sales_df.to_html()

        else:
            no_data = "Apparently...no data available"

    context = {
        'search_form': search_form,

        'sales_df': sales_df,

        'chart': chart,
        'no_data': no_data

    }
    return render(request, 'sales.html',  context)
class SalesListView( ListView):
    model = Sale
    template_name = 'saleslist.html'
