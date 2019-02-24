class User:
    name = ""
    homeworks = []

    class Homework:
        title = ""
        content = ""

        def __init__(self, title, content):
            self.title = title
            self.content = content

        def __str__(self):
            return self.title + ": " + self.content

    def __init__(self, name):
        self.name = name

    def __str__(self):
        str = self.name + ':\n'

        for homework in self.homeworks:
            str += homework + '\n'

        return str


    def add_homework(self, title, homework):
        self.homework.append({
            title: homework
        })

def init_users(user_names):
    users = []

    for name in user_names:
        users.append(User(name))

    return users