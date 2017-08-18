# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CsvPasteForm
import tablib


def csv(request):
    csv_data = None
    csv_as_json = None
    csv_as_yaml = None
    csv_as_rows = None

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CsvPasteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # TODO: Wrap in exception handling. http://docs.python-tablib.org/en/latest/api/#exceptions
            # Show generic format error message
            # on form errors, if we encounter an exception here.
            try:
                if form.cleaned_data['has_headers']:
                    imported_data = tablib.Dataset().load(
                        form.cleaned_data['csv_data']
                    )
                else:
                    imported_data = tablib.Dataset().load(
                        form.cleaned_data['csv_data'],
                        headers=None
                    )
            except (tablib.UnsupportedFormat,
                    tablib.InvalidDatasetType,
                    tablib.InvalidDimensions):
                form.add_error(None, ("Sorry, I couldn't figure out how to "
                                      "properly organize the data supplied. "
                                      "This could be due to inconsistent rows/columns, "
                                      "or just a format we don't recognize."))
            else:
                csv_data = imported_data.csv
                csv_as_json = imported_data.json
                csv_as_yaml = imported_data.yaml
                csv_as_rows = repr([row for row in imported_data])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CsvPasteForm()

    return render(request, 'csv_paste/csv.html', {
        'form': form,
        'csv_data': csv_data,
        'csv_as_json': csv_as_json,
        'csv_as_yaml': csv_as_yaml,
        'csv_as_rows': csv_as_rows,
    })
