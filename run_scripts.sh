
#!/bin/bash

run_command() {
    echo "Running: $1"
    $1
    if [ $? -eq 0 ]; then
        echo "$1 executed successfully."
    else
        echo "Error occurred while executing: $1"
        exit 1  # Exit the script if an error occurs
    fi
}

python C:/Users/eric/Desktop.aff_folder/hsiav.github.io/speed_test.py/daily_update_tool/daily_update_tool/date.py
python C:/Users/eric/Desktop.aff_folder/hsiav.github.io/speed_test.py/daily_update_tool/speed_test.py
python C:/Users/eric/Desktop.aff_folder/hsiav.github.io/speed_test.py/daily_update_tool/replace.py
