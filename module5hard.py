from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def get_info(self):
        return self.nickname, self.password

    def __str___(self):
        return f'{self.nickname} - {self.age}'

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __repr__(self):
        return self.nickname

class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.get_info() == (nickname, hash(password)):
                self.current_user = user
                return user

        print('Неверный логин или пароль')

    def register(self, nickname, password, age):
        user_new = User(nickname, password, age)
        if user_new not in self.users:
            self.users.append(user_new)
            self.log_in(nickname, password)
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        self.current_user = None


    def add(self, *more_videos):
        for v2 in more_videos:
            if not any(v1.title == v2.title for v1 in self.videos):
                self.videos.append(v2)

    def get_videos(self, word):
        search_video = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                search_video.append(video.title)
        return search_video

    def watch_video(self, film_name):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == film_name:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                else:
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(f'Сейчас вы на {video.time_now} минуте видео')
                        sleep(0.1)
                    video.time_now = 0
                    print("Конец видео")
                    return
        else:
            print('Видео не найдено')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')