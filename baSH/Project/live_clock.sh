#!/bin/bash
# =============================================================================
# Description    : Displays a live digital clock that updates every second
#                  with colorful output in the terminal.
# Usage          : Just run → bash live_clock.sh  (or ./live_clock.sh if executable)
#                  Press Ctrl+C to stop
# =============================================================================

# Define color codes (bold + color)
red=$'\e[1;31m'    # Bold red
green=$'\e[1;32m'  # Bold green
blue=$'\e[1;34m'   # Bold blue
reset=$'\e[0m'     # Reset to default color (optional, not used here)

while true         # Infinite loop to keep the clock running
do
    clear                      # Clear the screen for a clean display each second
    echo -e "$green===== CLOCK ====="  # Title in green (added -e for proper escape handling)
    echo -e "$blue$(date +%T)$reset"   # Current time in HH:MM:SS format, colored blue
    echo -e "$red=================$reset"  # Decorative line in red
    sleep 1                    # Wait 1 second before the next update
done