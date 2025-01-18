#import directories
import pyautogui as pg
from time import sleep

#create main function

def autoclicer() -> None:
    try:
        try:
            interval =float(input("write interval"))
            clics =int(input("write quality of cliks"))
            button =str(input("write hotkey."
                              "\nleft"
                              "\nmiddle"
                              "\nright"
                              "\nwrite hotkey:"))
            try:
                interval_for_start =float(input("write timer:"))
                print(f"click {clics} with interval {interval} on hotkey {button} .")
                #main cycle
                sleep(interval_for_start)
                for i in range(clics):
                    pg.click(button=button)
                    sleep(interval)
                    print(f"remain {clics} clics")
                    clics -=1
                print("clics off!")
                return
            except ValueError:
                print("interval is invalid")
                return

        except  ValueError:
            print("invalid clics")
            return
        #if programm was turn off

    except KeyboardInterrupt:
        print("clics off")
        return

#launch

if __name__ == "__main__":
    autoclicer()
