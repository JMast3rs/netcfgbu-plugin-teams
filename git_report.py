
import pymsteams

teams_webhook_url = "<< Insert Teams Webhook URL>>"

teams_git_repository_url = "<< Insert GitLab Repo URL (without .git) >>"
teams_git_repository_id =  "<< Insert GitLab Repo ID >>"
teams_git_token = "<< Insert GitLab Access Token >>"

class Teams_Git(Plugin):
    name = "Teams_Git"

    def git_report(success, tag_name):
        message = pymsteams.connectorcard(teams_webhook_url_vcs)

        if success:

            res = requests.get(f"https://gitlabs.com/api/v4/projects/{teams_git_repository_id}/repository/tags?private_token={teams_git_token}").json()
            previous_repo = res[1]["name"]

            message.title("Configuration Change Detected")
            message.text("Successfully pushed to git.")
            message.addLinkButton("View Config", f"{teams_git_repository_url}/-/tree/{tag_name}")
            message.addLinkButton("View Changes", f"{teams_git_repository_url}/-/compare/{previous_repo}...{tag_name}")
            message.color("#4EE73C")
            message.send()

            print(f"Previous Config Tag: {previous_repo}, New Config Tag: {tag_name}")

        else:
            message.title("No Configureation Change Detected")
            message.text("Skipping git push.")
            message.send()