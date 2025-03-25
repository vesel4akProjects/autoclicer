import pyautogui as pg
from time import sleep
from win10toast import ToastNotifier
import keyboard

from pyautogui import click
pg.FAILSAFE = False

class MouseAutoClicker:
    def __init__(self,clicks,interval,button,x,y):
        self.clicks =clicks
        self.interval =interval
        self.button =button
        self.x =x
        self.y =y
        self.new_cliks = self.clicks

        print(f"Кликаю {self.clicks} раз с интервалом {self.interval} секунд на клавишу {self.button} на коордианты {self.x , self.y}")
        print("ДЛЯ ОСТАНОВКИ СКРИПТА НАЖМИТЕ КЛАВИШУ Q")


        self.timer =5
        for g in range(5):
            print(f"клики начнуться через : {self.timer} секунд")
            self.timer -=1
            sleep(1.5)


        for i in range(self.clicks):
            try:

                if keyboard.is_pressed("q"):
                    print("Клики были прерваны")
                    ToastNotifier().show_toast("Завершение программы", "Клики были прерваны")
                    return None

                pg.click(x=self.x,y=self.y,button=self.button)
                sleep(self.interval)
                self.clicks -=1
                print(f"Осталось {self.clicks} кликов")

            except:
                print("Произошла ошибка. Возможно вы ввели неконкретные данные")
                ToastNotifier().show_toast("Завершение программы","Клики были прерваны")
                return None

        print(f" {self.new_cliks} КЛИКОВ ЗАВЕРШЕНЫ")
        ToastNotifier().show_toast("Успешно!",f"{self.new_cliks} кликов заввершены")
        return None




if __name__ == "__main__":
    try:
        clicks = int(input("Привет Я - простой автокликер для мышки!Для начала введи количество кликов,которое я сделаю >>>>"))
        interval = int(input("Теперь введи интервал , с которым я буду кликать >>>>"))
        button = input("Теперь выбери клавишу мышки , на которую мне кликать:"
                       "\nleft"
                       "\nmiddle"
                       "\nright"
                       "\nНапиши название клавиши >>>>")
        x = int(input("Предпоследнее . Напиши координату по x , на которую мне кликать >>>>"))
        y = int(input("Последнее. Напиши координату по y , на которую мне кликать >>>>"))
        MouseAutoClicker(clicks,interval,button,x,y)
    except:
        print("Произошла ошибка. Возможно вы ввели неконкретные данные")
        ToastNotifier().show_toast("Завершение программы", "Клики были прерваны")
