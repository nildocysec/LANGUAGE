#!/bin/bash
# =============================================================================
# Description    : Creates a new Linux user with auto-generated password
#                  and forces password change on first login
# Usage          : sudo bash create_user.sh username Optional Full Name
# =============================================================================

# Step 1: Check if script is run as root (needs sudo)
if [[ $UID -ne 0 ]]
then
    echo "Error: Please run this script with sudo!"
    echo "Example: sudo bash $0 $@"
    exit 1
fi

# Step 2: Check if username is given
if [[ $# -lt 1 ]]then
    echo "Error: Username missing!"
    echo ""
    echo "Correct usage:"
    echo "   sudo bash $0 username \"Full Name or Comment (optional)\""
    echo ""
    echo "Examples:"
    echo "   sudo bash $0 john"
    echo "   sudo bash $0 priya \"Priya Sharma - Student\""
    exit 1
fi

# Step 3: Take username from first argument
USERNAME=$1
echo "Creating user: $USERNAME"

# Step 4: Take remaining words as comment (like full name)
shift                  # remove username from list
COMMENTS="$*"          # everything left = comment
if [[ -n "$COMMENTS" ]]; then
    echo "Comment     : $COMMENTS"
else
    echo "Comment     : (none)"
fi

# Step 5: Generate simple but strong random password
# Using date + nanoseconds + random = good enough for beginners
PASSWORD=$(date +%s%N | sha256sum | head -c 12)
# This makes a 12-character strong password every time

echo "Generated Password: $PASSWORD"
echo "========================================"

# Step 6: Create the user with home folder and comment
useradd -m -c "$COMMENTS" "$USERNAME"

# Check if user was created successfully
if [[ $? -ne 0 ]]then
    echo "Failed to create user $USERNAME. Try another name."
    exit 1
fi

# Step 7: Set the password (safe way)
echo "$USERNAME:$PASSWORD" | chpasswd
# Better than passwd --stdin because password doesn't show in history

# Step 8: Force user to change password on first login
passwd -e "$USERNAME"   # or: chage -d 0 "$USERNAME"

# Final success message
echo ""
echo "SUCCESS! User '$USERNAME' created!"
echo ""
echo "Login details:"
echo "   Username : $USERNAME"
echo "   Password : $PASSWORD"
echo ""
echo "User MUST change password when they login first time."
echo "========================================"

exit 0