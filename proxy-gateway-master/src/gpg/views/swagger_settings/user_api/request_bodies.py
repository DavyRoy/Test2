from drf_yasg.openapi import TYPE_OBJECT, TYPE_STRING, Schema

ERROR_RESPONSE = Schema(type=TYPE_OBJECT, properties={'error': Schema(type=TYPE_STRING, title='some_error')})
SUCCESS_RESPONSE = Schema(type=TYPE_OBJECT, properties={'success': Schema(type=TYPE_STRING, title='success')})

USER_PARTIAL_UPDATE_REQUEST_BODY = Schema(
        type=TYPE_OBJECT,
        properties={
            'role': Schema(type=TYPE_STRING, title='role'),
            'first_name': Schema(type=TYPE_STRING, title='first_name'),
            'last_name': Schema(type=TYPE_STRING, title='last_name'),
            'username': Schema(type=TYPE_STRING, title='username'),
            'email': Schema(type=TYPE_STRING, title='email'),
            'phone': Schema(type=TYPE_STRING, title='phone'),

        },

    )



