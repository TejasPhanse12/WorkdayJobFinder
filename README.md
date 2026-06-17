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

## The `company_dict` Variable

The `company_dict` variable is the **heart of the WorkdayJobFinder**. It is a list of dictionaries where each entry provides the necessary metadata for the script to successfully locate and query a specific company's Workday career portal.

### Why is it important?
Workday job portals are hosted on different subdomains (environments) and use unique identifier slugs for their career sites. Without the correct configuration in `company_dict`, the script cannot construct the valid API or web URL required to fetch job listings.

### Structure Breakdown
Each dictionary in the list follows this schema:

| Key | Description | Example |
| :--- | :--- | :--- |
| `company` | The primary name of the company (used for the subdomain). | `comcast`, `walmart` |
| `env` | The specific Workday environment/instance (e.g., `wd1`, `wd5`). | `wd5`, `wd504` |
| `user_name` | The unique identifier or "slug" for the company's career portal. | `Comcast_Careers` |

### Adding New Companies
To track a new company, simply find their Workday career site URL and extract these three components to add a new entry to the list in `workday.py`.

## Future Improvements

- [ ] Automate the extraction of job listings and display them in a unified format.
- [ ] Add support for filtering by location.
- [ ] Implement a CLI interface for easier role and company management.
- [ ] Export results to a CSV or JSON file.

