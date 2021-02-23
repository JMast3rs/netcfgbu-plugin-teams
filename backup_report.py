
import pymsteams

teams_webhook_url = "<< Insert Teams Webhook URL>>"

class Teams_Backup(Plugin):
    name = "Teams_Backup"

    def report(report):
        message = pymsteams.connectorcard(teams_webhook_url_backup)
        report_dic = dict(report.task_results)

        message.title("Configurtion Backup Report")
        message.text("Configurtion Backup Report")
        messageSection = pymsteams.cardsection()

        for suc in report_dic[True]:
            messageSection.addFact(str(suc[0]["host"]), "Successful!")

        for unsuc in report_dic[False]:
            messageSection.addFact(str(unsuc[0]["host"]), str(unsuc[1]))

        message.addSection(messageSection)
        message.send()

        if len(report_dic[False]) > 0:
            message = pymsteams.connectorcard(teams_webhook_url_backup)
            message.title("Configurtion Backup Failures!")
            message.text("Configurtion Backup Failures!")
            message.color("E74C3C")

            messageSection = pymsteams.cardsection()

            for unsuc in report_dic[False]:
                messageSection.addFact(str(unsuc[0]["host"]), str(unsuc[1]))

            message.addSection(messageSection)
            message.send()
