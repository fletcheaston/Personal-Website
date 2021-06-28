from website.models import Skill

skills: list[Skill] = [
    Skill(
        category="Web APIs",
        technologies=[
            "Django",
            "FastAPI",
            "OepnAPI/Swagger",
            "REST",
        ],
    ),
    Skill(
        category="DevOps and Cloud Computing",
        technologies=[
            "Google Cloud Platform",
            "Amazon Web Services",
            "CI/CD pipelines (Cloud Build, CodeBuild, CodeDeploy)",
        ],
    ),
    Skill(
        category="Web Apps",
        technologies=[
            "JS",
            "CSS",
            "HTML5",
            "Jinja2 templating",
            "Django templating",
        ],
    ),
    Skill(
        category="Data Persistence",
        technologies=[
            "PostgreSQL",
            "MySQL",
            "Memcached",
            "Redis",
            "Django ORM",
            "SQLAlchemy ORM/Core",
        ],
    ),
    Skill(
        category="High Performance Computing",
        technologies=[
            "Python",
            "TensorFlow",
            "NumPy",
            "SciPy",
            "Pandas",
            "Basic C++",
        ],
    ),
    Skill(
        category="Requirements Engineering and Communication",
        technologies=[
            "JIRA",
            "Notion",
            "Slack",
            "Teams",
            "Microsoft Office",
            "Google Workspace/G-Suite",
        ],
    ),
    Skill(
        category="Robotics",
        technologies=[
            "Arduino",
            "Raspberry Pi",
            "GPS/RTK/PPK",
            "Sensor fusion systems",
            "Intermediate electrical systems knowledge",
        ],
    ),
]


def list_skills() -> list[Skill]:
    return skills
