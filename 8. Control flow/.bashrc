# Customizing Git Bash prompt
PS1='\[\033[01;34m\]\W\[\033[00m\] $ '

# Function to run Python scripts without displaying the full command
runpython() {
    python "$(basename "$1")"
}
