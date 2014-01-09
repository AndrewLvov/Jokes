# -*- condig: UTF-8 -*-

from django.shortcuts import render_to_response
import Ice

Ice.loadSlice('../service/fun.ice')
import Fun

def jokes(request):
    ice = Ice.initialize()
    jokesPrx = ice.stringToProxy('JokeList:default -h localhost -p 10001')

    try:
        jokeList = Fun.JokeListPrx.checkedCast(jokesPrx).all()
    except Fun.DataNotAvailable:
        print('Exception received!')
        jokeList = []
    except Exception as e:
        jokeList = []
        # TODO(analytic): log error
        print('Something wrong!')

    ctx = {
        'jokes': jokeList,
    }

    return render_to_response('ice/jokes.html', ctx)
