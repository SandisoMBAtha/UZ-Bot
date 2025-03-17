import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import time
class SplashScreen(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        loadUi("newsplashh.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        label = QLabel(self)
        pixmap = QPixmap("Screenshot 2023-09-03 105348.png")
        label.setPixmap(QPixmap("Screenshot 2023-09-03 105348.png"))
        label.setScaledContents(True)
        label.setSizePolicy(50, 50)
        label.setPixmap(pixmap)
        label.move(100, 60)
        label.resize(100, 100)
        self.centralWidget()
        self.resize(300,430)
        self.status.setText('Initializing')

    def progressbar(self):
        for i in range(100):
          self.progressBar.setValue(i)
          app.processEvents()
          time.sleep(0.08)

class LowConfidenceException(Exception):
    pass
class MainPage(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        loadUi("chat.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        label = QLabel(self)
        pixmap = QPixmap("Screenshot 2023-09-03 105348.png")
        pixmap = pixmap.scaled(50, 50, 50, 10)
        label.setPixmap(QPixmap("Screenshot 2023-09-03 105348.png"))
        label.setScaledContents(True)
        label.setSizePolicy(50, 50)
        label.move(90, -15)
        label.resize(100, 100)
        self.centralWidget()
        self.resize(400, 400)
        self.plainTextEdit.setStyleSheet("color: white;")

        self.keyword_responses = {
            "hello": "Hello!",
            "sawbona": "Yebo unjn, Ngiwumsizi wakho mayelana no Lwazi ongase uludinge nge University of Zululand",
            "hello":"Greetings",
            "Greetings":"Hello",
            "how are you": "I'm just a computer program, but I'm here to assist you.",

            "security": "Safety and security of the University of Zululand’s campus community is the primary responsibility of PSD. The Department aims to ensure a safe and secure environment on campus in which quality teaching, learning and research can be done. The Department provides a seven day, 24-hour patrol and guarding service on the campuses, residences. The Department also has ten (10) Student Crime Prevention Officers who assist with and report any problems in the residences and University functions."
                         " crime prevention techniques and tactics, CCTV surveillance, marking of University property, crime intelligence system to get forewarning of potential problems",

            "safety" :" Safety and security of the University of Zululand’s campus community is the primary responsibility of PSD. The Department aims to ensure a safe and secure environment on campus in which quality teaching, learning and research can be done. The Department provides a seven day, 24-hour patrol and guarding service on the campuses, residences. The Department also has ten (10) Student Crime Prevention Officers who assist with and report any problems in the residences and University functions."
                         " crime prevention techniques and tactics, CCTV surveillance, marking of University property, crime intelligence system to get forewarning of potential problems",

            " commerce":"Commerce, Administration and Law , The Faculty of Commerce, administration and law (Henceforth FCAL) is headed by the dean Professor Lorraine Greyling and comprises 5 academic departments, namely: "
                          "Accounting & Auditing[3] (including Information Systems) which headed by Professor M Livingstone CA (SA) Department of Business Management[4] (incorporating Human Resources Management) which is headed by N Vezi-Magigaba Department of Economics,[5] headed by Professor I Kaseeram Department of Public Administration,[6] headed by NM Jili Department of law[7] (Private law, Public law and Criminal & Procedural law) Which is headed by K Naidoo The Faculty participates avidly in community outreach and development programmes. The Faculty website : http://www.fcal.unizulu.ac.za/ ",

            "education":"Education The faculty consists of six departments, namely, Comparative and Science of Education, Curriculum and Instruction Studies, Educational Planning and Administration, Educational Psychology and Foundations of Education",
             "science   ":"Engineering, Science and AgricultureThe Faculty of Science and Agriculture offers various Science Programmes within the departments of Agriculture, Biochemistry and Microbiology, Botany, Chemistry, Computer Science, Consumer Science, Geography and Environmental Studies, Human Movement Sciences, Hydrology, Mathematical Science, Nursing, Physics and Engineering, Science Foundation and Zoology.",

            " humanities ": "Humanities & Social Sciences The Faculty of Arts[8] is the largest faculty within the institution and boasts 16 departments. The Faculty is headed up by the dean, Professor MA Masoga Anthropology and development studies Communication science Creative Arts English General Linguistics and modern languages Geography and environmental studies History",

            "tuition ":"Fees are charged per module on a semester basis for undergraduate students.Tuition fees include laboratory and examination fees (excluding re-examination fees), librarysubscriptions, student facilities and personal accident insurance. Charges relating to theprovision of additional material, e.g. supplementary/lecture notes, field trips, practical fees,where applicable, will be raised separately, depending on the particular modules for whichstudents are registered. Prescribed text books are explicitly excluded from the tuition fees",

            "housing": "The University has on-campus (KwaDlangezwa) and off campus residences,provided by various external service providers that meet the minimum requirementsas prescribed by the University. The cost of accommodation provided by externalservice providers is charged to the respective student’s account. On-campusresidence costs vary from an average of R8,599 to R28,522 in the 2020 academic year.",
            "residence":"The University has on-campus (KwaDlangezwa) and off campus residences,provided by various external service providers that meet the minimum requirementsas prescribed by the University. The cost of accommodation provided by externalservice providers is charged to the respective student’s account. On-campusresidence costs vary from an average of R8,599 to R28,522 in the 2020 academic year.",
            "funding": "An award letter, addressed to the University, should be obtained from each sponsor on an official letterhead and company stamp with the relevant signature, confirmingthe details of the award (i.e. tuition, books, meals, etc.) and the amount of funding,clearly indicating that the funds will be paid TO THE UNIVERSITY (NOT THESTUDENT).This must be submitted to the Student Financial Aid Officesat least two (2) days prior to Registration for early financial clearance.",
            "bursary": "An award letter, addressed to the University, should be obtained from each sponsor on an official letterhead and company stamp with the relevant signature, confirmingthe details of the award (i.e. tuition, books, meals, etc.) and the amount of funding,clearly indicating that the funds will be paid TO THE UNIVERSITY (NOT THESTUDENT).This must be submitted to the Student Financial Aid Officesat least two (2) days prior to Registration for early financial clearance.",
            "nsfas": "The National Student Financial Aid Scheme (NSFAS) is a public entity reporting to the Department of Higher Education and Training. NSFAS provides financialassistance in the form of a study bursary to qualifying students who wish to studyor are already studying at TVET colleges and public universities"
               "Applicants who are approved for NSFAS funding are covered for the following  Registration Tuition Allowances for:• Food• Accommodation or transport• Learning material Personal care",
            "finance": "The National Student Financial Aid Scheme (NSFAS) is a public entity reporting to the Department of Higher Education and Training. NSFAS provides financialassistance in the form of a study bursary to qualifying students who wish to studyor are already studying at TVET colleges and public universities"
                     "Applicants who are approved for NSFAS funding are covered for the following  Registration Tuition Allowances for:• Food• Accommodation or transport• Learning material Personal care",

            "accomodation": "UNIZULU provides home-away-from-home suitable accommodation both on campus and privately rented accommodation. We provide both mixed residences as well gender dedicated residences.The Student Housing section provides accessible, affordable, safe and healthy environment that is conducive to learning. Both registered and returning studentsmay apply for accommodation via an online self-service platform at a date announced by the department each year. Successful applications for residence are subject to the residence placement criteria ",
            "housing": "UNIZULU provides home-away-from-home suitable accommodation both on campus and privately rented accommodation. We provide both mixed residences as well gender dedicated residences.The Student Housing section provides accessible, affordable, safe and healthy environment that is conducive to learning. Both registered and returning studentsmay apply for accommodation via an online self-service platform at a date announced by the department each year. Successful applications for residence are subject to the residence placement criteria",

            "sport ": "Sports and recreation Sports and Recreation is governed by the Student Services Department which carries out some of the co-curricular services that aim at contributing towards total personal student development and advancement. There are 23 sports codes classified as indoor and outdoor.Indoor sports include aerobics, basketball, bodybuilding, boxing, chess, dance, judo, karate, pool, squash, and table tennis.Outdoor sports include athletics, cricket, hiking, hockey, netball, rowing, rugby, soccer (men and women), softball, swimming, tennis, and volleybal",
            "recreaction ": "Sports and recreation Sports and Recreation is governed by the Student Services Department which carries out some of the co-curricular services that aim at contributing towards total personal student development and advancement. There are 23 sports codes classified as indoor and outdoor.Indoor sports include aerobics, basketball, bodybuilding, boxing, chess, dance, judo, karate, pool, squash, and table tennis.Outdoor sports include athletics, cricket, hiking, hockey, netball, rowing, rugby, soccer (men and women), softball, swimming, tennis, and volleybal",
            "registration":"Students typically apply for admission to UNIZULU through an online application portal.After reviewing applications, UNIZULU sends admission offers to eligible candidates. These offers may be conditional on meeting certain requirements.Students who receive admission offers must formally accept the offer through the university's admission portal or by submitting the required documents.Students need to pay the required registration and tuition fees. The university provides details on fee payment methods and deadlines.Financial aid and scholarship applications, if applicable, should be submitted.After completing all necessary steps, students receive confirmation of their registration status.",
            "rules":"The policy intends to provide guidelines and direction to the University of Zululand (UNIZULU) regarding the rules and procedures to be followed in the implementationof work integrated learning (WIL). It will also ensure that those University structures that are responsible for implementation of this policy are identified.APPROVAL AUTHORITY,SCOPE AND APPLICATION, procedures:MPLEMENTAION AND OVERSIGHT RESPONSIBILITIES , POLICY REVIEW,RISK MANAGEMENT, RESPONSIBILITY OF STUDENTS UNDERTAKING WIL, RESPONSIBILITY OF AN ACADEMIC WHO COORDINATE/ SUPERVISE WIL INCLUDING COMMUNITY AND INDUSTRY PARTNERS    ",
            "imithetho":"Lo mgomo uhlose ukuhlinzeka ngemihlahlandlela nesiqondiso eNyuvesi yaseZululand(UNIZULU) mayelana nemithetho nezinqubo okumele zilandelwe ekuqalisweni kokufunda okudidiyelwe komsebenzi(WIL).Izoqinisekisa futhi ukuthi lezo zinhlaka zeNyuvesi ezibhekele ukuqaliswa kwale  nqubomgomo ziyahlonzwa.IGUNYA LOKUVUMA, Ububanzi KANYE NESICELO, izinqubo: UKUSEBENZA KANYE  NEZIBOPHO ZOKUQAPHELA, UKUBUYEKEZWA KWENQUBOMGOMO, UKULAWULWA KOBUNGOZI, ISIBOPHO SABAFUNDI ABENZA IMISEBENZI, UMSEBENZIWONKE.",

            "ukubhalisela":"Abafundi ngokuvamile bafaka izicelo zokwamukelwa e-UNIZULU ngengosi yezicelo eku inthanethi. Ngemva kokubuyekeza izicelo, i-UNIZULU ithumela izicelo zokwamukelwa kwabafanelekayo. Lokhu kunikezwa kungase kube nemibandela yokuhlangabezana nezimfuneko ezithile. Abafundi abathola izicelo zokwamukelwa kufanele bakwamukele ngokusemthethweni lokho okunikezwayo ngengosi yokwamukelwa kwenyuvesi noma ngokuletha imibhalo edingekayo.Abafundi kudingeka bakhokhe imali edingekayo yokubhalisa kanye nemali yokufunda. Inyuvesi inikeza imininingwane yezindlela zokukhokha izimali kanye nezinsuku zokugcina.Usizo lwezezimali kanye nezicelo zezifundo, uma zikhona, kufanele zithunyelwe.Ngemva kokuqeda zonke izinyathelo ezidingekayo, abafundi bathola isiqinisekiso sesimo sabo sokubhalisa.",
            "ezemidlalo": "Ezemidlalo nokuNgcebeleka Ezemidlalo Nokuzijabulisa zibuswa uMnyango Wezinkonzo Zabafundi owenza ezinye zezinhlelo zezifundo ezihlose ukufaka isandla ekuthuthukisweni nasekuthuthukisweni komfundi. Kunamakhodi ezemidlalo angama-23 ahlukaniswa njengasendlini yasendlini. .Ezemidlalo zasendlini zihlanganisa i-aerobics, i-basketball, ukwakha umzimba, isibhakela, i-chess, umdanso, i-judo, i-karate, i-pool, i-squash, ne-table tennis.Ezemidlalo zangaphandle zihlanganisa ukugijima, ikhilikithi, ukukhuphuka, i-hockey, i-netball, ukugwedla, i-rugby, ibhola lezinyawo (abesilisa nabesifazane)",

            "indawoyokuhlala": "I-UNIZULU ihlinzeka ngendawo yokuhlala efanelekile ekhaya-kude nasekhaya ekhampasi naseziqashwe ngasese. Sihlinzeka ngezindawo zokuhlala ezixubile kanye nezindawo zokuhlala ezizinikele ngobulili. .Ingxenye Yezindlu Zabafundi inikeza indawo efinyelelekayo, ethengekayo, ephephile nenempilo evumela ukufunda. Bobabili abafundi ababhalisiwe nababuyayo bangafaka isicelo sendawo yokuhlala besebenzisa inkundla yokuzisiza eku-inthanethi ngosuku olumenyezelwe umnyango unyaka ngamunye.",
            "nSFAS": "I-National Student Financial Aid Scheme (NSFAS) iyinhlangano yomphakathi ebika eMnyangweni wezeMfundo ePhakeme Nokuqeqesha. I-NSFAS inikeza usizo lwezezimali ngohlobo lomfundaze wokufunda kubafundi abafanelekile abafisa ukufunda asebefunda e-TVET Abafake izicelo abagunyazwe uxhaso lwe - NSFAS bakhaviwe ngalezi Izibonelelo Zokubhalisa Zokubhalisa ezilandelayo:• Ukudla• Indawo yokuhlala noma izinto zokuhamba• Izinto zokufunda Ukunakekelwa komuntu siqu",

           "ezokuphepha": "Ukuphepha nokuvikeleka komphakathi wekhempasi yaseNyuvesi yaseZululand kuwumsebenzi oyinhloko we-PSD. UMnyango uhlose ukuqinisekisa indawo ephephile nevikelekile esikhungweni lapho ukufundisa, ukufunda nokucwaninga okuseqophelweni kungenziwa khona. Mnyango uhlinzeka ngezinsuku eziyisikhombisa, amahora angama-24 wokugada kanye nokuqapha emakhempasini, ezindaweni zokuhlala, UMnyango futhi unamaPhoyisa ayishumi (10) aBafundi Avimbela Ubugebengu asiza futhi abike noma yiziphi izinkinga ezindaweni zokuhlala nemisebenzi yaseNyuvesi." "Ukuvimbela ubugebenguamasu namaqhinga okunqanda ubugebengu, ukugadwa kwe-CCTV, ukumaka impahla yeNyuvesi, uhlelo lwezobunhloli bobugebengu ukuze uthole isexwayiso ngezinkinga ezingase zibe khona.",
            "ezezimali": "INational Student Financial Aid Scheme (NSFAS) iyinhlangano yomphakathi ebika eMnyangweni Wezemfundo Ephakeme Nokuqeqesha, i-NSFAS ihlinzeka ngosizo lwezimali ngohlobo lomfundaze wokufunda kubafundi abafanelekile abafisa ukufunda asebefunda emakolishi e-TVET nasemanyuvesi omphakathi.Abafakizicelo abagunyazwe uxhaso lwe-NSFAS bakhaviwe ngalezi Izibonelelo Zokubhalisa Zokubhalisa ezilandelayo:• Ukudla• Indawo yokuhlala noma izinto zokuhamba• Izinto zokufunda Ukunakekelwa komuntu siqu",
        }



    def Response(self):
       Question = self.textEdit.toPlainText()
       for keyword, response in self.keyword_responses.items():
           if keyword in Question.lower():
               self.plainTextEdit.appendPlainText("YOU : " + Question + "\n""\n")
               self.plainTextEdit.appendPlainText("BOT : " + response + "\n""\n")
               self.plainTextEdit.setReadOnly(True)
               self.textEdit.clear()
               self.show()
               return



       if Question.strip() == "":
               self.plainTextEdit.appendPlainText("YOU : " + Question + "\n""\n")
               self.plainTextEdit.appendPlainText("BOT : " + "Ask me any question about uniZulu" + "\n""\n")

       elif Question == 'exit':
               self.plainTextEdit.appendPlainText("BOT : " + "Goodbye see you soon" + "\n""\n")
               sys.exit(app.exec())


       elif keyword != Question.lower() :
               self.plainTextEdit.appendPlainText("YOU : " + Question + "\n""\n")
               self.plainTextEdit.appendPlainText(
                   "BOT : " + " Oops sorry i cannot find the answer you are looking for I'm still working on it" + "\n""\n")


       self.plainTextEdit.setReadOnly(True)
       self.textEdit.clear()
       self.show()

    def button(self):
      self.pushButton.clicked.connect(self.Response)
      self.show()

    def text(self):
        self.textEdit.setPlaceholderText("Welcome ask questions here")
        self.textEdit.clear()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    splash.progressbar()

    main = MainPage()
    main.button()
    main.text()
    main.show()
    splash.close()
    sys.exit(app.exec())
