# PIP Notes

Created: June 1, 2024 1:47 PM

## Quick Notes

## What is PIP?

PIP Is a recursive acronym that stands for “PIP installs Packages” or “Preferred Installer Program”. PIP is the dominant  package manager for python. It is a command-line utility that installs, updates, and uninstalls PyPI packages. It can be accessed int the terminal after adding it to your paths using “pip”. 

## **PIP Tips:**

- To check if it is installed you can run “pip —version”.
- To get the installer just run “python **get**-pip.py”. (replace python with your python path like python3 or python.exe if necessary)
- “pip install <package>” to install packages.
- “pip **install** *--upgrade pip” to update PIP.*
- *“pip uninstall <package-name>” to uninstall a package.*
- *“pip list” to list installed packages.*
- *“pip show <package-name>” to show the package details.*
- *“pip install --upgrade <package-name>” to update a specific package.*
- *“pip list --outdated” to get a list of packages you can update*
- *“pip install --upgrade” to update all packages to the latest version.*
- *To install a git directly, you can use “pip install git+<address/url>” and optionally add “@<version>” to the end to download a specific version, useful for version pinning.*

## ***PIP Virtual Environment:***

*You can create and use PIP in a virtual python environment. This is highly recommended when building a new project and I really encourage you to start any new python project this way!*

***On Windows:***

1. *Navigate to your project folder in the terminal (See navigating in windows terminal for help)*
2. *Type “python3 -m venv env”(replace python3 with your python path like python or python.exe if necessary). This will make a new virtual python environment called “env”. You can check your project folder for a folder called “env” to see if it got set up correctly.*
3. *Next run “env\Scripts\activate” to activate it. There should now be “(env)” in front of your address in the terminal. if not try “pip list” and see if it is empty. If it failed make sure to double triple check you are in the right folder. If you get an error related to your permissions you can try running PowerShell as an administrator. Do: “Get-ExecutionPolicy” to check if you now have permissions. It should respond with: RemoteSigned. If it doesn’t or, like me, you are doing it through VSCode you can change your permissions without opening a new terminal by running “Set-ExecutionPolicy RemoteSigned -Scope CurrentUser” then just type y to confirm if prompted. Check your execution policy and type “env\Scripts\activate” to activate the environment in your terminal.*

*Now any python packages you add with PIP will stay in this virtual environment. This is useful for containerization, sharing files, and is vital for docker.* 

**Managing packages in your pip virtual environment:.** 

*To make a list of all the packages you are using type “pip freeze > requirements.txt”. This will save it to a file named “requirements.txt”(Name is important). You can share this list with others so they can set up their environment the same way.  All they need to do is run “pip install -r requirements.txt”. You can get only the main packages using “pip freeze --local > requirements.txt” making it easier to manage and understand.* 

---

## Acknowledgements:

*This explanation was made with lots of help from “*[https://daily.dev/blog/pip-essentials-for-python-developers]” by “Nimrod Kramer” and borrows very heavily from it. If you find any of this information useful it is likely from Nimrod and if there are any mistakes they are wholly my own. I encourage you to read the article if you have any other questions. 

## Definitions

- **Version Pinning:** Deciding exactly what version of your packages/dependencies you are going to use to avoid problems. An important part of the  project design process for projects that may take a long time, involve larger teams, or utilize older hardware or software.
- **PyPI:** The Python Package Index. A large repository of mostly safe Python packages. While the open-source packages are reviewed by contributors and volunteers, the sheer size means that you should still be relatively cautious of malware when using less popular packages. Also remember that, just because a package is “safe” aka free of malware, it does not necessarily mean the package is “secure” and it may still leave your project open to attacks and exploits. You should be especially cautious of obscure packages or one’s you haven't reviewed thoroughly.
- **Main packages:** Packages you yourself installed, as opposed to those packages that were installed as requirements for the packages you installed.
- **Package Manager:** a language specific application that allows you to download, update, and delete packages in your environment, usually accessed through the command line.
- **Package:** A bundled sets of code and recourses distributed through a package manager.
