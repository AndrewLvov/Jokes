#pragma once


module Fun {
    exception UnknownServerError {
    };

    exception DataNotAvailable {
    };

    interface Joke {
        idempotent string url();
        idempotent string text();
        idempotent double rating();
    };

    sequence<Joke*> JokeSeq;

    interface JokeList {
        idempotent JokeSeq all()
            throws DataNotAvailable;
    };
};