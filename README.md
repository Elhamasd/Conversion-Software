# Conversion-Software
## Markdown to SCORM/PDF Beamer Converter

This application allows users to convert Markdown files into either a PDF Beamer format or SCORM packages.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python**: The application is developed in Python. You need Python 3.6 or newer, which you can download from [Python's official site](https://www.python.org/downloads/).

- **PyQt6**: The GUI is built using PyQt6, which provides the bindings for Qt6 application framework. Install it via pip:

  ```bash
  pip install PyQt6
  ```

- **Pandoc**: For Markdown to HTML/PDF conversion. Download and install from (https://pandoc.org/installing.html).
- **MikTeX**: For Markdown to PDF Beamer conversion. Download and install from MikTeX from (https://miktex.org/)

- **Jinja2**: For templating, especially for creating the SCORM manifest file.

  ```bash
  pip install Jinja2
  ```

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-repo/markdown-to-scorm-pdf.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd markdown-to-scorm-pdf
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

   -- python ScromPackage1.py


2. Use the "Upload File" button to select the Markdown file you wish to convert.

3. Choose the desired conversion format (PDF or SCORM) using the radio buttons provided.

4. Click "Convert" to start the conversion process. A progress bar will indicate the conversion status.

5. Upon completion, the application will provide options to view or save the converted file.
