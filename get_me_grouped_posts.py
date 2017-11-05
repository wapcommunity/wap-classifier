# -*- coding: utf8 -*-
import nltk
from langdetect import detect
from collections import Counter

all_sharings = [
    {
        "author": "Marie Locaux",
        "sharing": "La non-scolarisation : laisser son enfant diriger ses apprentissages. D'après le documentaire Être et devenir de Clara Bellar."
    },
    {
        "author": "Clémentine Pigny",
        "sharing": "Sensibiliser des élèves de 3eme au monde de l'entreprise et de l'entreprenariat en leur faisant creer une entreprise de A à Z le temps d'une année."
    },
    {
        "author": "Roger Mazar",
        "sharing": "J'ai parlé d'une association (Énergie Jeunes) qui intervient dans les collèges REP et qui parvient en très peu de temps à avoir un très fort impact sur les élèves en stimulant l'auto-discipline."
    },
    {
        "author": "Franky Patrick",
        "sharing": """"La leçon en trois temps" méthode pour enseigner et apprendre n'importe quoi à n'importe qui"""
    },
    {
        "author": "Max ColLy",
        "sharing": "KISD est une école avant-gardiste entièrement basée sur la pédagogie project based learning."
    },
    {"author": "Samina Parisier",
     "sharing": "J'ai raconté les expériences qui m'ont mené à devenir prof de lettres classiques en collège REP. Puis j'ai raconté ce que j'y ai appris et pourquoi je m'y épanouis tellement!"
     },
    {
        "author": "Clara Sène",
        "sharing": "Ce qui m'a inspiré : les sciences cognitives pour les utiliser dans l'éducation - et développer l'esprit critique ?"
    },
    {
        "author": "Brutuus Maxime",
        "sharing": "Le mindmapping numérique permet d organiser et de reorganiser des idees efficacement ce qui en fait un outil pour prof et etudiants efficace."
    },
    {
        "author": "Anonymous",
        "sharing": "Les nounous sont peu qualifiées. Les exercices d'intelligence collective leur permet de reprendre confiance, sortir de l'isolement et aller vers la professionnalisation."
    },
    {
        "author": "Anonymous",
        "sharing": "Apprendre à travailler en Chine : projet de consulting interculturel entre français et chinois"
    },
    {
        "author": "Anthony Mesirally",
        "sharing": "Vie et croissance d'une startup en edtech"
    },
    {
        "author": "Diana Flaske",
        "sharing": "How the MBTI works : personality model that helps you know more about yourself, your strenghts and how you function in the world, and how the others are different from you (and why there are misunderstandings sometimes)"
    },
    {
        "author": "Natania Zoghby",
        "sharing": "Neurosciences et éducation"
    },
    {
        "author": "Liber K",
        "sharing": "Peer learning with WAP"
    },
    {
        "author": "Max Balo",
        "sharing": "Find what to learn next. Understand the IT job market and learn the right skills."
    },
    {
        "author": "Mariane Fazer",
        "sharing": "How volunteering in the slums in Cambodia defined my mission in life by making me switch from working in finance to promoting international mobility in education worldwide. My mission today is allowing EVERY child and student in the world to study abroad."
    },
    {
        "author": "Anne-Elise Pascal",
        "sharing": "How to produce artisanal clay (pâte à modeler): recipe, factory organisation and creative possibilities."
    },
    {
        "author": "Patrick Karri",
        "sharing": "Apprendre l'espagnol en Angleterre."
    },
    {
        "author": "Axel Farounne",
        "sharing": """
        - mettre mon "talent" d'illustratrice au service de l'éducation
	    - raconter des histoires aux enfants
	    - sensibiliser aux "bonnes pratiques" (planete, consommation,...)
	    - concevoir un outil inédit éco-conçu
	    - envoyer du courrier
	    - voir du reve et des progrès dans les yeux des kids
        """
    },
    {
        "author": "Caroline Imbert",
        "sharing": "Developper les perpsectuves d avenir des collegiens par une experience Intercative d enquetes entre collegiens et professionnels . L apprenant devient le sachant et inversement"
    },
    {
        "author": "Anonymous",
        "sharing": "Un programmr riche et collectif pour se lancer dans l entrepreneuriat"
    },
    {
        "author": "Lillianne Bouchier",
        "sharing": """Une de mes plus inspirantes rencontres, Avec Tonee NDungu, entrepreneur Kenyan fondateur de KYTABU: accès à l'éducation, numérisation de contenu, pragmatisme extrême!, neurodiversite, différenciation
	More : https://medium.com/@leadouhard/why-we-have-a-lot-to-learn-from-edtech-kenya-6353e4ca79e3"""""
    },
    {
        "author": "Anonyme",
        "sharing": "Les nounous sont peu qualifiées. Les exercices d'intelligence collective leur permettent de reprendre confiance, sortir de l'isolement et s'approprier les dispositifs de professionnalisatio"
    },
    {
        "author": "Anonymous",
        "sharing": """Redonner le goût d’apprendre grâce à ses passions !
	Un enfant révise les maths et le français grace a sa passion du foot !"""
    }
]


def get_me_grouped_categories(sharings, number_of_expected_groups, number_of_participants_per_group=6):
    dominant_language_counter = Counter()
    for post in sharings:
        post['language'] = detect(post['sharing'])
        dominant_language_counter[post['language']] += 1
        print(post)

    dominant_language = dominant_language_counter.most_common(1)[0]
    print('Dominant language :', dominant_language)


if __name__ == '__main__':
    get_me_grouped_categories(all_sharings, 1)
