# alarm
made an raspberry alarm clock that sets off a buzzer

configured it with crontab to auto start on boot.
to do so, open up a terminal again and enter:

  >crontab -e
  >
  >@reboot python projects/startup/alarm.py

SAVE AND EXIT

  >sudo chmod +x alarm.py
  >
  >sudo reboot
