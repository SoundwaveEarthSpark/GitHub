
#Использование %
def team_member(name,team_num):
    print('В команде %s участников: %s !' % (name,team_num) )

def team_all_members(*team_num):
    print('Итого сегодня в командах участников: %s и %s !' % (team_num[0], team_num[1]))

#Использование format():
def task_count(name,score):
    print('Команда {} решила задач: {} !'.format(name,score))

def task_time(name, team_time):
    print('{} решили задачи за: {} !'.format(name,team_time))

#Использование f-строк:
def task_count_team(score_1, score_2):
    print(f'Команды решили {score_1} и {score_2} игровых задач.')

def challenge_results(name1, name2, score_1, score_2,team1_time,team2_time):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        print(f'Победа команды {name1} !')
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        print(f'Победа команды {name2} !')
    else:
        print("Ничья")


def results_of_game(team1_time, team2_time, *score):
    tasks_total = sum(score)
    time_avg = tasks_total / (team1_time + team2_time)
    print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")


name1 = 'Мастер кода'
name2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451


team_member(name1, team1_num)
team_all_members(team1_num, team2_num)


task_count(name1, score_1)
task_time(name2, team2_time)



task_count_team(score_1, score_2)

challenge_results(name1, name2, score_1, score_2, team1_time, team2_time)
results_of_game(team1_time, team2_time,score_1,score_2)
