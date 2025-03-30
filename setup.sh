#!/bin/bash
#==================================================================================
#
# FILE: setup.sh
#
# USAGE: setup.sh
#
# DESCRIPTION: Linux shell script to set up python virtual environment and start
#              source and replica folders monitoring and synchronization.
# 
#==================================================================================

# Header
echo
echo " ================================="
echo "      F O L D E R   S Y N C       "
echo " ================================="
echo
echo " 1. Preparing Python virtual environment..."

# Creates and activates virtual environment
python3 -m venv .venv_folder_sync
source .venv_folder_sync/bin/activate

# Install dependencies listed in requirements.txt file
echo
echo " 2. Installing project dependencies..."
pip install --upgrade pip --quiet
pip install --no-cache-dir -r requirements.txt --quiet

# Install project package in editable mode to run test cases
pip install --editable . --quiet

# Prompt user to run unit test cases with pytest in local environment
echo
read -p " 3. Run unit tests [Y/n]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo " Running unit tests locally..."
    python3 tests/setup_teardown/folder_setup.py
    pytest tests --ignore=tests/setup_teardown -sv -rA
    python3 tests/setup_teardown/folder_teardown.py
fi

# Read running configuration from user
echo
echo " 4. Configuration"
echo 
echo "    Enter the absolute paths of"
echo
read -p "    Source dir (with trailing slash): " SOURCE_DIR
echo
read -p "    Replica dir (with trailing slash): " REPLICA_DIR
echo
read -p "    Log file: " LOG_FILE
echo
read -p "    Enter the synchronization interval (in seconds): " T_INTERVAL
echo 

# Promp user about background bot simulation
read -p " 5. Run random folder modifications by a bot user [Y/n]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo
    echo "    Starting bot user..."
    python3 tests/integration/usr_sim.py \
        --source_dir "$SOURCE_DIR" \
        --replica_dir "$REPLICA_DIR" \
        --log_file "$LOG_FILE" \
        --t_interval 5.0 &
    export BOT_PID=$!
fi

# Start folder monitoring and synchronization
echo
echo " 6. Starting folder monitoring and synchronization (Ctrl + ^ to close)..."
echo
python3 src/folder_sync/main.py \
    --source_dir "$SOURCE_DIR" \
    --replica_dir "$REPLICA_DIR" \
    --log_file "./log_bot.log" \
    --t_interval "$T_INTERVAL"

# Terminate bot if running
if ps -p $BOT_PID > /dev/null
then
   echo " 7. Terminating bot user..."
   kill -9 $BOT_PID
fi
echo " 8. Finished."
echo