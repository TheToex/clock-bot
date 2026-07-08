systemctl stop clock-bot
rm /etc/systemd/system/clock-bot.service
systemctl daemon-reload
rm -r /root/clock-bot
echo -e "\e[32m===Uninstallation Completed===\e[0m"