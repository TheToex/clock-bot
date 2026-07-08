# Telegram Clock Self Bot
A simple Python self-bot that updates your Telegram last name with the current time.
## Installations
### 1. clone repository:
```bash
git clone https://github.com/TheToex/clock-bot
```
### 2. get permission
```bash
cd clock-bot
chmod +x install.sh
```
### 3. run installation script
```bash
./install.sh
```
### 4. get **API_ID** and **API_HASH** from [my.telegram.org](https://my.telegram.org/apps) and enter
### 5. select and enter your font (or Enter to use normal font)

***Available Fonts:***
> - bold :             𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗
> - outlined :         ⓪①②③④⑤⑥⑦⑧⑨
> - double_struck :    𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡
> - fullwidth :        ０１２３４５６７８９
> - sans_serif_bold :  𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵
> - monospace :        𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿
### 6. select Time Zone. Example: Europe/Rome  (or Enter to use server default timezone)
### 7. enter your phone number and wait to get Login code. (if **two-fa** enabled, you need to enter your password)
***Congratulations!🎉 The bot is installed and active. Check your Telegram profile.❤️***
## Configuration
If you want to change the Font or TimeZone after installation,you can edit the config file:
```bash
cd clock-bot
nano config.env
systemctl restart clock-bot
```

## Uninstallation
```bash
cd clock-bot
chmod +x uninstall.sh
./uninstall.sh
```
uninstallation completed.

**Disclaimer**
This project is for educational purposes only. Use it at your own responsibility.