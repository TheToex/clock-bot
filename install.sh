apt install python3 -y
apt install python3-venv -y 
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
touch /etc/systemd/system/clock-bot.service
echo """
[Unit]
Description=Telegram Clock Bot
After=network.target

[Service]
User=root
WorkingDirectory=/root/clock-bot
ExecStart=/root/clock-bot/venv/bin/python3 clock-bot.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
""" > /etc/systemd/system/clock-bot.service
systemctl daemon-reload
systemctl enable clock-bot
systemctl start clock-bot
echo -e "\e[32mInstallation Completed!!!\e[0m"