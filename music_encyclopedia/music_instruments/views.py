from django.shortcuts import render, get_object_or_404
from .models import Country, People, Category, Instrument


def index(request):
    # Получаем список всех стран из базы данных
    countries_list = Country.objects.all()
    # Передаем список стран в шаблон 'index.html' для рендеринга
    return render(request, 'music_instruments/index.html', {'countries_list': countries_list})


def peoples(request, country_id):
    # Получаем объект страны по её идентификатору или возвращаем 404 ошибку, если она не найдена
    country = get_object_or_404(Country, pk=country_id)
    # Фильтруем людей, связанных с выбранной страной
    people_list = People.objects.filter(id_country=country)
    # Передаем страну и список людей в шаблон 'peoples.html' для рендеринга
    return render(request, 'music_instruments/peoples.html', {'country': country, 'people_list': people_list})


def instrument_categories(request, people_id):
    people = get_object_or_404(People, pk=people_id)
    # Фильтруем категории инструментов, связанные с выбранным человеком
    categories = Category.objects.filter(people=people)
    # Передаем человека и категории в шаблон 'instrument_categories.html' для рендеринга
    return render(request, 'music_instruments/instrument_categories.html', {'people': people, 'categories': categories})


def instrument_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    # Фильтруем инструменты, связанные с выбранной категорией
    instruments = Instrument.objects.filter(category=category)
    # Передаем категорию и список инструментов в шаблон 'instrument_list.html' для рендеринга
    return render(request, 'music_instruments/instrument_list.html', {'instruments': instruments, 'category': category})


def instrument_detail(request, instrument_id):
    instrument = get_object_or_404(Instrument, pk=instrument_id)
    # Передаем инструмент в шаблон 'instrument_detail.html' для рендеринга
    return render(request, 'music_instruments/instrument_detail.html', {'instrument': instrument})
