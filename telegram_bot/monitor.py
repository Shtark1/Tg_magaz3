import subprocess

if __name__ == '__main__':
    while True:
        try:
            subprocess.Popen(["/home/str/Tg_magaz3/.venv/bin/python", "/home/str/Tg_magaz3/start_all_bot.py"])
            # subprocess.run(["python", "start_all_bot.py"])
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Ошибка: {e}")
