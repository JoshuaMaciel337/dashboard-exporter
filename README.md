
Built by https://www.blackbox.ai

---

# Dashboard Exporter

## Project Overview
Dashboard Exporter is a simple web application built using Flask that allows users to view dashboard statistics and export data to Excel files. The application is designed to provide a user-friendly interface for monitoring product stock levels and offer easy data export functionality.

## Installation

To set up the Dashboard Exporter on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/dashboard-exporter.git
   cd dashboard-exporter
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   Make sure you have `Flask` and `pandas` installed. You can install them with:
   ```bash
   pip install Flask pandas openpyxl
   ```

4. **Set your secret key in `config.py`:**
   Open `config.py` and replace `'your-secret-key-here'` with a secure key.

5. **Run the application:**
   You can start the application by executing:
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Usage

- Navigate to the home page to view the dashboard.
- The dashboard displays various statistics about product stock levels.
- Users can click on the "Export" link to download the inventory data in an Excel format.

## Features

- View dashboard statistics including total products, critical stock, production needs, and excess stock.
- Download product data as an Excel file.
- Basic error handling for 404 and 500 errors.

## Dependencies

The project requires the following Python packages, which can be installed via pip:

- `Flask`: For building web applications.
- `pandas`: For data manipulation and analysis.
- `openpyxl`: For exporting data to Excel format.

## Project Structure

```
dashboard-exporter/
│
├── app.py              # Main application file
├── config.py           # Configuration settings
├── templates/          # HTML templates folder
│   ├── index.html      # Dashboard main page
│   ├── error.html      # Error page template
└── static/             # Static files (e.g., for downloads)
    └── exports/        # Folder for exported files
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to this project by submitting issues and pull requests. Enjoy using the Dashboard Exporter!