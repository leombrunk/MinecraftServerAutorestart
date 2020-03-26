import time
import autoit
from datetime import datetime, timedelta

# Minecraft server command
server = "java -Xms1024M -Xmx2048M -jar server.jar nogui"

# Timout in seconds
timeout = 3

# Open terminal
autoit.run("cmd.exe")

# Wait for terminal to open
if(autoit.win_wait_active("[CLASS:ConsoleWindowClass]", timeout) == 0):
    raise Exception("Timed out")
else:
    # Restart server every day at 5:00am
    while(True):
        # Begin server
        autoit.win_activate("[CLASS:ConsoleWindowClass]")
        autoit.send(server)
        autoit.send("{Enter}")

        # Calculate time in seconds until shutdown
        today = datetime.today()
        print("Today is: " + str(today))
        restart = today.replace(day=today.day, hour=5, minute=0, second=0, microsecond=0) + timedelta(days=1)
        print("Restart Scheduled for: " + str(restart))
        wait = restart - today
        print("Wait Time of: " + str(wait))
        secs = wait.total_seconds()
        print("Waiting: " + str(secs) + " seconds")
        time.sleep(secs - 60)

        # Shutdown server
        autoit.win_activate("[CLASS:ConsoleWindowClass]")
        autoit.send("/say Server restart in 60 seconds")
        autoit.send("{Enter}")
        time.sleep(60)
        autoit.win_activate("[CLASS:ConsoleWindowClass]")
        autoit.send("stop")
        autoit.send("{Enter}")
        time.sleep(30)


