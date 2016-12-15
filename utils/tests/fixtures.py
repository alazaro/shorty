from dateutil.parser import parse


RANDOM_USER_JSON_RESPONSE = {
    "results": [
        {
            "gender": "male",
            "name": {
                "title": "mr",
                "first": "romain",
                "last": "hoogmoed"
            },
            "location": {
                "street": "1861 jan pieterszoon coenstraat",
                "city": "maasdriel",
                "state": "zeeland",
                "postcode": 69217
            },
            "email": "romain.hoogmoed@example.com",
            "login": {
                "username": "lazyduck408",
                "password": "jokers",
                "salt": "UGtRFz4N",
                "md5": "6d83a8c084731ee73eb5f9398b923183",
                "sha1": "cb21097d8c430f2716538e365447910d90476f6e",
                "sha256": "5a9b09c86195b8d8b01ee219d7d9794e2abb66"
                          "41a2351850c49c309f1fc204a0"
            },
            "dob": "1983-07-14 07:29:45",
            "registered": "2010-09-24 02:10:42",
            "phone": "(656)-976-4980",
            "cell": "(065)-247-9303",
            "id": {
                "name": "BSN",
                "value": "04242023"
            },
            "picture": {
                "large": "https://randomuser.me/api/portraits/"
                         "men/83.jpg",
                "medium": "https://randomuser.me/api/portraits/"
                         "med/men/83.jpg",
                "thumbnail": "https://randomuser.me/api/portraits"
                             "/thumb/men/83.jpg"
            },
            "nat": "NL"
        }
    ],
    "info": {
        "seed": "2da87e9305069f1d",
        "results": 1,
        "page": 1,
        "version": "1.1"
    }
}

ONE_USER_PREPARED_DATA = [{
    'date_joined': parse("2010-09-24 02:10:42 UTC"),
    'email': 'romain.hoogmoed@example.com',
    'first_name': 'romain',
    'last_name': 'hoogmoed',
    'password': 'jokers',
    'username': 'lazyduck408'
}]
