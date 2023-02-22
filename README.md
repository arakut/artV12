1. создать локуальную дирректорию под проект
2. sudo apt update
3. sudo apt install git
4. git config --global user.email 'ваш email'
5. git config --global user.name 'ваше имя'
7. git clone https://github.com/arakut/artV12.git
8. sudo apt install -y python3-venv
9. python3 -m venv env
10. source env/bin/activate
12. sudo apt install ufw
13. sudo ufw status verbose (должно быть выключено)
14. sudo ufw enable
15. sudo ufw allow 5000
16. sudo apt install postgresql postgresql-contrib
11. pip install -r requirements.txt
19. 1) sudo -u postgres psql 
    2) \password
    3) Вводим новый пароль
    4) Сохраняем пароль и выходим обратно в терминал (Ctrl + d)
20. sudo -u postgres createdb inputs_db
21. sudo -u postgres psql -c "\l" - увидим список всех бд в postgres, где одна из них будет наша созданная
22. export FLASK_APP=main.py
23. flask db init
24. flask db migrate
25. flask db upgrade
26. flask run
