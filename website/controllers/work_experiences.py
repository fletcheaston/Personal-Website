from website.models import Accomplishment, WorkExperience

work_experiences: list[WorkExperience] = [
    WorkExperience(
        title="Lead DevOps and Backend Engineer",
        company="Grove",
        start_date="September 2019",
        end_date="Present",
        accomplishments=[
            Accomplishment(
                description="Coordinated an API-first development process with our customers, designers, and front-end engineers.",
            ),
            Accomplishment(
                description="Developed and documented our REST APIs using Django and FastAPI.",
            ),
            Accomplishment(
                description="Implemented devops with robust CI/CD and production-monitoring practices.",
            ),
        ],
    ),
    WorkExperience(
        title="Automation Engineer",
        company="California Strawberry Commission",
        start_date="October 2019",
        end_date="Present",
        accomplishments=[
            Accomplishment(
                description="Developed machine vision systems to identify and count Lygus bugs.",
            ),
            Accomplishment(
                description="Assisted in automating the runner-cutting process for strawberries.",
            ),
            Accomplishment(
                description="Built robust machine vision pipelines in AWS for detecting Lygus bugs and strawberry runners.",
            ),
        ],
    ),
    WorkExperience(
        title="DevOps and Backend Engineering Contractor",
        company="HealMed Solutions",
        start_date="January 2021",
        end_date="June 2021",
        accomplishments=[
            Accomplishment(
                description="Worked closely with HealMed Solutions to develop HIPAA-compliant software for partnered hospital systems.",
            ),
            Accomplishment(
                description="Developed a well-documented backend in FastAPI and SQLAlchemy using a TDD process.",
            ),
            Accomplishment(
                description="Implemented devops with robust CI/CD and production-monitoring practices.",
            ),
            Accomplishment(
                description="Assisted in requirements discovery with customers.",
            ),
        ],
    ),
    WorkExperience(
        title="DevOps and Backend Engineering Contractor",
        company="Assembled Supply",
        start_date="July 2020",
        end_date="June 2021",
        accomplishments=[
            Accomplishment(
                description="Scraped and cleaned data from various industrial supplies websites.",
            ),
            Accomplishment(
                description="Built a data management system for matching items from dozens of sellers for direct price comparisons.",
            ),
            Accomplishment(
                description="Developed the backend system for an e-commerce platform, integrated with Stripe.",
            ),
            Accomplishment(
                description="Documented code and practices for other engineers and the (non-technical) CEO to follow.",
            ),
        ],
    ),
    WorkExperience(
        title="Web Development Contractor",
        company="MyFreightCube",
        start_date="October 2020",
        end_date="January 2021",
        accomplishments=[
            Accomplishment(
                description="Built a high-performant system to efficiently arrange variably sized pallets in box trucks.",
            ),
            Accomplishment(
                description="Developed a responsive web app for common freight conversions and calculations.",
            ),
            Accomplishment(
                description="Worked with a UI/UX contractor to design and build the web app.",
            ),
            Accomplishment(
                description="Completed requirements discovery with the customer.",
            ),
        ],
    ),
    WorkExperience(
        title="BRAE Undergrad Research Assistant",
        company="Cal Poly Corporation",
        start_date="May 2018",
        end_date="June 2020",
        accomplishments=[
            Accomplishment(
                description="Assisted the SmartFarm project by installing, monitoring, and analyzing data from custom Arduino boards in "
                "CSU Fresno almond orchards.",
            ),
            Accomplishment(
                description="Built an autonomous in-field platform for hosting a variety of mechanical and electrical equipment.",
            ),
            Accomplishment(
                description="Contributed to master branch of SciPy’s statistics library and development documentation.",
            ),
        ],
    ),
]


def list_work_experiences() -> list[WorkExperience]:
    return work_experiences
