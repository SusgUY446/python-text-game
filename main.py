# Imports

import config
import saves
import threading

# setup

save_thread = threading.Thread(target=saves.save_game)


save_thread.start()

# main loop

while True:
    pass





