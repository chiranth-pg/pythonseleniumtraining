school = {
    'admin': [
        {'username': 'user1', 'email1': 'user1@gmail.com'},
        {'username': 'user2', 'email2': 'user2@gmail.com'},
    ],
    'teachers': {
        'physics': [
            {'teachers_name': 'teach1', 'email': 'teacher1@gmail.com'},
            {'teachers_name': 'teach2', 'email': 'teacher2@gmail.com'},
        ],
        'maths': [
            {'teachers_name': 'math', 'email': 'mathteacher1@gmail.com'},
            {'teachers_name': 'math2', 'email': 'mathteacher2@gmail.com'},
        ]
    }
}

print(school['teachers']['physics'][1]['email'])