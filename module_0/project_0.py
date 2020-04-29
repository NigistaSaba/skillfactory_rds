def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    import numpy as np
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core(number):
    count = 1
    start = 1  
    end = 101
    guess = int()
    while number != guess:
        count += 1
        guess = int((start + end)/2)
        if number < guess:
            end = guess
        else:
            start = guess
    return count

score_game(game_core)