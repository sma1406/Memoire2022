from CodeCreationInstances import *
import os

onto = createPrefixes()
onto += ("#################################################################\n" +
         "#    Object Properties\n" +
         "#################################################################\n\n" +
         createObjectProperties())
onto += ("#################################################################\n" +
         "#    Data properties\n" +
         "#################################################################\n\n" +
         createDataProperties())
onto += ("#################################################################\n" +
         "#    Classes\n" +
         "#################################################################\n\n" +
         createClasses())
#onto += ("#################################################################\n" +
        #"#    Individus\n" +
         #"#################################################################\n\n")

filepath = "Sceaux_byzantins_v5.json"
#files = os.listdir(filepath)
#files.sort(key=lambda x:int(x[:-5]))

i = 0

seal = Seal(filepath)
onto += seal.createInstance()
i = i + 1

# Générer TTL
with open('OntologieSceaux1.ttl', 'w', encoding="utf-8") as writer:
    writer.write(onto)
