# WorkdayJobFinder

WorkdayJobFinder is a tool designed to help students efficiently search for job opportunities across multiple companies that use the Workday platform. Instead of visiting each company's career portal individually, this tool automates the process of querying their job boards for specific roles.

## Goal

The primary objective of this project is to streamline the job search process for students by targeting specific companies and automating the search for relevant positions (e.g., internships, analyst roles, etc.) on their Workday-hosted job sites.

## Features

- **Multi-Company Search**: Search across a predefined list of companies in one go.
- **Customizable Roles**: Easily change the target role to search for (e.g., "Software Engineer", "Data Analyst", "Intern").
- **Direct Links**: Generates direct search URLs for each company's career portal.

## Prerequisites

- Python 3.x
- `requests` library

You can install the required library using:
```bash
pip install requests
```

## Usage

1. **Configure Companies**: Open `workday.py` and add your target companies to the `company_dict` list.
2. **Set the Role**: Update the `role` variable to your desired job title.
3. **Run the Script**:
   ```bash
   python workday.py
   ```

## Configuration

Companies are stored in a list of dictionaries with the following structure:
```python
{
    "company": "company_name",
    "env": "workday_environment", # e.g., wd1, wd5
    "user_name": "careers_slug"
}
```

## Future Improvements

- [ ] Automate the extraction of job listings and display them in a unified format.
- [ ] Add support for filtering by location.
- [ ] Implement a CLI interface for easier role and company management.
- [ ] Export results to a CSV or JSON file.

