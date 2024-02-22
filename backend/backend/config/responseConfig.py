resStatus = {
    'dataFound': {
        'status': 'CM200',
        'message': "Data retrived successfully!"
    },
    'dataNotFound': {
        'status': 'CM404',
        'message': "Data Not Found!"
    },
    'serverError': {
        'status': 'CM500',
        'message': "Something went wrong!"
    },
    'created': {
        'status': 'CM201',
        'message': 'Data created successfully!'
    },
    'createdFailed': {
        'status': 'CM400',
        'message': 'Failed to create data!'
    },
    'updated': {
        'status': 'CM200',
        'message': 'Data updated successfully!'
    },
    'updateFailed': {
        'status': 'CM400',
        'message': 'Failed to update data!'
    },
    'registered': {
        'status': 'CM201',
        'message': 'Registration successfull!'
    },
    'registrationFailed': {
        'status': 'CM400',
        'message': 'Failed to register!'
    },
    'login': {
        'status': 'CM200',
        'message': 'Login successfull!'
    },
    'loginFailed': {
        'status': 'CM400',
        'message': 'Invlaid email or password!'
    },
    'invalidInput': {
        'status': 'CM422',
        'message': 'Invlaid email or password!'
    },
}


def resBody(payload={}, status=200, error=None,  message=None):
    return {
        "status": status["status"],
        "payload": payload,
        "message": message or status["message"],
        "error": error
    }
