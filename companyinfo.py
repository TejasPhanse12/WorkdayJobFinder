class CompanyInfo:
    def __init__(self, company, env, user_name):
        self.company = company
        self.env = env
        self.user_name = user_name

    company_dict = [
        {"company":"comcast", "env":"wd5", "user_name":"Comcast_Careers"},
        {"company":"wexinc", "env":"wd5", "user_name":"WEXInc"},
        {"company":"idexx", "env":"wd1", "user_name":"IDEXX"},
        {"company":"abbott", "env":"wd5", "user_name":"abbottcareers"},
        #{"company":"walmart", "env":"wd504", "user_name":"WalmartExternal"},
        {"company":"huron", "env":"wd1", "user_name":"huroncareers"},
        {"company":"nvidia", "env":"wd5", "user_name":"NVIDIAExternalCareerSite"},
    ]

    role = "Data Science Analyst United States"

    def get_company_info(self):
        return self.company_dict
    
    def get_role(self):
        return self.role