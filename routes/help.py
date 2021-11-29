from flask_restful import Resource


class Help(Resource):

    def get(self):
        return """Example settings => ?field=experience_level&filter=EN&groupby=remote_ratio&method=mean&orientation=h&x=salary_in_usd&y=remote_ratio&xlabel=Salary in USD&ylabel=Remote Ratio
        
        
        
        
        
        
        Necessary params: field, filter, groupby, x, y.
        Optional params: orientation, xlabel, ylabel, method
        The graph generated is a boxplot
        Columns = work_year, experience_level, employment_type, job_title, salary, salary_currency, salary_in_usd, employee_residence, remote_ratio, company_location and company_size
        
        
        
        
        
        
        
        
        Go to /data-science-salaries to start"""
