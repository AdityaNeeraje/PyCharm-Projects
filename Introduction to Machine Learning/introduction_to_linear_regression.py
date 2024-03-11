import joblib
from pynput import keyboard
# We need to install plotly for graphing.py to work, because it utilizes plotly.express as px. Again, this is only for the first time

def on_press(key):
    global continue_running
    try:
        if key == keyboard.Key.esc:
            continue_running = False
            return False
        if key == keyboard.Key.enter:
            return False
        else:
            print("Please type either Enter to continue, Esc to escape.")
            return True
    except Exception as error:
        print(error)


model = joblib.load("machine_learning_model.pkl")

def check_boot_size(boot_size):
    global expected_boot_size
    while True:
        if abs(expected_boot_size - boot_size) > 2:
            if expected_boot_size - boot_size < -2:
                print(f"\nThat boot size might be too large. We recommend a boot size of {int(round(expected_boot_size))}.")
            elif expected_boot_size - boot_size > 2:
                print(f"\nThat boot size might be too small. We recommend a boot size of {int(round(expected_boot_size))}.")
            try:
                boot_size = float(input("What is the size of the boot you want to buy for your dog?\n"))
            except (TypeError, ValueError):
                while True:
                    try:
                        boot_size = float(input("Please type a valid boot size:\n"))
                        break
                    except (TypeError, ValueError):
                        pass
                check_boot_size(boot_size)
        else:
            print(f"\nThat boot size seems perfect. Thank you for shopping with us!\n\n")
            break

continue_running = True
while continue_running:
    try:
        try:
            harness_size = float(input("What is the size of the harness you want to buy for your dog?\n"))
        except (TypeError, ValueError):
            while True:
                try:
                    harness_size = float(input("\nPlease type a valid harness size:\n"))
                    break
                except (TypeError, ValueError):
                    pass
        try:
            boot_size = float(input("\nWhat is the size of the boot you want to buy for your dog?\n"))
        except (TypeError, ValueError):
            while True:
                try:
                    boot_size = float(input("\nPlease type a valid boot size:\n"))
                    break
                except (TypeError, ValueError):
                    pass
        expected_boot_size = round(model.predict({"harness_size": [harness_size]})[0], 2)
        check_boot_size(boot_size)
        print("Press Enter to continue, Esc to escape.")
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        break
