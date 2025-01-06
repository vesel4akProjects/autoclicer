#import directories
import pyautogui as pg
from time import sleep

#create main function

def autoclicer() -> None:
    try:
        try:
            interval =float(input("Привет,введи интервал между кликами:"))
            clics =int(input("Теперь введи количевство кликов,которое я сделаю:"))
            button =str(input("теперь введи на какую клавишу ммне нажимать."
                              "\nleft"
                              "\nmiddle"
                              "\nright"
                              "\nНужно написать название клавишы:"))
            try:
                interval_for_start =float(input("Последнее.введи интервал перед запуском автокликера:"))
                print(f"Кликаю {clics} раз с интервалом {interval} на клавишу {button} .")
                #main cycle
                sleep(interval_for_start)
                for i in range(clics):
                    pg.click(button=button)
                    sleep(interval)
                    print(f"Осталось {clics} кликов")
                    clics -=1
                print("Клики завершены!")
                return
            except ValueError:
                print("Интервал перед запуском не может быть равен дробному значению")
                return

        except  ValueError:
            print("Количевство кликов не может быть равно дробному значению")
            return
        #if programm was turn off

    except KeyboardInterrupt:
        print("Клики были прерваны")
        return

#launch

if __name__ == "__main__":
    autoclicer()
