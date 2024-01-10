# STATO AVANZAMENTO LAVORI

L’obbiettivo è di creare un sistema che possa interagire automaticamente con diversi dispositivi IoT, usando sia Alexa sia controllando automaticamente le app di controllo di tali dispositivi.
A tal proposito ti chiederei di dare un’occhiata alle metodologie esistenti su Android per poter controllare un’applicazione (tipo monkey / monkeyrunner).
Obbiettivo iniziale: dato un dispositivo IoT (es. una lampadina controllabile a distanza) e la relativa App, scrivere del codice che controlli automaticamente la lampadina tramite App (installata su smartphone o meglio su un emulatore android).

# INCONTRO FEBRUARY 18TH, 2022

## PRESENTI: Fabio

## PUNTI SALIENTI:
1. Raccogliere informazioni su Stato dell’Arte
2. Capire come poter usare un sistema android (e.g. emulazione, device fisico, su virtualbox)
3. capire possibili metodologie per creare un sistema che interagisce in automatico con l’app di un dispositivo intelligente.

## NOTE:
Credenziali per il controllo della lampadina tramite applicazione Tapo: *CHECK CREDENTIALS*

## DOMANDE

## PUNTO 1
- [x] Collezionare i vari  paper.
- [x] Dividere i paper in cluster.
- [x] Chiedere a Fabio come proseguire.

## OBIETTIVO
Stato dell’Arte sui sistemi per automatizzare il testing di un’applicazione android. Questo ci serve per automatizzare il processo di interazione Utente + APP dispositivo IOT con il dispositivo stesso. Facendo ciò successivamente sarà possibile fare lo spoofing dell’interazione tra APP e IOT device e collezionare grossi Dataset di traffico da poter analizzare per indagini in ambito IOT Forensics.

## PAROLE CHIAVE - LINKS

### IOT FORENSICS
~~[A Survey on the Internet of Things (IoT) Forensics: Challenges, Approaches, and Open Issues](https://ieeexplore.ieee.org/document/8950109)~~

**[Forensic Analysis of digital evidence extracted from Amazon Echo](https://ieeexplore.ieee.org/document/9398391)**

**[Towards Labeling On-Demand IoT Traffic](https://doi.org/10.1145/3474718.3474727)**

**[Simulation of Smart Home Activity Datasets](https://doi.org/10.3390/s150614162)**

### FRAMEWORK RESEARCH CURRENT STATE OF THE ART
**[An empirical study of Android test generation tools in industrial cases](https://doi.org/10.1145/3238147.3240465)**

**[Seven reasons why: an in-depth study of the limitations of random test input generation for Android](https://doi.org/10.1145/3324884.3416567)**

**[On the Energy Footprint of Mobile Testing Frameworks](https://doi.org/10.1109/TSE.2019.2946163)**

**Android Ripper [1](https://ieeexplore.ieee.org/abstract/document/6494930),[2](https://github.com/reverse-unina/AndroidRipper),[3](https://ieeexplore.ieee.org/document/6405345),[4](https://ieeexplore.ieee.org/abstract/document/6786194)**

**[Continuous, Evolutionary and Large-Scale: A New Perspective for Automated Mobile App Testing](https://doi.org/10.1109/ICSME.2017.27)**

**[A general framework for comparing automatic testing techniques of Android mobile apps](https://doi.org/10.1016/j.jss.2016.12.017)**

**[The iMPAcT Tool for Android Testing](https://doi.org/10.1145/3300963)**

**[Automated Testing of Android Apps: A Systematic Literature Review](https://doi.org/10.1109/TR.2018.2865733)**

**Mobicomonkey: context testing of Android apps [1](https://doi.org/10.1145/3197231.3197234),[2](https://github.com/LordAmit/mobile-monkey)**

**[Capture-Replay Testing for Android Applications](https://doi.org/10.1109/IS3C.2014.293)**

**[An analysis of automated tests for mobile Android applications](https://doi.org/10.1109/CLEI.2016.7833334)**

**[CrashScope: A Practical Tool for Automated Testing of Android Applications](https://doi.org/10.1109/ICSE-C.2017.16)**

**[Automated Mobile Testing as a Service (AM-TaaS)](https://doi.org/10.1109/SERVICES.2015.20)**

**[Automated Testing of Mobile Applications using Scripting Technique: A Study on Appium](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.1049.9945&rep=rep1&type=pdf)**

**[Novel Framework for Automation Testing of Mobile Applications using Appium](https://www.mecs-press.org/ijmecs/ijmecs-v9-n2/v9n2-4.html)**

**[Practical GUI Testing of Android Applications Via Model Abstraction and Refinement](https://doi.org/10.1109/ICSE.2019.00042)**

**[Guided, stochastic model-based GUI testing of Android apps](https://github.com/tingsu/Stoat)**

**[Record and replay for Android: are we there yet in industrial cases?](https://doi.org/10.1145/3106237.3117769)**

**[Paladin: Automated Generation of Reproducible Test Cases for Android Apps](https://doi.org/10.1145/3301293.3302363)**

**[Practical Android Test Recording with Espresso Test Recorder](https://doi.org/10.1109/ICSE-SEIP.2019.00029)**

**[Sara: self-replay augmented record and replay for Android in industrial cases](https://doi.org/10.1145/3293882.3330557)**

**[SmartDroid: an automatic system for revealing UI-based trigger conditions in android applications](https://doi.org/10.1145/2381934.2381950)**

**[MT4A: a no-programming test automation framework for Android applications](https://doi.org/10.1145/2994291.2994300)**

**[Barista: A Technique for Recording, Encoding, and Running Platform Independent Android Tests](https://doi.org/10.1109/ICST.2017.21)**

**[AppFlow: using machine learning to synthesize robust, reusable UI tests](https://doi.org/10.1145/3236024.3236055)**

**[Automated test input generation for android: towards getting there in an industrial case](https://doi.org/10.1109/ICSE-SEIP.2017.32)**

**[A reinforcement learning based approach to automated testing of Android applications](https://doi.org/10.1145/3278186.3278191)**

**[Segen: generation of test cases for selenium and selendroid](https://doi.org/10.1145/3011141.3011154)**

**[Research on Mobile Application Automation Testing Technology Based on Appium](https://doi.org/10.1109/ICVRIS.2019.00068)**

**[Humanoid: a deep learning-based approach to automated black-box Android app testing](https://doi.org/10.1109/ASE.2019.00104)**

## DIVIDI I PAPER IN CLUSTER
- scelta phisical device vs virtualbox con su iso android x86 ??
- scelta tool di GUI Automation tra quelli selezionati foss e sviluppati dai ricercatori ??
- usare un tool scrivendo il codice oppure usare un tool di record and replay
- machine learning technique per riprodurre UI Tests
- molti paper trattano (monkey, ui automator, monkeyrunner), appium, espresso


# INCONTRO MARCH 17TH, 2022

## PRESENTI: Fabio

## PUNTI SALIENTI:
Dopo che hai guardato una serie di tool per generare automaticamente delle interazioni con le app android ti direi di mettere in pratica uno dei metodi che hai trovato e vedere quanto possa funzionare.
Se tra virtualizzato e device fisico non c'è differenza ti direi che non cambia molto per le prime fasi puoi provare come ti viene meglio. 
Il traffico che andiamo a generare lo catturiamo con dei tool simili a wireshark e poi lo analizziamo con un tool che ne estragga delle caratteristiche per un approccio orientato al Machine Learning, ma questo sarà un passo futuro.
Ti direi di effettuare qualche prova e poi ci riaggiorniamo in chiamata o in persona anche con il prof, così se ci sono decisioni da prendere le facciamo insieme. 
Riguardo la 40ina di paper non credo sia necessario che tu li legga tutti, sono decisamente tanti.
Ti direi di scremarli guardando abstract/conclusioni e rimuovendo quelli che ti sembrano poco sensati.

## OBIETTIVO

## AUTOMATED UI TEST TOOLS
Dato che svilupperemo per Android partiamo dal suo IDE, Android Studio, e vediamo cosa offre lato AUTOMATED UI TESTING

## HOW TO TEST APPS ANDROID STUDIO / CLI USER GUIDE: [https://developer.android.com/studio/test](https://developer.android.com/studio/test) ##
Description of the various tools that help you create, configure, and run your tests from Android Studio or the command line.

## TEST IN ANDROID STUDIO 
basic testing, constraint => you need the source code of the app to be tested.

## TEST FROM THE COMMAND LINE
mode fine-grained control testing, but same constraint of previous point.

## ADVANCING TEST SETUP
to override default settings, configure Gradle options, or refactor your code so that tests are separated in their own module.

## OTHER TESTING TOOLS

### Espresso Test Recorder: [https://developer.android.com/studio/test/other-testing-tools/espresso-test-recorder](https://developer.android.com/studio/test/other-testing-tools/espresso-test-recorder)
### FUNZIONA SOLO SU NUOVE APP SVILUPPATE TRAMITE ANDROID STUDIO, NON PERMETTE DI ISPEZIONARE APP PREESISTENTI
The Espresso Test Recorder tool lets you create UI tests for your app without writing any test code.
\
By recording a test scenario, you can record your interactions with a device and add assertions to verify UI elements in particular snapshots of your app.
\
Espresso Test Recorder then takes the saved recording and automatically generates a corresponding UI test that you can run to test your app.
\
Espresso Test Recorder writes tests based on the [Espresso Testing framework](https://developer.android.com/training/testing/espresso), an API in AndroidX Test.
\
The Espresso API encourages you to create concise and reliable UI tests based on user actions.
\
By stating expectations, interactions, and assertions without directly accessing the underlying app’s activities and views, this structure prevents test flakiness and optimizes test run speed.
\
constraint => you need the source code to build of the app to be testedi

### App Crawler: [https://developer.android.com/studio/test/other-testing-tools/app-crawler](https://developer.android.com/studio/test/other-testing-tools/app-crawler)
To automatically test your app without the need to write or maintain any code.
\
The crawler runs alongside your app, automatically issuing actions (tap, swipe, etc.) to explore the state-space of your app.
\
The crawl terminates automatically when there are no more unique actions to perform, the app crashes, or a timeout you designate is reached.
\
constraint => you need the source code to build of the app to be tested
\
**ESPRESSO TEST RECORDER NEEDS USER TO INTERACT WITH THE BUILT APP IN ORDER TO GENERATE THE TEST CODE.**
\
**APP CRAWLER INSPECTS AUTOMAGICALLY THE BUILT APP AND DISCOVERS VALID ACTIONS TO BE EXECUTED.**

### Monkey Testing: [https://developer.android.com/studio/test/other-testing-tools/monkey](https://developer.android.com/studio/test/other-testing-tools/monkey)
The Monkey is a program that runs on your emulator or device and generates pseudo-random streams of user events such as clicks, touches, or gestures, as well as a number of system-level events. You can use the Monkey to stress-test applications that you are developing, in a random yet repeatable manner.
\
You can launch the Monkey using a command line on your development machine or from a script. Because the Monkey runs in the emulator/device environment, you must launch it from a shell in that environment. You can do this by prefacing adb shell to each command, or by entering the shell and entering Monkey commands directly.
\
With no options specified, the Monkey will launch in a quiet (non-verbose) mode, and will send events to any (and all) packages installed on your target. Here is a more typical command line, which will launch your application and send 500 pseudo-random events to it.
\
Working on seed values it seems to create a deterministic pseudo-random events:
\
e.g. connect device to Wi-Fi (it is the first time, pair it through android studio, i guess that would be the chance to pair it through adb, but this must be investigated more in detail)
\
`adb start-server`
\
`adb shell monkey -s 1 1` -> Apre Orologio su timer
\
`adb shell monkey -s 2 1` -> Apre Office
\
`adb shell monkey -s 3 1` -> Apre MobilePASS+
\
`adb shell monkey -s 4 1` -> Apre Spazio AR
\
`adb shell monkey -s 5 1` -> Apre Gmail
\
`adb kill-server`
\
With monkey command, you can increase the probability of certain events with percent value. Use Monkey-runner for a deterministic behaviour
\
[https://stackoverflow.com/questions/31431200/example-for-using-monkey-command-with-almost-all-options-in-android](https://stackoverflow.com/questions/31431200/example-for-using-monkey-command-with-almost-all-options-in-android)

### MonkeyRunner **(deprecated)**: [https://developer.android.com/studio/test/monkeyrunner](https://developer.android.com/studio/test/monkeyrunner)
Used to perform Monkey testing with python scripts.
\
The monkey tool runs in an adb shell directly on the device or emulator and generates pseudo-random streams of user and system events.
\
In comparison, the monkeyrunner tool controls devices and emulators from a workstation by sending specific commands and events from an API.
\
The monkeyrunner tool provides these unique features for Android testing:
* Multiple device control
* Functional Testing
* Regression Testing
* Extensible automation
The monkeyrunner tool uses Jython, an implementation of Python that uses the Java programming language.
\
Jython allows the monkeyrunner API to interact easily with the Android framework.
\
With Jython you can use Python syntax to access the constants, classes, and methods of the API.
\
[https://stackoverflow.com/questions/15579328/how-to-run-monkeyrunner-on-an-already-installed-apk](https://stackoverflow.com/questions/15579328/how-to-run-monkeyrunner-on-an-already-installed-apk)
\
[https://stackoverflow.com/questions/12698814/get-launchable-activity-name-of-package-from-adb](https://stackoverflow.com/questions/12698814/get-launchable-activity-name-of-package-from-adb)
\
Monkeyrunner is being replaced by UI AUTOMATOR Tool.
\
e.g.
\
`create monkeyrunner.py`
\
`monkeyrunner monkeyrunner.py`

### UI AUTOMATOR: [https://developer.android.com/training/testing/other-components/ui-automator](https://developer.android.com/training/testing/other-components/ui-automator)
UI Automator is a UI testing framework suitable for cross-app functional UI testing across system and installed apps.
The UI Automator APIs let you interact with visible elements on a device, regardless of which Activity is in focus, so it allows you to perform operations such as opening the Settings menu or the app launcher in a test device.
Your test can look up a UI component by using convenient descriptors such as the text displayed in that component or its content description.
UI Automator and Espresso have some feature overlap but Espresso has more synchronization mechanisms so it's preferred for common UI tests.

### Espresso: [https://developer.android.com/training/testing/espresso](https://developer.android.com/training/testing/espresso)

**ANDROID STUDIO AUTOMATED TESTING SAMPLES ESPRESSO / UI AUTOMATOR**
\
[https://github.com/android/testing-samples](https://github.com/android/testing-samples)

__(BOOKMARK)__
\
**AUTOMATE UI TESTS: [https://developer.android.com/training/testing/instrumented-tests/ui-tests](https://developer.android.com/training/testing/instrumented-tests/ui-tests)**
\
__(BOOKMARK)__

### COMPOSE: [https://developer.android.com/jetpack/compose/testing](https://developer.android.com/jetpack/compose/testing)

### APPIUM: [https://appium.io/](https://appium.io/)

### CALABASH: [https://github.com/calabash/calabash-android](https://github.com/calabash/calabash-android)
To use monkey use the bash tool adb shell monkey/adb devices.

To use the other devices create a java/kotlin test snippet in android studio and execute it in the device connected through usb cable/Wi-Fi pairing. 

## VIRTUAL / PHYSICAL

Creiamo VM con Android come OS INSTALLATION ANDROID 9.0 X86\_64: [https://i12bretro.github.io/tutorials/0258.html](https://i12bretro.github.io/tutorials/0258.html)

### ANDROID EMULATOR/DEVICE
[https://developer.android.com/studio/run/emulator](https://developer.android.com/studio/run/emulator) 
[https://developer.android.com/studio/run/device](https://developer.android.com/studio/run/device)

__USIAMO PHYSICAL DEVICE COLLEGATO AD ANDROID STUDIO__

[https://stackoverflow.com/questions/7022527/how-to-click-a-view-of-android-program-through-monkeyrunner](https://stackoverflow.com/questions/7022527/how-to-click-a-view-of-android-program-through-monkeyrunner) 

## Ridurre numero di paper

# INCONTRO APRIL 12TH, 2022

## PRESENTI: Fabio, Alessandro

## PUNTI SALIENTI:
1. 1 test con + app gestire o + test da orchestratore ognuno per 1 app o disp gestito
2. Orchestrare i test con scheduling temporale e esecuzione sequenziale per test deterministico per riprodurre comportamento umano o test random.
3. Provare a usare e creare un emulatore android anche di android studio o macchina virtuale
4. Mappare tutte le possibili interazioni che si possono avere con l'oggetto vanno mappate (e.g. x la lampadina Smart Bulb di Tapo, on/off, cambio colore e cambio luminosità.
5. Scrivere un log file con azioni automatiche che il test sta facendo x avere una GROUD TRUTH da sfruttare in seconda analisi x la parte di classificazione (e.g. TIMESTAMP APP TIPO\_ATTIVITA'

Per connettere il dispositivo all'emulatore android basta prima associarlo tramite un dispositivo hardware fisico dopo di che sara associato alla rete e si potra' proseguire dall'emulatore per tutti i test necessari.
In questo caso il primo pairing alla ret Wi-Fi viene gestito da iPhone personale. Da capire se tale pairing può essere fatto direttamente da emulatore senza passare da smartphone.

### COMMAND LINE UI INSTRUMENTED TEST
install java 11 
PROJECT\_NAME="MyApplication"
PROJECT\_PATH="/Users/angelo/AndroidStudioProjects/${PROJECT\_NAME}"
${PROJECT\_PATH}/gradlew connectedAndroidTest
${PROJECT\_PATH}/gradlew cAT
PROJECT\_SRC="/Users/angelo/AndroidStudioProjects/MyApplication/app/src/androidTest/java/com/example/myapplication"
TESTFILE="${PROJECT\_SRC}/ExampleInstrumentedTest.kt"

### First step: produce kotlin script files
### Re-engineerized the software creating classes for specific test use cases and ranmdoly run in another class test.
NB: l'app TAPO da emulatore qemu android funziona benissimo, mentre l'app EZVIZ ogni tanto in maniera casuale crasha all'avvio e dopo 3/4 tentativi si apre correttamente.
Inolte l'app EZVIZ fa fatica all'avvio quindi andrebbe verificata l'apertura della schermata iniziale e delle varie sotto schermate di gestione dei vari componenti (e.g. bulb, camera e plug) prima di iniziare con i test che generano interazioni casuali o il più causale possibile.
Per questo motivo per iniziare i test:
1. Avvio Emulatore
2. Apro le 2 applicazioni verificando che venga visualizzata la schermata HOME rispettiva e poi le lascio in background e torno nella HOME ANDDROID.
3. Faccio partire il TEST vero e proprio.
4. Ricordarsi prima di far partire il test di settare correttamente lo stato delle lampadine (TO-DO: verificare se lo stato si possa passare come parametro da cmd.

# KOTLIN COMPILER
/Users/angelo/Library/Application Support/Google/AndroidStudio2021.2/plugins/Kotlin/kotlinc/bin

# GENYMOTION (VM Virtualbox)
Tentativo fatto per verificare le prestazioni rispetto a qemu, sono simili e in più dall'App Store non è possibile scaricare le app Tapo e EZVIZ, quindi non è possibile fare i test. Opzione scartata. usa versione a 32 bit probabilmente.

# START EMULATOR QEMU FROM CMD
cd $ANDROID\_SDK/tools
./emulator -list-avds
./emulator @Automator -gpu on -no-boot-anim

# CONNECT NOX PLAYER TO ADB
adb connect 127.0.0.1:62001
adb disconnect

# INCONTRO July 12TH, 2022
## PRESENTI: Fabio

- inserire device in log file -> fatto
- tutto ok quello fatto finora
- creare classi e gestire smart plug -> fatto
- provare a usare noxplayer invece che qemu android studio -> funzione

# Per problemi DateTimeFormatter quando uso NoxPlayer che ha API 29 SDK Java
# https://stackoverflow.com/questions/52510370/java-lang-noclassdeffounderror-failed-resolution-of-ljava-time-localdate-erro#52510417

# INCONTRO July 27TH, 2022
## PRESENTI: Fabio

- aggiungere metodo che esegue le interazioni in maniera sequenziale e non random, 1 seq per tutte le interazioni. -> fatto
- preparare una guida per il nuovo device e nuova applicazione (come se chi dovesse fare questa operazione non richieda conoscenze di programmazione, o in modo tale che sia semplice questa fase evitando la complessita' e il mio sforzo). elenco puntato cose da fare per l'implementazione. provare a spostare logica implementazione su logica file di configurazione tipo yaml/json. l'unico problema in questo caso e' che bisogna definire anche le funzionalita da attivare (e.g. accendi, spegni, cambia colore, etc), e se usare i pixel, quindi la dimensione, oppure resourceID. Potrei creare uno script bash che legge il file yaml/json e crea le classi .kt. Questo e' il primo step. il secondo e' l'esecuzione. Bisogna creare anche il progetto in Android Studio prima. Creare anche un altro file di configurazione dove dici che classi instanziare e se lanciare il comando in maniera sequenziale o random. Quindi la soluzione potrebbe essere uno script bash che crea la classe .kt e poi tu la inserisci all'interno del progetto in Android Studio. Nella configurazione potrei mettere il path da eseguire per svolgere l'azione dove i nodi del grafo descrivono o un resourceid da cercare oppure dei pixel su cui cliccare (e.g. Tapo -> ALL -> Smart Bulbs -> \[10x10\]\[20x20\]) e poi specificare anche l'azione da eseguire, cioe' click,drag,swipe). Al posto delle frecce potrei anche per esempio definirli come una lista di oggetti chiave,valore da eseguire in sequenza per ottenere il risultato voluto all'interno dello yaml.
- iniziare a simulare per 24/48 ore i device vedere nel frattempo cosa succede al traffico di rete, provare a fare il test con una lampadina.
- provare a studiare il traffico in base agli eventi generati.
- installare il tutto su pc lab e lavorare in lab.

# INCONTRO September 13th, 2022
## PRESENTI: Fabio, Alessandro
1 BUG: In Tapo Bulb setPresetColor non controllavo lo stato della lampadina dopo aver cambiato colore auto.
       Bisogna riaccendere solo se si spegne a causa del path auto -> auto-compensate
2 BUG: per la lampadina EZVIZ quando facevo il click diretto dopo per esempio aver attivato lo smart plug EZVIZ avevo un errore perche'
       mi dimenticavo di cambiare il tab su Bulbs, quindi in output vedevo che cercava erroneamente di disattivare il plug dato 
	   che non cambiavo tab come scritto prima. Tale problema non si evidenzia nell'app Tato dato che ogni interazione richiede
	   l'apertura della windows Bulbs/Plug da cui si eseguono tutte le operazioni.

Effettuando un'analisi tra le azioni eseguite sugli smart devices e il log che fa da groundtruth si evidenzia una corrispondenza univoca
senza eventi mappati male o che non si correlano tra loro.

TO-DO: aggiungere l'event number nel file di log                                                                    FATTO
       randomizzare cicli che modificare colori e saturazioni facendogli scegliere un valore tra 1 e 10.            FATTO
	   randomizzare delay tra un evento e il successivo con un valore tra 1 e 5                                     FATTO
	   Tapo, valutare se randomizzare luminosita' e saturazioni, sembrano deterministiche gli eventi associati.
	   
TODO:
- creare guida per mappare smart object in android studio
- generare un evento ogni 60 secondi

2 OBIETTIVI:
ANALISI TRAFFICO
- caratterizzazione traffico in base alle interazioni tra virtual device e smart object
- trovare se esiste del traffico generato dallo smart object senza essere sollecitato dal virtual device
  possibilmente creare una rappresentazione grafica con l'asse dei tempi sulle ascisse e gli eventi sulle ordinate


## TIMEZONE
Run>Debug Configurations/Run Configurations

Tab Target> Additional Emulator Command Line Options

-timezone America/New_York
-timezone Europe/Rome

emulator -timezone Europe/Rome

C:\Users\Admin\AppData\Local\Android\Sdk\emulator>emulator.exe -timezone Europe/Rome

cambiare impostazioni da device Settings > System > Date&Time

## BUG 3
possibile inconsistenza auto-match state

quando e' selezionato di default auto-compensate e faccio auto-match ho il comportamento di auto-compensate
questo crea un'inconsistenza, proviamo a selezionare prima il bottone e poi lo clicco, o meglio a fare il focus sul bottone prima di cliccarlo.


## ORACLE ACCOUNT TO DOWNLOAD JAVA JDK 1.8
Phazard1#
angelo.re@mail.polimi.it

## BUG 4
implementare try-catch per ogni azione e scrivere nel log NOP skippando l'azione che va in errore
il try-catch implementato nei metodi centrali che eseguono il task (e.g. click, edit color) e non quelli di spostamento tra windows.
In EZVIZ non abbiamo in problema delle schermate intermedie quindi basta aggiungere i try-catch nel metodo selectRandomInstrumentedTest
In Tapo, invece abbiamo problema di schermate intermedie in enablePartyTheme enableRelaxTheme e editColor e editColorTemperature, setPresetColor

Togliere checkPopUpFeedback da schermate diverse dalla Home in Tapo.
Per Tapo associare un bool per gestire i 2 pressBackButton della openSmartPlub

in evziz non sempre rispetta i delay e non riesce a beccare i pixel corretti quando seleziona COLOR/TEMPERATURE/MODES
mettiamo un delay di 2s ad ogni azione per rallentare l'esecuzione e renderla piu' robusta.

## NOTES
1. Ogni tanto l'errore e' causato dalla rete, quindi il dispositivo risulta non raggiungibile per alcuni secondi, per poi tornare disponibile.
Compare una schermata con scritto dispositivo irraggiungibile e chiede se rimuoverlo o meno.
Questo lasso di tempo mandava in crash il test.
Sembrerebbe essere causato dal irraggiunbilita' temporanea dello smartPlug per quanto riguarda l'app Tapo.
Questo avviene sempre nella transizione da App EZVIZ a App Tapo, all'apertura della Home dell'app.

2. Dopo un po' c'e' un disallinemaneto tra lo stato reale della lampadina ezviz e lo stato tracciato dall'app.
   Lo stato tracciato e' acceso mentre quello mostrato in app e' spento.
   Nello specifico quando viene restituita l'eccezione sulla seek-bar

#  BUG 6: in EZVIZ se e' selezionata una delle editModes non e' possibile cambiare la brightness, infatti se si prova
   il comando viene ignorato. Per poterlo fare bisogna selezionare o editColorTemperature o editTemperature.

#  Il Delay delle azioni eseguite era impostato a 1s, riprovare con 2s per vedere se permette di dimunuire le eccezioni.
   Oppure in alternative settarne uno casuale tra 2s e 5s.

#  App pensate per gestire interazioni sporadiche nel tempo, noi stiamo stressando molto le applicazioni
   Testing di automazione delle app seguengo lo schema app che interagisce con gli smart object e non solo il semplice test 
   delle funzionalita' dell'app in se.

!! Provare a gestire stati smart bulb e plug in base allo stato del bottone (se checked o no) invece che gestendolo con un attributo
   da aggiornare.

## NOTES PCAP
Il tempo della trace di rete catturata e' 2 ore indietro rispetto al tempo attuale.

IP ASSEGNATI DAL ROUTER AI DISPOSITIVI
Active DHCP Leases
Hostname			IPv4 address	MAC address			Lease
Tapo\_SmartPlug			192.168.2.164	00:5F:67:BF:09:EF		tapo smartplug
CS-HAL-LB1-LCAW-		192.168.2.199	64:F2:FB:DF:FB:E1		ezviz smartbulb
Tapo\_Bulb			192.168.2.190	E8:48:B8:D6:A8:1D		tapo smartbulb
C100\_61A26E			192.168.2.244	90:9A:4A:61:A2:6E		tapo camera
T31-Q02345790.lan		192.168.2.167	64:F2:FB:48:2C:5B               ezviz smartplug


????ezviz smartplug???? anche tramite nslookup non sono riuscito a trovare il suo ip


## WIRESHARK FILTERS
ip.addr in { 192.168.2.164, 192.168.2.174, 192.168.2.190, 192.168.2.199 }
eth.addr == E8:48:B8:D6:A8:1D
eth.addr == E8:48:B8:D6:A8:1D and ip.addr not in { 52.212.233.55, 52.212.115.57, 34.241.252.94 } and not arp
### TAPO BULB
ip.dst in { 192.168.2.190 } and tls
ip.addr in { 192.168.2.174, 192.168.2.190 } and tls
ip.dst in { 192.168.2.190 } and tls and frame.len != 123 ## 123 => packet ack
ip.src eq 192.168.2.174 and ip.dst in { 52.212.233.55, 52.212.115.57, 34.241.252.94 } and tls
ip.src in { 52.212.233.55, 52.212.115.57, 34.241.252.94 } and ip.dst eq 192.168.2.174 and tls
ip.src eq 192.168.2.190 and ip.dst in { 52.212.233.55, 52.212.115.57, 34.241.252.94 } and tls
ip.src in { 52.212.233.55, 52.212.115.57, 34.241.252.94 } and ip.dst eq 192.168.2.190 and tls
### EZVIZ BULB
ip.dst in { 192.168.2.199 } and tls
ip.addr in { 192.168.2.174, 192.168.2.199 } and tls


# AWS INSTANCE
C:\Users\Admin\>nslookup 52.212.233.55
Server:  OpenWrt.lan
Address:  192.168.2.1

Name:    ec2-52-212-233-55.eu-west-1.compute.amazonaws.com
Address:  52.212.233.55

# AWS INSTANCE
C:\Users\Admin\>nslookup 52.212.115.57
Server:  OpenWrt.lan
Address:  192.168.2.1

Name:    ec2-52-212-115-57.eu-west-1.compute.amazonaws.com
Address:  52.212.115.57

# AWS INSTANCE
C:\Users\Admin\>nslookup 34.241.252.94
Server:  OpenWrt.lan
Address:  192.168.2.1

Name:    ec2-34-241-252-94.eu-west-1.compute.amazonaws.com
Address:  34.241.252.94

# NTP INSTANCE
20.101.57.9

# 
C:\Users\Admin\>nslookup 142.250.184.106
Server:  OpenWrt.lan
Address:  192.168.2.1

Name:    mil41s04-in-f10.1e100.net
Address:  142.250.184.106

# 
C:\Users\Admin\>nslookup 216.58.209.42
Server:  OpenWrt.lan
Address:  192.168.2.1

Name:    waw02s05-in-f10.1e100.net
Address:  216.58.209.42

# AWS INSTANCE
C:\Users\Admin\>nslookup 3.248.82.188
Server:  OpenWrt.lan
Address:  192.168.2.1

Name:    ec2-3-248-82-188.eu-west-1.compute.amazonaws.com
Address:  3.248.82.188

# AWS INSTANCE
C:\Users\Admin\>nslookup 54.255.151.26
Server:  OpenWrt.lan
Address:  192.168.2.1

Name:    ec2-54-255-151-26.ap-southeast-1.compute.amazonaws.com
Address:  54.255.151.26

# GOOGLE INSTANCE
C:\Users\Admin\>nslookup 35.186.224.25
Server:  OpenWrt.lan
Address:  192.168.2.1

Name:    25.224.186.35.bc.googleusercontent.com
Address:  35.186.224.25

# AWS INSTANCE
C:\Users\Admin\>nslookup 23.33.13.135
Server:  OpenWrt.lan
Address:  192.168.2.1

Name:    a23-33-13-135.deploy.static.akamaitechnologies.com
Address:  23.33.13.135

# AWS INSTANCE
C:\Users\Admin\>nslookup 108.138.199.53
Server:  OpenWrt.lan
Address:  192.168.2.1

Name:    server-108-138-199-53.mxp64.r.cloudfront.net
Address:  108.138.199.53

# AWS INSTANCE
C:\Users\Admin\>nslookup 52.212.118.190
Server:  OpenWrt.lan
Address:  192.168.2.1

Name:    ec2-52-212-118-190.eu-west-1.compute.amazonaws.com
Address:  52.212.118.190

# AWS INSTANCE
C:\Users\Admin\>nslookup 99.80.122.254
Server:  OpenWrt.lan
Address:  192.168.2.1

Name:    ec2-99-80-122-254.eu-west-1.compute.amazonaws.com
Address:  99.80.122.254

### NOTES
sembra non esserci un'interazione diretta tra app finale e smart device ma la richiesta viene intermediata da aws che la prende in carico e poi manda la risposta allo smart device.
evidentemente tp-link/ezviz hostano il loro servizio su aws.
FILTRO: per IP o mac di destinazione associato al dispositivo per vedere cosa riceve e quando.

### ANALISI TEMPORALE
Analisi temporale sfruttando il tool di openwrt the estrae le features dalle trace di rete filtrando per mac
Usiamo finestre temporali di 0.5s e plottiamo sulla x il tempo in secondi per 2 giorni e sulla y il numero totale di pacchetti/il numero totale di bytes associati ai pacchetti (questo puo' anche essere fatto in python, una sorta di pre-trasformazione del dataset).
Scartare momentaneamente la presa EZVIZ dai grafici dato che il suo traffico era finito su una rete separata e non e' stato catturato nella trace di rete.
Il tool di openwrt non considera il payload dei pacchetti ma solo l'overhead.
Il traffico generato dallo Smartplug Ezviz non e' all'interno delle 4 trace di rete catturate dato che era erroneramente configurato su un'altra rete locale.
Il traffico generato dagli altri 3 device e' all'interno delle trace raccolte finora.

# INCONTRO October, 04 2022
## PRESENTI: Fabio
- Openwrt Traffic Feature Capture window max 10s long
- Grafici OK, win di 0.5s OK
- Fare Guida per il 17 Ottobre su come aggiungere nuovi dispositivi OK
- Commentare il codice OK
- Leggere paper "Towards Automatic Identiﬁcation and Blocking of Non-Critical IoT Traffic Destinations" OK
- Provare a fare script che legge yaml e crea classe kotlin in automatico (future works)

# INCONTRO October, 18 2022
## PRESENTI: Fabio, Alessandro
- Analizzare il traffico ottenuto OK
- Fare grafici traffico con sankey tool. I grafici devono essere per device quindi filtrero' per MAC Adress o IP Address e mostrero' il traffico degli eventi non correlati agli eventi scatenati dall'automazione androidtest, per capire a cosa e' dovuto questo traffico aggiuntivo. Produrre un primo grafico con tutto il traffico partendo da IP.SRC collegato a TCP.PORT e collegato a IP.DST. Poi cercare una strategia per filtrare il traffico generato da eventi effettivamente generati (per esempio adottare una sorta di finestratura intorno all'evento evidenziato nel gtfile.csv di un certo valore di secondi - 1s, 2s, 5s) in modo tale da considerare come traffico collegato ad eventi e traffico spontaneo.
- Iniziare a preparare scaletta tesi in overleaf in modo tale da mandare i capitoli direttamente a Fabio una volta scritti per le correzioni OK
- Use obj.exists() or obj.waitForExists(timeout) UI Automator per skippare popup o network problems o disallineamenti smart device - emulated app. OK
- il sistema e' containerizzabile ? (future works)
- implementare un controllo sul package attualmente visualizzato e capire l'azione da eseguire (future works).
- Specificare in experimental results tesi, possibili problemi nei confronti delle altre soluzioni trovate in altri paper. Per esempio quando scateno un evento tramite il selector nell'emulatore in android studio e non viene prodotto traffico per errori lato aws. Le situazioni possono essere 3.
  1. Genero un evento e viene prodotto traffico che fa cambiare stato allo smart device.
  2. Non genero nessun evento e viene prodotto traffico spontaneo. Nessuna transizione di stato.
  3. Genero un evento e non viene prodotto traffico di rete (errore su aws), con conseguente mancata transizione di stato. Si crea un disallineamento tra stato app e stato device (possibili lavori futuri -> trovare il modo di garantire che la transizione sia avvenuta a seguito di un evento, tipo il paper di mandalari con gli screeshoot generati tramite adb in precedenza, l'unico problema in questo caso e che non sia ha riscontro dello stato del device. Servirebbe una sorta di API di controllo o REST API di controllo da usare nel test -> inserisci quello che hai trovato su Github in merito con le API cloud trovate), oppure un altro workaround potrebbe essere quello di fare refresh nella home dell'app, e poi controllare lo stato del dispositivo (in questo modo cerchiamo di evitare il disallineamento tra stato in UI app e stato lato cloud del marchio che gestisce e che vende lo smart device. Saniamo questa inconsistenza). Altri possibili lavori futuri riguardano la containerizzazione dell'emulatore per piu' veloce replicabilita' e yaml file per file sorgenti .kt da generare in automatico in base ai dati raccolti in uiautomatorviewer. Strumenti automatici esistenti scartati dato che non ne abbiamo bisogno, dato che filtrano tutti i possibili eventi per scovare bug o problemi di stabilita' o soundness, noi abbiamo bisogno solo di alcuni eventi che consentono l'interazione smart device - app associati, e non tutti i possibili elementi selezionabili nell'app da testare.

# AWS INSTANCE
## TAPO TP-LINK
> nslookup tapo.tplinkcloud.com

Non-authoritative answer:
tapo.tplinkcloud.com	canonical name = d3utcvynanh8w7.cloudfront.net.
Name:	d3utcvynanh8w7.cloudfront.net
Address: 108.139.243.127
Name:	d3utcvynanh8w7.cloudfront.net
Address: 108.139.243.11
Name:	d3utcvynanh8w7.cloudfront.net
Address: 108.139.243.108
Name:	d3utcvynanh8w7.cloudfront.net
Address: 108.139.243.120

## EZVIZ
> nslookup euauth.ezvizlife.com

Non-authoritative answer:
euauth.ezvizlife.com	canonical name = ezvizlife-auth-16461422.eu-west-1.elb.amazonaws.com.
Name:	ezvizlife-auth-16461422.eu-west-1.elb.amazonaws.com
Address: 54.228.215.71
Name:	ezvizlife-auth-16461422.eu-west-1.elb.amazonaws.com
Address: 34.241.142.38

> tshark -r capture.pcap | grep -i ezvizlife
> tshark -r capture.pcap | grep tplinkcloud

UDP,TCP,TLSv.1.2,HTTP -> ok
DNS, MDNS, DHCP, ARP -> ko oppure DNS, MDNS e DHCP trattarli come UDP e filtrare via ARP packets.

` bash
os.system("tshark -r mirai.pcap -T fields -e ip.src -e frame.len -e ip.proto -E separator=, -E occurrence=f > traffic.csv")

tshark -r capture.pcap
tshark -r capture.pcap -Y 'ip.addr ' -T fields -e ip.addr 1>/dev/null

time tshark -r capture.pcap -t ud \
-Y 'ip.addr and tcp.srcport and eth.addr' \
-T fields -e _ws.col.Time -e eth.src -e ip.src \
-e eth.dst -e ip.dst -e tcp.srcport -e _ws.col.Protocol -e frame.len \
-E separator=, -E occurrence=f 2>/dev/null > traffic.csv


CAPTURE=( capture.pcap capture2.pcap capture3.pcap capture4.pcap )
TRAFFIC=( traffic.csv traffic2.csv traffic3.csv traffic4.csv )
for i in {1..4}; do tshark -r ../../linksysPcap/"${CAPTURE[i]}" -t ud -Y 'ip.addr and tcp.srcport and eth.addr' -T fields -e _ws.col.Time -e eth.src -e ip.src -e eth.dst -e ip.dst -e tcp.srcport -e _ws.col.Protocol -e frame.len -E separator=, -E occurrence=f 2>/dev/null > "${TRAFFIC[i]}"; done


# con dns name field
# /Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksysPcap
# /Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksysAnalysis/pcapSankey
CAPTURE=( capture.pcap capture1.pcap capture2.pcap capture3.pcap )
TRAFFIC=( traffic1.csv traffic2.csv traffic3.csv traffic4.csv )
for i in {1..4}; do tshark -r ../../linksysPcap/"${CAPTURE[i]}" -t ud -Y 'ip.addr and tcp.srcport and eth.addr' -T fields -e _ws.col.Time -e eth.src -e ip.src -e tcp.srcport -e eth.dst -e ip.dst -e tcp.dstport -e _ws.col.Protocol -e frame.len -e dns.qry.name -E separator=, -E occurrence=f 2>/dev/null > "${TRAFFIC[i]}"; done


# senza dns name field
# /Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksysPcap
# /Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksysAnalysis/pcapSankey
CAPTURE=( capture.pcap capture1.pcap capture2.pcap capture3.pcap )
TRAFFIC=( traffic1.csv traffic2.csv traffic3.csv traffic4.csv )
for i in {1..4}; do tshark -r ../../linksysPcap/"${CAPTURE[i]}" -t ud -Y 'eth.addr and ip.addr and tcp.dstport' -T fields -e _ws.col.Time -e eth.src -e ip.src -e tcp.srcport -e eth.dst -e ip.dst -e tcp.dstport -e _ws.col.Protocol -e frame.len -E separator=, -E occurrence=f 2>/dev/null > "${TRAFFIC[i]}"; done


# filter only 4 devices traffic based upon mac adress
# Here we will get also DNS, NTP, DHCP related to UDP protocol
#
# This csv would need a remap defining the protocol used and the port, so if TCP/TLSv1/TLSv1.2/TLSv1.3 then it will be used tcp.srcport and tcp.dstport, else if UDP/NTP/DNS/DHCP then it will be used udp.scrpot and udp.dstport, else we map eth.src to eth.dst to protocol skipping ports.
time tshark -r /Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksysPcap/capture.pcap -t ud -Y 'eth.addr==64:f2:fb:df:fb:e1 or eth.addr==64:f2:fb:48:2c:5b or eth.addr==00:5f:67:bf:09:ef or eth.addr==e8:48:b8:d6:a8:1d' -T fields -e _ws.col.Time -e eth.src -e ip.src -e udp.srcport -e tcp.srcport -e eth.dst -e ip.dst -e udp.dstport -e tcp.dstport -e _ws.col.Protocol -e frame.len -E separator=, -E occurrence=f 2>/dev/null > /Users/angelo/workspace/playground/sankey1.csv


# dns python name resolution
python3 -c "import socket; print(socket.gethostbyaddr('8.8.8.8')[0])"


# PROTOCOLLI USATI
> cat traffic.csv | awk '{ split($0,pino,","); print pino[5] }' | sort | uniq
ARP
DB-LSP-DISC/JSON
DHCP
DNS
HTTP
HTTP/JSON
HTTP/XML
ICMP
ICMPv6
MDNS
OCSP
QUIC
SSDP
SSH
SSL
TCP
TLSv1
TLSv1.2
TLSv1.3
UDP
XID

UDP, TCP, TLSv1.2, HTTP

UDP <- DNS, MDNS, DHCP, …
`

test

- dall'analisi filtra che i dispositivi ezviz sono piu' accurati e perdono meno tempo, c'e' meno delay mentre quelli Tapo hanno un delay.

# INCONTRO May, 18 2023
## PRESENTI: Fabio
- I grafici che ho generato finora solo comprensivi di traffico spontaneo e traffico degli eventi. La sfida adesso è quella di scindere le due sorgenti per plottarle su dei sankey diagram per analizzare quantitativamente la loro differenza (pacchetti scambiati, protocolli usati, etc...).
- Tapo smartplug P100 ha un delay tra traffico scambiato e eventi generati molto peculiare. A cosa puo' essere dovuto ???.
  E' sfasato temporalmente di 0.x secondi
- Nella parte di benchmarking, dato che ezviz smartplug era connesso ad un'altra rete (wifi polimi saltuaria) e non fu possibile cattutare il suo traffico scambiato, andremo a confrontare Tapo smartplub e Tapo smartbulb (diverso device a parita' di brand) + Tapo smartbulb e Ezviz smartbulb (stessa tipologia di device tra brand differenti ).
- Al momento abbiamo considerato nei sankey il traffico scambiato nella capture1.csv da 2.0 GB dato che il linksys andava a saturare la trace a questo valore. Questo valore pero' per noi e' poco significativo, dobbiamo estrarre l'orizzonte temporale di riferimento per le 4 trace di rete.
  Sempre per il sankey provare a fondere le 4 trace e fare un unico plot.
-> Per estrarre gli orizzonti temporali useremo l'utility cmd di Wireshark capinfos:

---------------------
capinfos capture.pcap
---------------------
File name:           capture.pcap
File type:           Wireshark/tcpdump/... - pcap
File encapsulation:  Ethernet
File timestamp precision:  microseconds (6)
Packet size limit:   file hdr: 262144 bytes
Number of packets:   3,057 k
File size:           2,048 MB
Data size:           1,999 MB
Capture duration:    69072.681900 seconds
First packet time:   2022-09-20 17:19:24.476804
Last packet time:    2022-09-21 12:30:37.158704
Data byte rate:      28 kBps
Data bit rate:       231 kbps
Average packet size: 653.81 bytes
Average packet rate: 44 packets/s
SHA256:              3a00b4991961368bb04dc6903886247f93280ca0694f6a6f56a2729b8b8f6b77
RIPEMD160:           cda9bd151c209821596996945cfb035e35bc0dce
SHA1:                56023d360e866005fd47588de2258d88bd272236
Strict time order:   False
Number of interfaces in file: 1
Interface #0 info:
                     Encapsulation = Ethernet (1 - ether)
                     Capture length = 262144
                     Time precision = microseconds (6)
                     Time ticks per second = 1000000
                     Number of stat entries = 0
                     Number of packets = 3057574

----------------------
capinfos capture1.pcap
----------------------
File name:           capture1.pcap
File type:           Wireshark/tcpdump/... - pcap
File encapsulation:  Ethernet
File timestamp precision:  microseconds (6)
Packet size limit:   file hdr: 262144 bytes
Number of packets:   2,868 k
File size:           2,048 MB
Data size:           2,002 MB
Capture duration:    90654.061987 seconds
First packet time:   2022-09-21 12:30:37.172284
Last packet time:    2022-09-22 13:41:31.234271
Data byte rate:      22 kBps
Data bit rate:       176 kbps
Average packet size: 697.98 bytes
Average packet rate: 31 packets/s
SHA256:              31262f0f4bbccdcf6cea6d706030c8896eccd1707b34a9a9feed75d6940d77ca
RIPEMD160:           f9ea18f9d85a21a0290fed26d44327a72ef11468
SHA1:                09a000797c0e940f7bc24ba6d6eb3705e0d73d94
Strict time order:   False
Number of interfaces in file: 1
Interface #0 info:
                     Encapsulation = Ethernet (1 - ether)
                     Capture length = 262144
                     Time precision = microseconds (6)
                     Time ticks per second = 1000000
                     Number of stat entries = 0
                     Number of packets = 2868417

----------------------
capinfos capture2.pcap
----------------------
File name:           capture2.pcap
File type:           Wireshark/tcpdump/... - pcap
File encapsulation:  Ethernet
File timestamp precision:  microseconds (6)
Packet size limit:   file hdr: 262144 bytes
Number of packets:   2,721 k
File size:           2,048 MB
Data size:           2,004 MB
Capture duration:    14642.690737 seconds
First packet time:   2022-09-22 13:41:31.234278
Last packet time:    2022-09-22 17:45:33.925015
Data byte rate:      136 kBps
Data bit rate:       1,095 kbps
Average packet size: 736.40 bytes
Average packet rate: 185 packets/s
SHA256:              a651fe80d25b1397992213f649e58fe24e2611395cc4324431254be331efecd0
RIPEMD160:           17eba13cdb6e08ba2e99a740890fc58022c63bae
SHA1:                fc2942690a6c698256360689196c69b81e24fe9e
Strict time order:   False
Number of interfaces in file: 1
Interface #0 info:
                     Encapsulation = Ethernet (1 - ether)
                     Capture length = 262144
                     Time precision = microseconds (6)
                     Time ticks per second = 1000000
                     Number of stat entries = 0
                     Number of packets = 2721964

----------------------
capinfos capture3.pcap
----------------------
File name:           capture3.pcap
File type:           Wireshark/tcpdump/... - pcap
File encapsulation:  Ethernet
File timestamp precision:  microseconds (6)
Packet size limit:   file hdr: 262144 bytes
Number of packets:   680 k
File size:           583 MB
Data size:           572 MB
Capture duration:    9648.013583 seconds
First packet time:   2022-09-22 17:45:33.925034
Last packet time:    2022-09-22 20:26:21.938617
Data byte rate:      59 kBps
Data bit rate:       474 kbps
Average packet size: 840.37 bytes
Average packet rate: 70 packets/s
SHA256:              adc2eaf99c3c468c51e6fab5f787ff75afea9b594f370c96519e1a4da19fb9ef
RIPEMD160:           d7ec31b6382f0c4e0f83f96c758aa1b36af3fa69
SHA1:                b1f4ae34a2ebbb8091f34b883cdc5acf581e6c83
Strict time order:   True
Number of interfaces in file: 1
Interface #0 info:
                     Encapsulation = Ethernet (1 - ether)
                     Capture length = 262144
                     Time precision = microseconds (6)
                     Time ticks per second = 1000000
                     Number of stat entries = 0
                     Number of packets = 680945

- /Users/angelo/workspace/playground/sankey.csv contiene i dati di tutte 4 le trace di rete (capture.pcap e capture[123].pcap) generato con il seguente comando
`
tshark -r /Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksysPcap/capture.pcap -t ud -Y 'eth.addr==64:f2:fb:df:fb:e1 or eth.addr==64:f2:fb:48:2c:5b or eth.addr==00:5f:67:bf:09:ef or eth.addr==e8:48:b8:d6:a8:1d' -T fields -e _ws.col.Time -e eth.src -e ip.src -e udp.srcport -e tcp.srcport -e eth.dst -e ip.dst -e udp.dstport -e tcp.dstport -e _ws.col.Protocol -e frame.len -E separator=, -E occurrence=f 2>/dev/null > /Users/angelo/workspace/playground/sankey.csv

tshark -r /Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksysPcap/capture1.pcap -t ud -Y 'eth.addr==64:f2:fb:df:fb:e1 or eth.addr==64:f2:fb:48:2c:5b or eth.addr==00:5f:67:bf:09:ef or eth.addr==e8:48:b8:d6:a8:1d' -T fields -e _ws.col.Time -e eth.src -e ip.src -e udp.srcport -e tcp.srcport -e eth.dst -e ip.dst -e udp.dstport -e tcp.dstport -e _ws.col.Protocol -e frame.len -E separator=, -E occurrence=f 2>/dev/null >> /Users/angelo/workspace/playground/sankey.csv

tshark -r /Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksysPcap/capture2.pcap -t ud -Y 'eth.addr==64:f2:fb:df:fb:e1 or eth.addr==64:f2:fb:48:2c:5b or eth.addr==00:5f:67:bf:09:ef or eth.addr==e8:48:b8:d6:a8:1d' -T fields -e _ws.col.Time -e eth.src -e ip.src -e udp.srcport -e tcp.srcport -e eth.dst -e ip.dst -e udp.dstport -e tcp.dstport -e _ws.col.Protocol -e frame.len -E separator=, -E occurrence=f 2>/dev/null >> /Users/angelo/workspace/playground/sankey.csv

tshark -r /Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksysPcap/capture3.pcap -t ud -Y 'eth.addr==64:f2:fb:df:fb:e1 or eth.addr==64:f2:fb:48:2c:5b or eth.addr==00:5f:67:bf:09:ef or eth.addr==e8:48:b8:d6:a8:1d' -T fields -e _ws.col.Time -e eth.src -e ip.src -e udp.srcport -e tcp.srcport -e eth.dst -e ip.dst -e udp.dstport -e tcp.dstport -e _ws.col.Protocol -e frame.len -E separator=, -E occurrence=f 2>/dev/null >> /Users/angelo/workspace/playground/sankey.csv
`

- /Users/angelo/workspace/playground/sankey1.csv contiene i dati di capture.pcap
`
tshark -r /Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksysPcap/capture.pcap -t ud -Y 'eth.addr==64:f2:fb:df:fb:e1 or eth.addr==64:f2:fb:48:2c:5b or eth.addr==00:5f:67:bf:09:ef or eth.addr==e8:48:b8:d6:a8:1d' -T fields -e _ws.col.Time -e eth.src -e ip.src -e udp.srcport -e tcp.srcport -e eth.dst -e ip.dst -e udp.dstport -e tcp.dstport -e _ws.col.Protocol -e frame.len -E separator=, -E occurrence=f 2>/dev/null > /Users/angelo/workspace/playground/sankey1.csv
`

- /Users/angelo/workspace/playground/sankey2.csv contiene i dati di capture1.pcap
`
tshark -r /Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksysPcap/capture1.pcap -t ud -Y 'eth.addr==64:f2:fb:df:fb:e1 or eth.addr==64:f2:fb:48:2c:5b or eth.addr==00:5f:67:bf:09:ef or eth.addr==e8:48:b8:d6:a8:1d' -T fields -e _ws.col.Time -e eth.src -e ip.src -e udp.srcport -e tcp.srcport -e eth.dst -e ip.dst -e udp.dstport -e tcp.dstport -e _ws.col.Protocol -e frame.len -E separator=, -E occurrence=f 2>/dev/null > /Users/angelo/workspace/playground/sankey2.csv
`

- /Users/angelo/workspace/playground/sankey3.csv contiene i dati di capture2.pcap
`
tshark -r /Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksysPcap/capture2.pcap -t ud -Y 'eth.addr==64:f2:fb:df:fb:e1 or eth.addr==64:f2:fb:48:2c:5b or eth.addr==00:5f:67:bf:09:ef or eth.addr==e8:48:b8:d6:a8:1d' -T fields -e _ws.col.Time -e eth.src -e ip.src -e udp.srcport -e tcp.srcport -e eth.dst -e ip.dst -e udp.dstport -e tcp.dstport -e _ws.col.Protocol -e frame.len -E separator=, -E occurrence=f 2>/dev/null > /Users/angelo/workspace/playground/sankey3.csv
`

- /Users/angelo/workspace/playground/sankey4.csv contiene i dati di capture3.pcap
`
tshark -r /Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksysPcap/capture3.pcap -t ud -Y 'eth.addr==64:f2:fb:df:fb:e1 or eth.addr==64:f2:fb:48:2c:5b or eth.addr==00:5f:67:bf:09:ef or eth.addr==e8:48:b8:d6:a8:1d' -T fields -e _ws.col.Time -e eth.src -e ip.src -e udp.srcport -e tcp.srcport -e eth.dst -e ip.dst -e udp.dstport -e tcp.dstport -e _ws.col.Protocol -e frame.len -E separator=, -E occurrence=f 2>/dev/null > /Users/angelo/workspace/playground/sankey4.csv
`

#### IOT FORENSICS SANKEY UNSW UNIVERSITY ANALYSIS EXAMPLE
https://iotanalytics.unsw.edu.au/profiles.html
 
# ISSUE TO RESOLVE
In fase di creazione dei sankey nel caso abbiamo porta sorgente e destinazione che si ripetono abbiamo un un problema in fase di creazione della map che tiene traccia degli indici.

0	1				2			3	4		5	6	7	8
11224	2022-09-21 17:55:19.799026	64:f2:fb:df:fb:e1	53	192.168.2.1	57345	ICMP	70	192.168.2.1
12000	2022-09-21 18:25:24.256858	64:f2:fb:df:fb:e1	63482	192.168.2.1	53	DNS	81	192.168.2.1

In questo caso la porta 53 verrebbe mappata una sola volta creando un loop nel sankey, cosa che dobbiamo evitare. Come???? Dovremmo creare uno snippet in grado di distinguere tra porta sorgente 53 e porta destinazione 53 e associare ad ognuna un indice da mappare nel sankey differente (Questo comportamento inusuale e' stato riscontrato nel traffico verso il default gateway 192.168.2.1 usato in lab come sniffer.
[ OK ] - issue resolved with multi-map to manage the indexes, one for each piece of the sankey node src/dst.

% percentage computed over the number of packets.
LB1
ALL 33808 (3256882 B ~ 3.11 MB)
- OUTGOING 16379 (1610224 B ~ 1.54 MB)
- INCOMING 17429 (1646658 B ~ 1.57 MB)
SPONTANEOUS 25509 ($75.45\%$) (2408929 B ~ 2.3 MB)
- OUTGOING 12549 (1204392 B ~ 1.15 MB)
- INCOMING 12960 (1204537 B ~ 1.15 MB)
EVENTS 8299 ($24.55\%$) (847953 B ~ 0.81 MB)
- OUTGOING 3830 (405832 B ~ 0.39 MB)
- INCOMING 4469 (442121 B ~ 0.42 MB)

L530E
ALL 15610 (2321007 B ~ 2.21 MB)
- OUTGOING 8983 (1306301 B ~ 1.25 MB)
- INCOMING 6627 (1014706 B ~ 0.97 MB)
SPONTANEOUS 7330 ($46.96\%$) (1058114 B ~ 1.01 MB)
- OUTGOING 4222 (595473 B ~ 0.57 MB)
- INCOMING 3108 (462641 B ~ 0.44 MB)
EVENTS 8280 ($53.04\%$) (1262893 B ~ 1.2 MB)
- OUTGOING 4761 (710828 B ~ 0.68 MB)
- INCOMING 3519 (552065 B ~ 0.53 MB)

P100
TOTAL 23418 (5633911 ~ 5.37 MB)
- OUTGOING 13273 (3024658 B ~ 2.88 MB)
- INCOMING 10145 (2609253 B ~ 2.49 MB)
SPONTANEOUS 13985 ($59.72\%$) (3423816 B ~ 3.27 MB)
- OUTGOING 7952 (1811833 B ~ 1.73 MB)
- INCOMING 6033 (1611983 B ~ 1.54 MB)
EVENTS 9433 ($40.28\%$) (2210095 B ~ 2.10 MB)
- OUTGOING 5321 (1212825 B ~ 1.15 MB)
- INCOMING 4112 (997270 B ~ 0.95 MB)
