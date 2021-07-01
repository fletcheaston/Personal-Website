from website.models import Project

projects: list[Project] = [
    Project(
        uid="website",
        name="fletcheaston.com",
        description="A look at this website.",
        url="/website",
        html_content='<iframe class="rounded-xl self-end w-full h-96" '
        'src="/" title="fletcheaston.com"></iframe>',
    ),
    Project(
        uid="healmed",
        name="HealMed",
        description="Automating the intake process for patients in healthcare systems.",
        url="/healmed",
        html_content='<img alt="Screenshot of healmed.ai." class="rounded-xl self-end" '
        'src="/static/images/healmed/home.jpg"/>',
    ),
    Project(
        uid="grove",
        name="Grove",
        description="Networking platform for verified mental health professionals.",
        url="/grove",
        html_content='<img alt="Screenshot of joingrove.com." class="rounded-xl self-end" '
        'src="/static/images/grove/home.jpg"/>',
    ),
    Project(
        uid="assembled_supply",
        name="Assembled_supply",
        description="Industrial supply price comparison.",
        url="/assembled-supply",
        html_content='<img alt="Screenshot of assembledsupply.com." class="rounded-xl self-end" '
        'src="/static/images/assembled-supply/home.jpg") }}"/>',
    ),
    Project(
        uid="my_freight_cube",
        name="MyFreightCube",
        description="Single source for freight conversions and calculations.",
        url="/my-freight-cube",
        html_content='<img alt="Screenshot of myfreightcube.com." class="rounded-xl self-end" '
        'src="/static/images/myfreightcube/home.jpg"/>',
    ),
    Project(
        uid="lygus_monitoring",
        name="Lygus Monitoring",
        description="Counting Lygus sucked up by the bug vacuum in strawberry fields.",
        url="/lygus-monitoring",
        html_content='<img alt="Screenshot of the California Strawberry Commission logo." class="rounded-xl self-end" '
        'src="/static/images/strawberry-center/home.jpg"/>',
    ),
    Project(
        uid="baja",
        name="Baja SAE DAQ",
        description="High-performance, fault tolerant data acquisition for the Baja SAE car.",
        url="/baja-daq",
        html_content='<img alt="Picture of the Cal Poly Racing Baja SAE car." class="rounded-xl self-end"'
        ' src="/static/images/baja/home.jpg"/>',
    ),
    Project(
        uid="apple",
        name="Simulated Apple Harvester",
        description="Building a robot to autonomously harvest apples.",
        url="/apple-harvester",
        html_content='<img alt="The Cal Poly BRAE logo." class="rounded-xl self-end" '
        'src="/static/images/brae/home.jpg"/>',
    ),
    Project(
        uid="watermelon",
        name="Watermelon Harvester",
        description="Building a robot to autonomously harvest watermelons.",
        url="/watermelon-harvester",
        html_content='<img alt="The Cal Poly BRAE logo." class="rounded-xl self-end" '
        'src="/static/images/brae/home.jpg"/>',
    ),
    Project(
        uid="smartfarm",
        name="SmartFarm",
        description="Open-source Arduino-based platform for crop monitoring.",
        url="/smartfarm",
        html_content='<img alt="The Cal Poly BRAE logo." class="rounded-xl self-end" '
        'src="/static/images/brae/home.jpg"/>',
    ),
    Project(
        uid="star_thistle",
        name="Yellow Star-Thistle Killer",
        description="Automated machine for hunting and killing yellow star-thistle.",
        url="/yellow-star-thistle",
        html_content='<img alt="The Cal Poly BRAE logo." class="rounded-xl self-end" '
        'src="/static/images/brae/home.jpg"/>',
    ),
]


def list_projects() -> list[Project]:
    return projects
