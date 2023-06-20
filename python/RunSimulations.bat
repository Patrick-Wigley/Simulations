@ECHO OFF

if NOT EXIST "v/scripts/activate.bat" (
    echo "Must setup environment first. Setting up environment..."
    call SetupEnvironment.bat
)
@REM Create space in terminal
echo.
echo -=-=-=-=-=-=-=-=-=-

echo "Which of the following would you like to see?"
echo "[1]- Rope/Vine"
echo "[2]- Ladder"
echo "[3]- Water"

set /p "result=->:"

if %result% EQU 1 (
    "v/scripts/python" "Rope/main.py"
)
if %result% EQU 2 (
    "v/scripts/python" "Ladder/main.py"
)
if %result% EQU 3 (
    "v/scripts/python" "Water/main.py"
)
    exit

