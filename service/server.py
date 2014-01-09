# -*- coding: UTF-8 -*-

import sys
import Ice

# Fun module is generated here from ice file
Ice.loadSlice('fun.ice')
# Now the module can be actually imported
import Fun
import pymysql

import settings


class DataNotAvailableI(Fun.DataNotAvailable):
    pass


class UnknownServerErrorI(Fun.UnknownServerError):
    pass


class JokeI(Fun.Joke):
    def __init__(self, url, text, rating=None):
        self._id = Ice.Identity()
        self._id.name = Ice.generateUUID()
        self._url = url
        self._text = text
        self._rating = rating

    def url(self, current=None):
        return self._url

    def text(self, current=None):
        return self._text

    def rating(self, current=None):
        return self._rating


class JokeListI(Fun.JokeList):
    def __init__(self, adapter, communicator):
        # content
        self._adapter = adapter
        self._communicator = communicator

    def all(self, current=None):
        jokes = []
        connect_params = {
            'charset': 'utf8',
            'use_unicode': True,
        }

        connect_params.update(settings.DB_CONFIG)

        try:
            db = pymysql.connect(**connect_params)
            cursor = db.cursor()
        except pymysql.err.OperationalError:
            raise DataNotAvailableI()

        fields = ('url', 'text', 'rating')
        query_str = """SELECT %s FROM `jokes`""" % (', '.join(fields))
        try:
            cursor.execute(query_str)
        except (pymysql.err.ProgrammingError, pymysql.err.InternalError) as e:
            raise DataNotAvailableI()
        except Exception as e:
            print("Unknown exception")
            raise DataNotAvailableI()

        for row in cursor:
            res = dict(zip(fields, row))
            j = JokeI(**res)
            casted = Fun.JokePrx.uncheckedCast(self._adapter.add(j, j._id))
            jokes.append(casted)

        cursor.close()
        db.close()

        return jokes

    def activate(self):
        self._adapter.add(self, self._communicator.stringToIdentity('JokeList'))


class Server(Ice.Application):
    def run(self, args):
        self.shutdownOnInterrupt()

        adapter = self.communicator().createObjectAdapterWithEndpoints(
            'FunAdapter', 'default -h localhost -p 10001')
        jokeList = JokeListI(adapter, self.communicator())
        jokeList.activate()

        adapter.activate()

        self.communicator().waitForShutdown()

        if self.interrupted():
            print('Shutting down')

        return 0


def main():
    app = Server()
    sys.exit(app.main(sys.argv))


main()
