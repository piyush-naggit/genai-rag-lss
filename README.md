Please find below the following prerequisites:

1. **Python Installation**:
   - Ensure Python is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).
   - During installation, check the option **"Add Python to PATH"** to make Python and `pip` accessible from the command line.

2. **Verify Python and pip Installation**:
   - Open **Command Prompt** and type:
     ```shell
     python --version
     pip --version
     ```
   - These commands should return the installed versions of Python and `pip`. If `pip` isn’t installed, you may need to reinstall Python, ensuring that the “Install pip” option is selected during setup.

3. **Microsoft Visual C++ Build Tools (for some packages)**:
   - Some Python packages require compilation. If you encounter errors indicating the need for Microsoft Visual C++ (e.g., "Microsoft Visual C++ 14.0 or greater is required"), you’ll need to install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
   - After installation, restart your command prompt.


4. **Updating pip (Optional)**:
   - Sometimes updating `pip` helps avoid issues. Run:
     ```shell
     python -m pip install --upgrade pip
     ```

5. **Installing Packages**:
   - After installing Python and pip on Windows, you can install the required packages by running the following command in your terminal or Command Prompt:
     ```shell
     pip install streamlit langchain langchain-community openai wikipedia chromadb tiktoken
     ```
5. **Verify Installation (Optional)**:
   - Run pip show <package_name> (e.g., pip show streamlit) to confirm each package was installed.
   
This should set up your environment.
