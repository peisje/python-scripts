import subprocess

def menu():
    while True:
        print("\nMENU")
        print("masafaka")
        print("1 -  (Ping)")
        print("2 -  (Tasklist)")
        print("3 - (Exit)")
        choice = input("Vali tegevus  ")

        if choice == '1':
            subprocess.run(["python", "importostime.py"])
        elif choice == '2':
            subprocess.run(["python", "tasklist.py"])
        elif choice == '3':
            print("Väljun programmist...")
            break
        else:
            print("Vigane valik. Proovi uuesti.")

menu()
