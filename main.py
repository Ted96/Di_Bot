from TextApp import TextAppDiscord


def dostuff():
    pass


def main():
    # initialize everything
    # df_nlu = ChatbotService('wtfdoitypehere')
    intent = "Course-Grade"
    value = "Physics"
    # An rwthsei gia to faq
    if (intent == "faq"):
        # input: None
        # Fere to tis erwthseis h tis apanthseis me vash to faq
        # output: The Questions And The Answers
        dostuff()
    # alliws an rwthsei kapoion va8mo se kapoio ma8hma
    elif (intent == "MyStudies-CourseGrade"):
        # input: Course (i.e: Psychics)
        # Kane login sto my-studies kai fere ton va8mo gia ayto to ma8hma
        # output: Course Grade
        dostuff()
    elif (intent == "MyStudies-CoursesDeclaration"):
        # input: None
        # Kane login sto my-studies kai fere tis dhlwseis gia to trexon e3amhno
        # output: Course Declarations
        dostuff()
    elif (intent == "Eclass-Announcements"):
        # input: None
        # Kane login sto eclass kai fere ta anoucements gia ola, h ena ma8hma
        # output: Top 5 most recent announcements?
        dostuff()
    elif (intent == "Eclass-Deadline"):
        # input: Course
        # Kane login sto eclass kai fere to deadline gia tis ergasies enos ma8hmatos
        # output: Course Deadline
        dostuff()
    elif (intent == "Kati allo me to di.uoa.gr"):
        # Px fere tis argeies, h ta ma8hmata ana e3amhno
        dostuff()
    pass


dc_bot = TextAppDiscord()

for text in dc_bot.run():
    print('------>', text)

print('------- END MAIN ----------')

if __name__ == '__main__':
    main()

    # message = 	dc.message
    # intent = 	df.ask( message )
    # answer = 	formulate_answer( intent )
    # dc.sendbackto( author , answer)
    #
    #
    #
    #
    # #
    # if intent:
    # 	pass
    # 	wb = webparser()
    # 	ergasies = wb.getelement_ergasies
    # 	return ergasies
    # elif intent:
    # 	pass
    # elif intent:
    # 	pass
