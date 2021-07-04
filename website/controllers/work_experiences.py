from website.models import Accomplishment, WorkExperience

work_experiences: list[WorkExperience] = [
    WorkExperience(
        title="Lead DevOps and Backend Engineer",
        company="Grove",
        start_date="September 2019",
        end_date="Present",
        accomplishments=[
            Accomplishment(
                description="Coordinated an API-first development process with customers, designers, and front-end engineers.",
            ),
            Accomplishment(
                description="Developed, documented, and tested REST APIs using FastAPI, Django, and pytest.",
            ),
            Accomplishment(
                description="Implemented robust CI/CD, unit/integration testing, A/B testing, and production-monitoring practices",
            ),
            Accomplishment(
                description="Assisted with front-end testing and debugging using React and TypeScript.",
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
                description="Developed edge and cloud-based machine-vision systems to identify and count Lygus, mites, and strawberry "
                "runners using TensorFlow and FastAPI.",
            ),
            Accomplishment(
                description="Built robust pipelines in AWS for updating the machine-vision models powering the cloud-based object "
                "detection.",
            ),
            Accomplishment(
                description="Onboarded new software engineers onto our cloud-based infrastructure.",
            ),
            Accomplishment(
                description="Worked with mechanical engineers and California strawberry growers to develop edge-computing hardware ("
                "cameras, sensors, embedded computers) for fields.",
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
                description="Assisted with testing and debugging using Angular and TypeScript.",
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
                description="Scraped and cleaned data from various industrial supplies websites using selenium and scrapy.",
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
            Accomplishment(
                description="Assisted with front-end testing and debugging using React and TypeScript.",
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
                description="Built a highly performant API to efficiently arrange variably sized pallets in box trucks using FastAPI and "
                "NumPy/SciPy.",
            ),
            Accomplishment(
                description="Developed a responsive web app and cloud architecture to support precise freight conversions and "
                "calculations.",
            ),
            Accomplishment(
                description="Worked with a UI/UX contractor to design and build the web app.",
            ),
        ],
    ),
    WorkExperience(
        title="Electrons Software Lead",
        company="Cal Poly Racing - Baja",
        start_date="August 2019",
        end_date="June 2020",
        accomplishments=[
            Accomplishment(
                description="Led the electronics team in building software for high-performance embedded systems/microcontrollers, "
                "using various sensors to gather data about the Baja vehicle.",
            ),
            Accomplishment(
                description="Conducted rigorous testing of sensors on the Baja vehicle in the field.",
            ),
            Accomplishment(
                description="Assisted in the design, prototyping, and testing of custom PCBs.",
            ),
        ],
    ),
    WorkExperience(
        title="Club President",
        company="Precision Agriculture and Automation Club",
        start_date="May 2018",
        end_date="June 2020",
        accomplishments=[
            Accomplishment(
                description="Led the robotics team in developing software and hardware solutions to various international competitions.",
            ),
            Accomplishment(
                description="Built an autonomous watermelon harvesting robot that won $5,000 at the 2018 AgBot competition.",
            ),
            Accomplishment(
                description="Built an autonomous apple harvesting robot that placed competitively at the 2019 ASABE competition.",
            ),
            Accomplishment(
                description="Assisted faculty members with student recruitment efforts.",
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
