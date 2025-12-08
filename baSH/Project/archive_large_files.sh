#!/bin/bash
# =============================================================================
# Description   : Finds files larger than 50KB in a given directory (limited depth)
#                 compresses them with gzip, and moves the archives to a target folder.
# Usage         : ./archive_large_files.sh /path/to/search
# =============================================================================

# ----------------------------- Configuration ---------------------------------
# Directory where archived (.gz) files will be stored
OUT_PATH="/home/LANGUAGE/baSH/Project/Archives"

# Maximum depth for searching files (1 = current directory only)
SEARCH_DEPTH=1

# Minimum file size to consider for archiving (50KB)
# Note: find uses 'c' for bytes, so +50k = more than 50 KiB
SIZE_THRESHOLD="+50k"

# ---------------------------- Pre-flight checks ------------------------------
# Ensure an input directory was provided
if [[ $# -eq 0 ]]; then
    echo "Error: No directory provided."
    echo "Usage: $0 <directory_to_scan>"
    exit 1
fi

IN_PATH="$1"

# Check if the provided path exists and is a directory
if [[ ! -d "$IN_PATH" ]]; then
    echo "Error: Directory '$IN_PATH' not found or is not a directory."
    echo "Please check the path and try again."
    exit 1
fi

# Ensure the archive destination directory exists
if [[ ! -d "$OUT_PATH" ]]; then
    echo "Archive directory '$OUT_PATH' does not exist. Creating it..."
    mkdir -p "$OUT_PATH" || {
        echo "Error: Failed to create archive directory '$OUT_PATH'."
        exit 1
    }
    echo "Created archive directory: $OUT_PATH"
fi

# Optional: Ensure we have write permission in archive directory
if [[ ! -w "$OUT_PATH" ]]; then
    echo "Error: No write permission in archive directory '$OUT_PATH'."
    exit 1
fi

# ------------------------------- Main logic ----------------------------------
echo "Starting archive process..."
echo "Source directory : $IN_PATH"
echo "Archive location : $OUT_PATH"
echo "Size threshold   : files > 50KB"
echo "Search depth     : $SEARCH_DEPTH level(s)"
echo "=========================================================================="

# Counter for statistics
archived_count=0
failed_count=0

# Use null-delimited output to safely handle filenames with spaces/special chars
while IFS= read -r -d '' file; do
    # Extract just the filename for cleaner logs
    filename=$(basename "$file")

    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Archiving: $file"

    # Compress the file in place
    if gzip "$file"; then
        # Move the resulting .gz file to archive location
        if mv "${file}.gz" "$OUT_PATH/"; then
            echo "[$(date '+%Y-%m-%d %H:%M:%S')] Success: $filename archived."
            ((archived_count++))
        else
            echo "[$(date '+%Y-%m-%d %H:%M:%S')] Error: Failed to move ${file}.gz to $OUT_PATH"
            # Optionally ungzip on failure to restore original state
            gunzip "${file}.gz" 2>/dev/null
            ((failed_count++))
        fi
    else
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] Error: Failed to compress $file"
        ((failed_count++))
    fi

# Find files larger than 50KB, respecting maxdepth, safely handling special characters
done < <(find "$IN_PATH -maxdepth "$SEARCH_DEPTH" -type f -size "$SIZE_THRESHOLD" -print0)

# -------------------------------- Summary ------------------------------------
echo "=========================================================================="
echo "Archiving complete!"
echo "Successfully archived : $archived_count file(s)"
echo "Failed operations     : $failed_count"
echo "Archives stored in    : $OUT_PATH"

exit 0