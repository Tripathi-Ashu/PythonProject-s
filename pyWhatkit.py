from plyer import notification
import time


if __name__ == '__main__':
    while True:
        notification.notify(
             title="*** Take Rest***",
             message ="I am Ashutosh Tripathi",
             app_icon = "C:\Users\Ashutosh tripathi\Desktop\Python\Rest.png",  # Assuming Rest.ico is the icon file
             timeout=5
        )
        time.sleep(5)


     
    