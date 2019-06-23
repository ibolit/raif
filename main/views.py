from django.http import HttpResponse
from django.views import View

from vector_api.api import get_word_vector


class MainView(View):
    def get(self, request):
        d1, d2 = _data_from_full_set()

        html = (
            '''<h1>Computation result:</h1>
            <p>|| x - queen || == {d1}</p>
            <p>|| x - cat   || == {d2}'''.format(d1=d1, d2=d2))

        return HttpResponse(html)


def _data_from_full_set():
    v_king = get_word_vector("король")
    v_queen = get_word_vector("королева")
    v_man = get_word_vector("мужчина")
    v_woman = get_word_vector("женщина")
    v_cat = get_word_vector("кошка")

    return _get_two_sums(v_king, v_man, v_woman, v_queen, v_cat)


def _data_from_short_set():
    v_king = get_word_vector(",")
    v_queen = get_word_vector(".")
    v_man = get_word_vector("и")
    v_woman = get_word_vector("в")
    v_cat = get_word_vector(":")
    return _get_two_sums(v_king, v_man, v_woman, v_queen, v_cat)


def _get_two_sums(v_king, v_man, v_woman, v_queen, v_cat):
    v_x = v_king - v_man + v_woman

    d1 = sum((v_x - v_queen) ** 2) ** 0.5
    d2 = sum((v_x - v_cat) ** 2) ** 0.5
    return (d1, d2)
