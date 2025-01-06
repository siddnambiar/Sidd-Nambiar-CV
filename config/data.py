import pandas as pd
from datetime import datetime

class PortfolioData:
    def get_profile(self):
        return {
            "name": "Siddhartha Nambiar, PhD",
            "title": "Senior Lead Data Scientist & Operations Research Expert",
            "bio": "Specializing in healthcare analytics, supply chain modeling, and operational efficiency optimization.",
            "contact": {
                "email": "SiddharthaNambiar@Gmail.Com",
                "website": "www.snambiar.com",
                "twitter": "@SiddNambiar"
            }
        }

    def get_news(self):
        return [
            {
                "date": "November 2024",
                "content": "Presented research on Medical Device Demand Modeling at FDA Scientific Computing Days",
                "icon": "newspaper",
                "type": "presentation"
            },
            {
                "date": "August 2024",
                "content": "Promoted to Senior Lead Scientist at Booz Allen Hamilton",
                "icon": "bullhorn",
                "type": "promotion"
            },
            {
                "date": "July 2024",
                "content": "Publication in Nature - 'Genomic data in the All of Us research program'",
                "icon": "newspaper",
                "type": "publication"
            },
            {
                "date": "June 2023",
                "content": "Publication in JAMA Network Open",
                "icon": "newspaper",
                "type": "publication"
            }
        ]

    def get_experience(self):
        return [
            {
                "title": "Senior Lead Scientist",
                "company": "Booz Allen Hamilton",
                "period": "2024-Present",
                "icon": "user-tie",
                "points": [
                    "Contributing to FDA's Office of Supply Chain Resilience (OSCR) modeling initiatives",
                    "Developing time series and Bayesian models for medical device demand forecasting",
                    "Supporting development of supply chain risk assessment frameworks",
                    "Exploring privacy-preserving record linkage (PPRL) capabilities",
                    "Researching implications of AI/ML in medical device regulatory pathways"
                ]
            },
            {
                "title": "Lead Scientist",
                "company": "Booz Allen Hamilton",
                "period": "2022-2024",
                "icon": "flask",
                "points": [
                    "Developed computational models for FDA's supply chain resilience efforts",
                    "Built hurricane scenario models for medical device demand estimation",
                    "Created data processing pipelines for medical device tracking",
                    "Implemented statistical methods for supply chain risk assessment",
                    "Collaborated with FDA stakeholders to refine modeling approaches"
                ]
            },
            {
                "title": "Data Scientist",
                "company": "Covalent Solutions LLC (NIH All of Us Research Program)",
                "period": "2021-2022",
                "icon": "database",
                "points": [
                    "Implemented privacy-preserving record linkage (PPRL) solutions",
                    "Developed data quality assessment frameworks",
                    "Analyzed health outcomes in sexual and gender minority populations",
                    "Conducted research on Hispanic health during COVID-19",
                    "Collaborated on secure data sharing methodologies"
                ]
            },
            {
                "title": "Postdoctoral Research Fellow",
                "company": "MedStar Health Research Institute",
                "period": "2020-2021",
                "icon": "microscope",
                "points": [
                    "Developed analysis pipelines for clinical data cleaning",
                    "Created computational models for cardiovascular disease research",
                    "Analyzed substance use disorder patterns",
                    "Built machine learning models for COVID-19 outcome prediction",
                    "Collaborated with clinicians on research validation"
                ]
            },
            {
                "title": "Graduate Research Assistant",
                "company": "North Carolina State University",
                "period": "2016-2020",
                "icon": "graduation-cap",
                "points": [
                    "Developed optimization models for hospital staff allocation and patient routing",
                    "Created microsimulation models for colorectal cancer screening policy analysis",
                    "Built discrete event simulation models for emergency departments",
                    "Analyzed sepsis markers using EHR data for NSF-funded research",
                    "Published research in leading healthcare and operations research journals"
                ]
            }
        ]

    def get_publications(self):
        return pd.DataFrame({
            'Year': [
                2024, 2024, 2023, 2023, 2022, 2022, 2022, 2020, 2020, 2020, 2019, 2019, 
                2018, 2018, 2016, 2014, 2013, 2012
            ],
            'Title': [
                "Medical Device Demand Modeling for Supply Chain Analysis",
                "Genomic data in the All of Us research program",
                "Prevalence of 12 common health conditions in sexual and gender minority participants",
                "Routing and staffing in emergency departments: A multiclass queueing model with workload dependent service times",
                "Dynamic simulation of social media challenge participation",
                "Triply stochastic sequential assignment problem with the uncertainty in worker survival",
                "Assessing the impact of multicomponent interventions on colorectal cancer screening through simulation",
                "Objective measures of workload in healthcare: a narrative review",
                "Evaluating diabetic retinopathy screening interventions in a microsimulation model",
                "Resource allocation strategies under dynamically changing health conditions",
                "Mailed FIT, navigation or patient reminders? Using microsimulation to inform selection of interventions",
                "Estimating the impact of insurance expansion on colorectal cancer and related costs in North Carolina",
                "On scheduling a photolithography area containing cluster tools",
                "A simulation model to assess the impact of insurance expansion on colorectal cancer screening",
                "Low-cost sensor system design for in-home physical activity tracking",
                "Towards evaluating and enhancing the reach of online health forums for smoking cessation",
                "Understanding the visualization strategies used by experts when reading mechanical part drawings",
                "Braillekey: An alternative braille text input system"
            ],
            'Journal': [
                "FDA Scientific Computing and Digital Transformation Symposium",
                "Nature",
                "JAMA Network Open",
                "IISE Transactions on Healthcare Systems Engineering",
                "Journal of Computational Social Science",
                "Optimization Letters",
                "Preventive Medicine",
                "International Journal of Health Care Quality Assurance",
                "Winter Simulation Conference (WSC)",
                "SSRN",
                "Preventive Medicine",
                "Preventive Medicine",
                "Computers & Industrial Engineering",
                "Winter Simulation Conference (WSC)",
                "IEEE Journal of Translational Engineering in Health and Medicine",
                "Network Modeling Analysis in Health Informatics and Bioinformatics",
                "IIE Annual Conference Proceedings",
                "International Conference on Intelligent Human Computer Interaction (IHCI)"
            ],
            'Link': [
                "",
                "https://www.nature.com/articles/s41586-023-06957-x",
                "https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2807788",
                "https://yunanliu.wordpress.ncsu.edu/files/2022/07/Routing-and-staffing-in-emergency-departments-A-multiclass-queueing-model-with-workload-dependent-service-times.pdf",
                "https://link.springer.com/article/10.1007/s42001-022-00177-5",
                "https://www.researchgate.net/publication/356152060_Triply_stochastic_sequential_assignment_problem_with_the_uncertainty_in_worker_survival",
                "https://www.thecommunityguide.org/findings/cancer-screening-multicomponent-interventions-colorectal-cancer.html",
                "https://pubmed.ncbi.nlm.nih.gov/31940153/",
                "https://pureadmin.qub.ac.uk/ws/portalfiles/portal/483304881/Evaluating_Screening_Strategies_for_Diabetic_Retinopathy_Final_Submission_1_.pdf",
                "https://pmc.ncbi.nlm.nih.gov/articles/PMC8759806/",
                "https://stacks.cdc.gov/view/cdc/83845",
                "https://pubmed.ncbi.nlm.nih.gov/31666187/",
                "https://pure.tue.nl/ws/portalfiles/portal/312407041/Scheduling_a_Real-World_Photolithography_Area_With_Constraint_Programming.pdf",
                "",
                "https://ieeexplore.ieee.org/document/7314874",
                "https://link.springer.com/article/10.1007/s13721-014-0057-y",
                "",
                "https://ieeexplore.ieee.org/document/6481813"
            ],
            'Abstract': [
                "Presented research on Medical Device Demand Modeling at FDA Scientific Computing Days",
                "Comprehensive genomic data from the All of Us Research Program, including whole genome sequencing and genotyping array data from diverse participants",
                "Study examining the prevalence of 12 common health conditions in sexual and gender minority participants in the All of Us research program",
                "Developed a multiclass queueing model for emergency departments considering workload-dependent service times",
                "Agent-based modeling approach to simulate social media challenge participation and examine intervention strategies",
                "Explored a triply stochastic sequential assignment problem considering uncertainty in worker survival",
                "Simulation study assessing the impact of multicomponent interventions on colorectal cancer screening rates",
                "Narrative review of objective measures of workload in healthcare settings",
                "Microsimulation model evaluating diabetic retinopathy screening interventions and their impact on patient outcomes",
                "Examined resource allocation strategies in healthcare under dynamically changing health conditions",
                "Used microsimulation to inform selection of interventions to increase colorectal cancer screening in Medicaid enrollees",
                "Population-level simulation analysis estimating the impact of insurance expansion on colorectal cancer and related costs",
                "Presented a model for optimizing the scheduling of the photolithography process in semiconductor manufacturing",
                "Developed a simulation model to assess the impact of insurance expansion on colorectal cancer screening at the population level",
                "Designed a low-cost sensor system for tracking in-home physical activity",
                "Quantitative study on the effect of engagement in online smoking cessation forums",
                "Used eye-tracking to understand visualization strategies of experts reading mechanical part drawings",
                "Developed an alternative Braille text input system for visually impaired users"
            ],
            'Authors': [
                "Nambiar, S., et al.",
                "All of Us Research Program Investigators",
                "Tran, N.K., Lunn, M.R., Schulkey, C.E., Tesfaye, S., Nambiar, S., et al.",
                "Nambiar, S., Mayorga, M.E., Liu, Y.",
                "Khasawneh, A., Chalil Madathil, K., Taaffe, K.M., Zinzow, H., Ponathil, A., Chalil Madathil, S., Nambiar, S., et al.",
                "Nambiar, S., Nikolaev, A., Pasiliao, E.",
                "Hicklin, K., O'Leary, M.C., Nambiar, S., Mayorga, M.E., Wheeler, S.B., Davis, M.M., et al.",
                "Fishbein, D., Nambiar, S., McKenzie, K., Mayorga, M., Miller, K., Tran, K., et al.",
                "Swan, B., Nambiar, S., Koutouan, P., Mayorga, M.E., Ivy, J., Fitts, E.P., Fransen, S.",
                "Nambiar, S., Mayorga, M., Capan, M.",
                "Davis, M.M., Nambiar, S., Mayorga, M.E., Sullivan, E., Hicklin, K., O'Leary, M.C., et al.",
                "Lich, K.H., O'Leary, M.C., Nambiar, S., Townsley, R.M., Mayorga, M.E., Hicklin, K., et al.",
                "Madathil, S.C., Nambiar, S., Mason, S.J., Kurz, M.E.",
                "Nambiar, S., Mayorga, M.E., O'Leary, M.C., Lich, K.H., Wheeler, S.B.",
                "Nambiar, S., Nikolaev, A., Greene, M., Cavuoto, L., Bisantz, A.",
                "Stearns, M., Nambiar, S., Nikolaev, A., Semenov, A., McIntosh, S.",
                "Nambiar, S., Madathil, K.C., Paul, M.D., Zelaya, M., Koikkara, R., Gramopadhye, A.K.",
                "Subash, N.S., Nambiar, S., Kumar, V."
            ]
        })


    def get_research_portfolio(self):
        return [
            {
                "title": "Medical Device Supply Chain",
                "period": "2022-Present",
                "description": "Contributing to FDA's Office of Supply Chain Resilience efforts to develop comprehensive understanding of medical device supply chains",
                "highlights": [
                    "Developing time series forecasting models to predict national-level medical device demand",
                    "Building Bayesian models to estimate medical device demand during hurricane scenarios",
                    "Analyzing supply chain network dynamics to assess product risk levels",
                    "Contributing to real-time monitoring systems for supply chain disruption",
                    "Supporting development of interactive dashboards for visualizing supply chain risks"
                ]
            },
            {
                "title": "Healthcare Resource Allocation",
                "period": "2016-Present",
                "description": "Optimizing healthcare resource allocation through mathematical modeling and simulation",
                "highlights": [
                    "Developed patient routing and staff allocation models to optimize workload and patient outcomes",
                    "Created COVID-19 queuing simulator for hospital capacity planning",
                    "Designed algorithms for emergency department resource optimization",
                    "Implemented machine learning models for predicting resource needs",
                    "Built interactive tools for scenario analysis and capacity planning"
                ]
            },
            {
                "title": "Modeling and Simulation",
                "period": "2016-Present",
                "description": "Developing complex simulation models for healthcare systems and disease progression",
                "highlights": [
                    "Built microsimulation models for colorectal cancer screening policy analysis",
                    "Developed diabetic retinopathy progression models incorporating insurance and screening factors",
                    "Created Bayesian models for hurricane impact assessment on healthcare systems",
                    "Designed agent-based models for disease transmission",
                    "Implemented discrete event simulation for healthcare operations"
                ]
            },
            {
                "title": "AI/ML in Healthcare",
                "period": "2020-Present",
                "description": "Working on responsible implementation of AI/ML in healthcare settings with focus on regulatory science and practical applications",
                "highlights": [
                    "Developing time series forecasting models for medical device demand",
                    "Studying regulatory considerations for AI/ML-enabled medical devices",
                    "Exploring interpretability and explainability in healthcare AI models",
                    "Contributing to discussions on AI/ML in medical device approval processes",
                    "Focusing on bridging technical implementation and practical usability"
                ]
            },
            {
                "title": "Privacy Enhancing Technology",
                "period": "2021-Present",
                "description": "Implementing and advancing privacy-preserving record linkage (PPRL) and other privacy-enhancing technologies in healthcare",
                "highlights": [
                    "Implemented PPRL solutions for the NIH All of Us Research Program",
                    "Developing PPRL capabilities at Booz Allen Hamilton for healthcare applications",
                    "Exploring advanced data linkage methodologies for healthcare datasets",
                    "Researching machine unlearning techniques for privacy preservation",
                    "Investigating novel approaches to secure multi-party computation in healthcare"
                ]
            }
        ]

    def get_skills(self):
        return {
            "core": [
                {"category": "Programming", "items": "Python, R, SQL, JavaScript"},
                {"category": "ML/AI", "items": "PyTorch, TensorFlow, scikit-learn"},
                {"category": "Cloud", "items": "AWS, Azure, GCP"}
            ],
            "methodologies": [
                {"category": "Analytics", "items": "Statistical Analysis, Time Series"},
                {"category": "Operations Research", "items": "Optimization, Queuing Theory"},
                {"category": "MLOps", "items": "CI/CD, Model Monitoring"}
            ]
        }

    def get_education(self):
        return {
            "degrees": [
                {
                    "title": "Ph.D. in Industrial and Systems Engineering",
                    "institution": "North Carolina State University",
                    "year": "2020",
                    "thesis": "Improving Hospital Operational Efficiency when Staff Workload Affects Patient Outcomes",
                    "advisor": "Dr. Maria E. Mayorga"
                },
                {
                    "title": "M.S. in Industrial Engineering",
                    "institution": "State University of New York at Buffalo",
                    "year": "2015",
                    "thesis": "Sequential Stochastic Assignment with Unknown Worker Quality",
                    "advisor": "Dr. Alexander Nikolaev"
                },
                {
                    "title": "B.Tech. in Mechanical Engineering",
                    "institution": "Indian Institute of Technology, Guwahati",
                    "year": "2013",
                    "thesis": None,
                }
            ],
            "awards": [
                {
                    "title": "Co-PI Grant",
                    "year": "2021",
                    "details": "$297,000 - DC Department of Behavioral Health"
                },
                {
                    "title": "INFORMS Health Applications Society",
                    "year": "2019",
                    "details": "Student Liaison"
                }
            ]
        }