sujetos = (
    "juan", " el juan","maría", "el perro", "la casa", "el sol", "la luna", "el profesor", "el estudiante",
    "la flor", "el árbol", "el coche", "el gato", "el libro", "el niño", "la niña", "el equipo",
    "la pelota", "el teléfono", "el ordenador", "la ciudad", "la montaña", "el río", "la playa",
    "el mar", "la nube", "el cielo", "la tierra", "el viento", "la lluvia", "la nieve", "el fuego",
    "el aire", "la comida", "la bebida", "el café", "el té", "el chocolate", "la leche", "el pan",
    "la carne", "la fruta", "la verdura", "el dinero", "el tiempo", "la vida", "la muerte", "la salud",
    "la enfermedad", "el amor", "el odio", "la amistad", "la familia", "el trabajo", "el descanso",
    "la felicidad", "la tristeza", "la alegría", "la sorpresa", "la emoción", "la calma", "el caos",
    "la paz", "la guerra", "el conflicto", "el problema", "la solución", "el viaje", "la aventura",
    "la experiencia", "la memoria", "el sueño", "la pesadilla", "la fantasía", "la realidad", "el recuerdo",
    "la imaginación", "la creatividad", "el arte", "la música", "el baile", "la pintura", "la escultura",
    "el cine", "la televisión", "el teatro", "la literatura", "el poema", "la novela", "el cuento",
    "la noticia", "el evento", "la celebración", "la tradición", "la costumbre", "la religión", "la creencia",
    "el dios", "la diosa", "el héroe", "la heroína", "el villano", "la villana", "el monstruo", "la monstrua",
    "el superhéroe", "la superheroína", "el animal", "la planta", "el mineral", "el ser humano", "la criatura",
    "el extraterrestre", "la máquina", "el robot", "la inteligencia artificial", "el gobierno", "la política",
    "el presidente", "la presidenta", "el líder", "la líder", "el ciudadano", "la ciudadana", "el país", "la nación",
    "el continente", "la isla", "el océano", "el planeta", "la estrella", "el cometa", "el asteroide", "la galaxia",
    "el universo", "la historia", "el pasado", "el presente", "el futuro", "la época", "el siglo", "la era", "la generación",
    "el cambio", "la transformación", "la evolución", "la revolución", "la innovación", "la tecnología", "la ciencia",
    "la investigación", "el descubrimiento", "la invención", "el avance", "la mejora", "la educación", "la enseñanza",
    "el aprendizaje", "el conocimiento", "la sabiduría", "la ignorancia", "el error", "la corrección", "la lección",
    "la prueba", "el desafío", "la dificultad", "la superación", "la victoria", "la derrota", "el logro", "la meta",
    "el objetivo", "el sueño", "la aspiración", "el deseo", "la ambición", "la pasión", "la dedicación", "el esfuerzo",
    "la perseverancia", "la paciencia", "la impaciencia", "la prisa", "la calma", "la tranquilidad", "la ansiedad",
    "el miedo", "el coraje", "la valentía", "la cobardía", "la confianza", "la duda", "la certeza", "la incertidumbre",
    "la seguridad", "la inseguridad", "la fe", "la desconfianza", "el riesgo", "la precaución"
)

articulos=("el","la","los","las","un","una","unos","unas")

verbos=(
"caminar","correr","nadar","saltar","bailar","cantar","escribir","leer","estudiar",
"aprender","enseñar","hablar","escuchar","observar","mirar","ver","sentir","tocar",
"oler","gustar","amar","odiar","querer","necesitar","desear","soñar","imaginar",
"crear","construir","destruir","comer","beber","cocinar","hornear","comprar","vender",
"gastar","ahorrar","trabajar","descansar","dormir","despertar","soñar","descubrir",
"inventar","resolver","pensar","reflexionar","recordar","olvidar","planear","organizar",
"limpiar","ordenar","decorar","dibujar","pintar","esculpir","fotografiar","filmar",
"viajar","explorar","conducir","navegar","volar","nadar","subir","bajar","correr",
"saltar","jugar","competir","ganar","perder","celebrar","luchar","gritar","llorar",
"reír","sonreír","besar","abrazar","acariciar","aplaudir","bailar","cantar","actuar",
"actuar","participar","colaborar","ayudar","apoyar","respetar","tolerar","escuchar",
"hablar","discutir","argumentar","convencer","persuadir"
)

verbos_presente=(
    "Camino","Corro","Nado","Salto","Bailo","Canto","Escribo","Leo","Estudio",
    "Aprendo","Enseño","Hablo","Escucho","Observo","Miro","Veo","Siento","Toco",
    "Huelo","Gusto","Amo","Odio","Quiero","Necesito","Deseo","Sueño","Imagino",
    "Creo","Construyo","Destruyo","Como","Bebo","Cocino","Horneo","Compro","Vendo",
    "Gasto","Ahorro","Trabajo","Descanso","Duermo","Despierto","Sueño","Descubro",
    "Invento","Resuelvo","Pienso","Reflexiono","Recuerdo","Olvido","Planeo","Organizo",
    "Limpio","Ordeno","Decoro","Dibujo","Pinto","Esculpo","Fotografío","Filmo","Viajo",
    "Exploro","Conduzco","Navego","Vuelo","Nado","Subo","Bajo","Corro","Salto","Juego",
    "Compito","Gano","Pierdo","Celebro","Lucho","Grito","Lloro","Río","Sonrío",
    "Beso","Abrazo","Acaricio","Aplaudo","Bailo","Canto","Actúo","Actúo","Participo",
    "Colaboro","Ayudo","Apoyo","Respeto","Tolero","Escucho","Hablo","Discuto","Argumento",
    "Convenzo","Persuado"
)

verbos_presente_tercera_persona = [
    "Camina", "Corre", "Nada", "Salta", "Baila", "Canta", "Escribe", "Lee", "Estudia",
    "Aprende", "Enseña", "Habla", "Escucha", "Observa", "Mira", "Ve", "Siente", "Toca",
    "Huele", "Gusta", "Ama", "Odia", "Quiere", "Necesita", "Desea", "Sueña", "Imagina",
    "Crea", "Construye", "Destruye", "Come", "Bebe", "Cocina", "Hornea", "Compra", "Vende",
    "Gasta", "Ahorra", "Trabaja", "Descansa", "Duerme", "Despierta", "Sueña", "Descubre",
    "Inventa", "Resuelve", "Piensa", "Reflexiona", "Recuerda", "Olvida", "Planea", "Organiza",
    "Limpia", "Ordena", "Decora", "Dibuja", "Pinta", "Esculpe", "Fotografía", "Filma", "Viaja",
    "Explora", "Conduce", "Navega", "Vuela", "Nada", "Sube", "Baja", "Corre", "Salta", "Juega",
    "Compite", "Gana", "Pierde", "Celebra", "Lucha", "Grita", "Llora", "Ríe", "Sonríe",
    "Besa", "Abraza", "Acaricia", "Aplauda", "Baila", "Canta", "Actúa", "Actúan", "Participa",
    "Colabora", "Ayuda", "Apoya", "Respeta", "Tolera", "Escucha", "Habla", "Discute", "Argumenta",
    "Convierte", "Persuade", "está"
]



verbos_pasado=(
"Caminó","Corrió","Nadó","Saltó","Bailó","Cantó","Escribió","Leyó","Estudió",
"Aprendió","Enseñó","Habló","Escuchó","Observó","Miró","Vio","Sintió","Tocó",
"Olió","Gustó","Amó","Odió","Quiso","Necesitó","Deseó","Soñó","Imaginó",
"Creó","Construyó","Destruyó","Comió","Bebió","Cocinó","Horneó","Compró","Vendió",
"Gastó","Ahorró","Trabajó","Descansó","Durmió","Despertó","Soñó","Descubrió",
"Inventó","Resolvió","Pensó","Reflexionó","Recordó","Olvidó","Planeó","Organizó",
"Limpió","Ordenó","Decoró","Dibujó","Pintó","Esculpó","Fotografió","Filmó",
"Viajó","Exploró","Condujo","Navegó","Voló","Nadó","Subió","Bajó","Corrió",
"Saltó","Jugó","Compitió","Ganó","Perdió","Celebró","Luchó","Gritó","Lloró",
"Rió","Sonrió","Besó","Abrazó","Acarició","Aplaudió","Bailó","Cantó","Actuó",
"Actuó","Participó","Colaboró","Ayudó","Apoyó","Respetó","Toleró","Escuchó",
"Habló","Discutió","Argumentó","Convenció","Persuadió"
)

verbos_futuro=(
"Caminará","Correrá","Nadará","Saltará","Bailará","Cantará","Escribirá","Leerá","Estudiará",
"Aprenderá","Enseñará","Hablará","Escuchará","Observará","Mirará","Verá","Sentirá","Tocará",
"Olerá","Gustará","Amara","Odiará","Querrá","Necesitará","Deseará","Soñará","Imaginará",
"Creará","Construirá","Destruirá","Comerá","Beberá","Cocinará","Horneará","Comprará","Venderá",
"Gastará","Ahorrará","Trabajará","Descansará","Dormirá","Despertará","Soñará","Descubrirá",
"Inventará","Resolverá","Pensará","Reflexionará","Recordará","Olvidará","Planeará","Organizará",
"Limpiará","Ordenará","Decorará","Dibujará","Pintará","Esculpirá","Fotografiará","Filmará",
"Viajará","Explorará","Conducirá","Navegará","Volara","Nadará","Subirá","Bajará","Correrá",
"Saltará","Jugará","Competirá","Ganará","Perderá","Celebrará","Luchará","Gritará","Llorará",
"Reirá","Sonreirá","Besará","Abrazará","Acariciará","Aplaudirá","Bailará","Cantará","Actuará",
"Actuará","Participará","Colaborará","Ayudará","Apoyará","Respetará","Tolerará","Escuchará",
"Hablará","Discutirá","Argumentará","Convencerá","Persuadirá", "gusta"
)

verbos_presente_continuo=(
"Caminando","Corriendo","Nadando","Saltando","Bailando","Cantando","Escribiendo",
"Leyendo","Estudiando","Aprendiendo","Enseñando","Hablando","Escuchando","Observando",
"Mirando","Viendo","Sintiendo","Tocando","Oliendo","Gustando","Amando","Odiando",
"Queriendo","Necesitando","Deseando","Soñando","Imaginando","Creando","Construyendo",
"Destruyendo","Comiendo","Bebiendo","Cocinando","Horneando","Comprando","Vendiendo",
"Gastando","Ahorrando","Trabajando","Descansando","Durmiendo","Despertando","Soñando",
"Descubriendo","Inventando","Resolviendo","Pensando","Reflexionando","Recordando",
"Olvidando","Planeando","Organizando","Limpiando","Ordenando","Decorando","Dibujando",
"Pintando","Esculpiendo","Fotografiando","Filmando","Viajando","Explorando","Conduciendo",
"Navegando","Volando","Nadando","Subiendo","Bajando","Saltando","Jugando",
"Compitiendo","Ganando","Perdiendo","Celebrando","Luchando","Gritando","Llorando","Riendo",
"Sonriendo","Besiendo","Abrazando","Acariciando","Aplaudiendo","Bailando","Cantando","Actuando",
"Actuando","Participando","Colaborando","Ayudando","Apoyando","Respetando","Tolerando","Escuchando",
"Hablando","Discutiendo","Argumentando","Convenciendo","Persuadiendo"
)

adjetivos=("Alto","feo","Bajo","Inteligente","Listo","Sabio","Astuto","Valiente","Fuerte","Débil","Rápido","Lento","Joven","Viejo","Nuevo","Antiguo","Fresco","Caliente","Frío","Alegre","Triste","Feliz","Contento","Enojado","Tranquilo","Nervioso","Aburrido","Interesante","Divertido","Serio","Gracioso","Formal","Informal","Complicado","Sencillo","Rico","Pobre","Generoso","Egoísta","Amable","Grosero","Educado","Maleducado","Cálido","Gélido","Cortés","Descortés","Paciente","Impaciente","Organizado","Desorganizado")

def mostrar(lista):
    for x in  lista:
        print(x)

r=input("introduce un enunciado\n").lower() + " "

#sesacaelsujeto
for x in  sujetos:
    if x in r:
        sujeto=x
        break

predicado=r.replace(sujeto,"")

#sacalosariculos
articulos_enunciado=[]
for x in  articulos:
    if x in r:
        articulos_enunciado.append(x)

#sacalosverbos
verbos_enunciado=[]

for x in verbos:#infinitivo
    if " " + x.lower() + " " in r:
        verbos_enunciado.append(x)

for x in verbos_pasado:#pasado
    if " " + x.lower() + " " in r:
        verbos_enunciado.append(x.lower())

for x in verbos_futuro:#futuro
    if " " + x.lower() + " " in r:
        verbos_enunciado.append(x.lower())

for x in verbos_presente_continuo:#presentecontinuo
    if " " + x.lower() + " " in r:
        verbos_enunciado.append(x.lower())

for x in verbos_presente:#presente
    if " " + x.lower() + " " in r:
        verbos_enunciado.append(x.lower())
        
for x in verbos_presente_tercera_persona:#presente tercera persona
    if " " + x.lower() + " " in r:
        verbos_enunciado.append(x.lower())

#adjetivos
adjetivos_enunciado=[]
for x in adjetivos:
    if " " + x.lower() + " " in r:
        adjetivos_enunciado.append(x.lower())
        
print(verbos_enunciado)

print("estos son los datos recopilados\n")
print("sujeto: ",sujeto)
print("predicado: ",predicado)
print("articulos: ")
mostrar(articulos_enunciado)
print()
print("verbos: ")
mostrar(verbos_enunciado)
print()
print("adjetivos: ")
mostrar(adjetivos_enunciado)
print()