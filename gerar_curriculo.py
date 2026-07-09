
from jinja2 import Environment, FileSystemLoader



dados_curriculo = {
    "nome": "Luiza Campos",
    "cargo": "Estagiária em Tecnologia da Informação.",
    "perfil": (
        "Estudante de Engenharia de Software focada em desenvolvimento de aplicações "
        "robustas de backend e IA. Experiência em Python, desenvolvimento de APIs "
        "RESTful e automação de processos."

    ),

    "contato": {
        "localizacao": "Brasília-DF",
        "email": "luiza.campossouza.25@gmail.com",
        "linkedin": "https://www.linkedin.com/in/luiza-campos-731a6a248/",
        "github": "https://github.com/EsterLuiza25",
        "portfolio": "https://esterluiza25.github.io/portfolio/"

    },

    "experiencias": [

        {

            "cargo": "Estagiária de Tecnologia da Informação",
            "empresa": "AGU - Advocacia-Geral da União",
            "periodo": "- Presente",
            "descricao": "Integração com a equipe de sistemas em desenvolvimento, atuando na sustentabilidade e evolução dos ecosistemas."

        },

        {

            "cargo": "Residente automação de processos e IA",
            "empresa": "Cogmo Technology",
            "periodo": "- presente",
            "descricao": "Desenvolvimento end-to-end de aplicações web e APIs. Fluxos para agentes de IA e uso de Codex para engenharia de prompt, otimização e revisão de código."

        }

    ],

    "voluntario": [

        {

            "local": "Universidade Projeção - Guará 2",
            "descricao": "Atuação na logística, contagem e triagem de doações. Proposição de estratégia de engajamento estudantil homologada pela coordenação, resultando no aumento expressivo de volume de arrecadação."

        }

    ],

    "competencias": [

        "Python, noções em Java, noções em JavaScript",
        "FastAPI, Django REST framework (DRF)",
        "SQL, PostgreSQL, GIT e GitHub"

    ],

    "idiomas": {

        "Português": "Nativo",
        "Inglês": "Intermediário"

    },

    "formacao": [

        {

            "curso": "Bacharelado em Engenharia de Software (3º semestre)",
            "instituicao": "Faculdade Projeção",
            "periodo": "Em curso (2028)"

        }

    ],

    "projetos": [

        {

            "nome": "SafeGuard ID",
            "descricao": "Sistema de middleware antifraude utilizando microsserviços em Django, focado em análise de risco preditiva e validação de dados.",
            "tecnologias": ["Python", "Django", "REST API", "Docker"]

        },

        {

            "nome": "InnovaBank API",
            "descricao": "API centralizada para gerenciamento de portfólio de projetos de TI, com controle de autenticação JWT e persistência em PostgreSQL.",
            "tecnologias": ["Django REST Framework", "PostgreSQL", "JWT"]

        }

    ],

    "certificados": [

        {

            "nome": "Técnico em Inteligência Artificial (1200h)",
            "detalhes": "SENAC - Serviço Nacional de Aprendizagem Comercial (Em andamento)"

        },

        {

            "nome": "Programador Full Stack (640h)",
            "detalhes": "SENAI - Serviço Nacional de Aprendizagem Industrial (Em andamento)"

        },

        {

            "nome": "Desenvolvimento de Software Backend (200h)",
            "detalhes": "IFB - Instituto Federal de Brasília"

        }

    ]

}



def gerar_html():

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    html_renderizado = template.render(dados=dados_curriculo)

    for arquivo in ('index.html', 'curriculo.html'):
        with open(arquivo, 'w', encoding='utf-8') as f:
            f.write(html_renderizado)

    print("Currículo gerado com sucesso!")


if __name__ == "__main__":

    gerar_html()
