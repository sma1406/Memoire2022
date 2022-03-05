from itertools import count
import json
import spacy

with open('Sceaux_byzantins_v5.json') as json_file:
    data = json.load(json_file)
print(data)

class Seal:
    # Compteur des instances
    _ids = count(0)
    # Constructeur de la classe Seal
    def __init__(self, filename):
        self.id = next(self._ids)
        self.filename = filename # Attribut d'instance
        self.jsonObject = None
        
    
    def createInstance(self):
        inst = (":sceau" + str(self.id) + " rdf:type owl:EntitesNommees ,\n" +
                "\t"*4 + ":Sceau ;\n")
        with open(self.filename, 'r', encoding="utf-8") as jsonFile:
            self.jsonObject = json.load(jsonFile)
            jsonFile.close()
            pairs = self.jsonObject()
            for key, value in pairs:
                if key not in ['Revers','Avers']:
                    inst += ("\t"*2 + "wdt:" + key + " \"" + value + "\" ;" + "\n")
        
        nlp = spacy.load("en_core_web_sm")
        '''if 'Obverse' in self.jsonObject:
            obverse = nlp(self.jsonObject['Obverse'])
            for w in obverse.ents:
                if w.label_ == 'PERSON':
                    inst += ("\t"*2 + ":represents :" + w.text.replace(" ", "_") + str(self.id) + " ;" + "\n")'''
         
        titre = nlp(self.jsonObject['Titre'])
        for w in titre.ents:
            if w.label_ == 'DATE':
                 inst += ("\t"*2 + ":appartient_a :" + w.text.replace(" ", "_") + " ;" + "\n")
    
        return inst + "\n"*2

def createPrefixes():
    prefixes = ("@prefix : <http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux> .\n" +
    "@prefix p: <http://www.wikidata.org/prop/> .\n" +
    "@prefix ic: <http://iconclass.org/> .\n" +
    "@prefix pq: <http://www.wikidata.org/prop/qualifier/> .\n" +
    "@prefix ps: <http://www.wikidata.org/prop/statement/> .\n" +
    "@prefix wd: <http://www.wikidata.org/entity/> .\n" +
    "@prefix aat: <http://vocab.getty.edu/aat/> .\n" +
    "@prefix gvp: <http://vocab.getty.edu/ontology#> .\n" +
    "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n" +
    "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n" +
    "@prefix tgn: <http://vocab.getty.edu/tgn/> .\n" +
    "@prefix wdt: <http://www.wikidata.org/prop/direct/> .\n" +
    "@prefix xml: <http://www.w3.org/XML/1998/namespace> .\n" +
    "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n" +
    "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n" +
    "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n" +
    "@prefix ulan: <http://vocab.getty.edu/ulan/> .\n" +
    "@prefix schema: <http://schema.org/> .\n" +
    "@base <http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux> .\n\n" +
    "<http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux> rdf:type owl:Ontology .\n\n")
    return prefixes


def createObjectProperties():
    # belongsTo, represents, holds...
    objectProperties = ("")
    # ...
    return objectProperties

def createDataProperties():
    # Image, ImageReverse, Name, Obverse...
    dataProperties = ("###  http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux#Materiaux\n" +
                      ":Materiaux rdf:type owl:DatatypeProperty ;\n" +
                      "\t"*2 + "rdfs:domain :Sceau ;\n" +
                      "\t"*2 + "rdfs:range xsd:string ." + "\n"*3 +
                      "###  http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux#Inventaire\n" +
                      ":Inventaire rdf:type owl:DatatypeProperty ;\n" +
                      "\t"*2 + "rdfs:domain :Sceau ;\n" +
                      "\t"*2 + "rdfs:range xsd:string ." + "\n"*3 +
                      "###  http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux#Collection\n" +
                      ":Collection rdf:type owl:DatatypeProperty ;\n" +
                      "\t"*2 + "rdfs:domain :Sceau ;\n" +
                      "\t"*2 + "rdfs:range xsd:string ." + "\n"*3+
                      "###  http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux#Periode\n" +
                      ":Periode rdf:type owl:DatatypeProperty ;\n" +
                      "\t"*2 + "rdfs:domain :Sceau ;\n" +
                      "\t"*2 + "rdfs:range xsd:string ." + "\n"*3+
                      "###  http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux#Mention_obligatoire\n" +
                      ":Mention_obligatoire rdf:type owl:DatatypeProperty ;\n" +
                      "\t"*2 + "rdfs:domain :Sceau ;\n" +
                      "\t"*2 + "rdfs:range xsd:string ." + "\n"*3+
                      "###  http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux#Avers\n" +
                      ":Avers rdf:type owl:DatatypeProperty ;\n" +
                      "\t"*2 + "rdfs:domain :Sceau ;\n" +
                      "\t"*2 + "rdfs:range xsd:string ." + "\n"*3+
                      "###  http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux#Revers\n" +
                      ":Revers rdf:type owl:DatatypeProperty ;\n" +
                      "\t"*2 + "rdfs:domain :Sceau ;\n" +
                      "\t"*2 + "rdfs:range xsd:string ." + "\n"*3+
                      "###  http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux#Description\n" +
                      ":Description rdf:type owl:DatatypeProperty ;\n" +
                      "\t"*2 + "rdfs:domain :Sceau ;\n" +
                      "\t"*2 + "rdfs:range xsd:string ." + "\n"*3+
                      "###  http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux#Bibliographie\n" +
                      ":Bibliographie rdf:type owl:DatatypeProperty ;\n" +
                      "\t"*2 + "rdfs:domain :Sceau ;\n" +
                      "\t"*2 + "rdfs:range xsd:string ." + "\n"*3)
                      
    
    # ...
    return dataProperties

def createClasses():
    # Century, Objet, Person, Seal...
    classes = ("###  http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux#Date\n" +
               ":Date rdf:type owl:Class ." + "\n"*3 +
               "###  http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux#Titre\n" +
               ":Titre rdf:type owl:Class ." + "\n"*3 +
               "###  http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux#Dignites\n" +
               ":Dignites rdf:type owl:Class ." + "\n"*3 +
               "###  http://www.semanticweb.org/asmac/ontologies/2022/2/OntologieSceaux#Sceau\n" +
               ":Sceau rdf:type owl:Class ." + "\n"*3)
    # ...
    return classes
