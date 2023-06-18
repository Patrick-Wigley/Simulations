ECHO OFF
SET PY_EXE=NULL
FOR %%P IN ("py", "python", "python3.8") DO (
    %%~P --version
    IF NOT ERRORLEVEL 1 (
        SET PY_EXE=%%~P
        GOTO :setup_environment
    )
)

IF PY_EXE=NULL (
    echo "Python not installed! Exitting"
    PAUSE
    EXIT
)

:setup_environment 
    IF NOT EXIST "v/scripts/activate.bat" (
        echo "Making Virtual Environment"
        %PY_EXE% -m venv v 
        "v/scripts/python" -m pip install --upgrade pip    
    )
    GOTO :install_dependencies

:install_dependencies
    echo "Installing Required Packages"
    "v/scripts/pip" install -r requirements.txt 
    exit/b