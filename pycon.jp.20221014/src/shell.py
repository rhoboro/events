import os

def main():
    while True:
        cmdline = input("> ")
        cmd = cmdline.split()
        if not cmd:
            continue
        if cmd[0] == "quit":
            break

        pid = os.fork()
        if pid == 0:
            print("Child Process")
            os.execvp(cmd[0], cmd)
            print("Unreachable")
        else:
            print(f"Parent Process waits for {pid}")
            os.waitpid(pid, 0)
            print(f"Child Process finished")


if __name__ == "__main__":
    main()