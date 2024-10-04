#Load Files Into a DataFrame
import pandas as pd
# df = pd.read_csv(r"C:\Users\AK Sajin\Documents\Business_analyst_job_listings_linkedin.csv")

df = pd.read_csv("Business_analyst_job_listings_linkedin.csv")
print(df)
'''
                                        title       location publishedAt  \
0                             Business Analyst  United States  2024-09-04   
1    Business Analyst, CS Workforce Management  United States  2024-08-23   
2                             Business Analyst    Atlanta, GA  2024-08-02   
3                             Business Analyst      Miami, FL  2024-08-20   
4                             Business Analyst   New York, NY  2024-08-27   
..                                         ...            ...         ...   
916                 eCommerce Business Analyst    Chicago, IL  2024-07-09   
917                         Business Analyst 5    Lansing, MI  2024-06-03   
918                    Senior Business Analyst     Irving, TX  2024-09-06   
919                    Business analyst (WCAG)  United States  2024-08-30   
920      Business Analyst/Consultant-IV - 1836  United States  2024-09-05   

                   companyName  \
0                        Wipro   
1                      Netflix   
2    Donato Technologies, Inc.   
3         Carnival Cruise Line   
4              Relevante, Inc.   
..                         ...   
916                Thanx Media   
917                    My3Tech   
918        The Intersect Group   
919      Stellar Professionals   
920               Certec, Inc.   

                                           description    applicationsCount  \
0    About the Company:\n\nWipro Limited (NYSE: WIT...  Over 200 applicants   
1    Netflix is one of the world’s leading entertai...  Over 200 applicants   
2    Required Fields\n\n\n * Number of Positions re...       170 applicants   
3    Job ID 7930 Location Miami, FL Date posted 07/...  Over 200 applicants   
4    Salary: $ 130,000.00\n\nWe have partnered with...  Over 200 applicants   
..                                                 ...                  ...   
916  Job Description\n\nJob Summary\n\nThe eCommerc...       151 applicants   
917  Hello,\n\nHope you are doing good.\n\nPosition...        34 applicants   
918  Job Summary:\n\nWe are seeking a highly detail...       144 applicants   
919  We have an opening for the Business analyst(WC...       158 applicants   
920  Business Analyst/Consultant-IV\n\nJob ID: CER ...       148 applicants   

    contractType   experienceLevel  \
0      Full-time  Mid-Senior level   
1      Full-time    Not Applicable   
2      Full-time         Associate   
3      Full-time         Associate   
4      Full-time         Associate   
..           ...               ...   
916    Full-time  Mid-Senior level   
917    Full-time         Associate   
918     Contract  Mid-Senior level   
919     Contract         Associate   
920     Contract         Associate   

                                          workType  \
0                 Analyst and Health Care Provider   
1                                            Other   
2    Research, Analyst, and Information Technology   
3    Research, Analyst, and Information Technology   
4    Research, Analyst, and Information Technology   
..                                             ...   
916  Research, Analyst, and Information Technology   
917  Research, Analyst, and Information Technology   
918                                        Analyst   
919  Research, Analyst, and Information Technology   
920  Research, Analyst, and Information Technology   

                                                sector  
0                        IT Services and IT Consulting  
1                              Entertainment Providers  
2                        IT Services and IT Consulting  
3                                  Travel Arrangements  
4                                              Banking  
..                                                 ...  
916                      IT Services and IT Consulting  
917                      IT Services and IT Consulting  
918                            Staffing and Recruiting  
919  Government Administration and Government Relat...  
920                               Information Services  

[921 rows x 10 columns]
'''
