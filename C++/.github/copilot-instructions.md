

# Copilot Instructions for HelloWorld

-   The package `HelloWorld` is a Python Project located in the folder `HelloWorld-folder`.
-   You need to call the `Get Python Environment Information` tool on the `HelloWorld` path to get the Python executable details.
-   Substitute the Python executable you get from the `Get Python Environment Information` tool anywhere you see `<python>` in these instructions.
    -   Run command for `HelloWorld`: `<python> -m HelloWorld`
    -   Command to run tests for `HelloWorld`: `<python> -m pytest HelloWorld/tests`
-   To run an editable install for the package `HelloWorld`, use the `Install Python Package` tool with the `HelloWorld-folder` path and arguments `['-e', '.']`.
-   In the workspace `launch.json` file, configurations related to this package have the prefix `HelloWorld`.
-   The package `HelloWorld` has a defined `pyproject.toml` file that you should use and keep up to date.
