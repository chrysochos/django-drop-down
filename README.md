# Dropdown Menu Example with JavaScript

This program demonstrates how to use JavaScript to create a dropdown menu with dynamic options based on the selection from another dropdown menu.

## Installation

To use this program, follow these steps:

1. Clone the repository to your local machine:
   ```shell
   git clone <repository_url of the dropdown_menu>

2. Navigate to the project directory:
    cd dropdown_menu

3. Create a new virtual environment and activate it:
    python -m venv myenv     # Create a new virtual environment
    source myenv/bin/activate     # Activate the virtual environment (macOS/Linux)
    myenv\Scripts\activate     # Activate the virtual environment (Windows)

4. Install the required packages from the requirements.txt file:
    pip install -r requirements.txt

5. Run the populate_initial_data.py script to populate the initial data:
    python populate_initial_data.py
Note: You can modify the populate_initial_data.py script to customize the initial districts and persons according to your needs.

6. Start the Django development server:
    python manage.py runserver

7. Open a web browser and navigate to http://localhost:8000 to view the application.

## Usage
On the homepage, you will see two dropdown menus:

The first dropdown menu allows you to select a district.
The second dropdown menu will dynamically update its options based on the selected district.
Choose a district from the first dropdown menu. The second dropdown menu will update to display the corresponding persons for the selected district.

Select a person from the second dropdown menu.

You can modify the populate_initial_data.py file to add or remove districts and persons according to your requirements. After modifying the file, re-run the populate_initial_data.py script to update the data.

License
[MIT License](https://www.mit.edu/~amini/LICENSE.md)


This README.md file provides the installation steps, usage instructions, and license information for your program.

