# MS Teams & GitLab intergration for `netcfgbu`


## About The Project

This project expands on the work by [@minitriga](https://github.com/minitriga) for [`netcfgbu (0.8.0)`](https://github.com/jeremyschulman/netcfgbu) which enables the creation of plugins. These `python` plugins can be used to create extra functionality. In my case I made a plugin which integrates with MS Teams. The reason for this is because Teams is the primary messaging tool at my company. This allows me to have multiple people to be alerted to a backup and any problems that it may have. Or to keep a log of when it was ran and the results.

**Notification of Device Backups (by using `backup_report.py`)**
![](https://james.masters.bio/files/github/images/image1.PNG)
![](https://james.masters.bio/files/github/images/image3.PNG)

**Notification of Git Push (by using `git_report.py`)**
![](https://james.masters.bio/files/github/images/image2.PNG)
![](https://james.masters.bio/files/github/images/image4b.PNG)

## Requirements

 **Needed for `backup_report.py`**

This plugin requires the uses of Teams Incoming Webhooks. This guide [here](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook) shows how to get the required webhook URL that is needed. This is all that is need from Teams.

A `python` library called `pymsteams` is need and instruction on how to install are found [here](https://pypi.org/project/pymsteams/).

Optionally if you are **not** using `git_report.py` or `GitLab` then this is all that is need for `backup_report.py`. 

 **Needed for `git_report.py`**

If you want to implement `git_report.py` then the following information is needed.

- The GitLab repository URL. Example (https://gitlab.com/john.doe/netcfgbu-backups)
- The GitLab repository ID. Can be found under the name on main repository page.
- The GitLab User Access Token. This is can be found [here](https://gitlab.com/-/profile/personal_access_tokens).


## Setup

The `netcfgbu` plugins need to be placed in a specified folder which is configured in `netcfgbu.toml`. This is described on the `netcfgbu` GitHub [here](https://github.com/jeremyschulman/netcfgbu).

 **The following lines need to be filled with the correct information.**
 
 **For `backup_report.py`**
```python
teams_webhook_url = "<< Insert Teams Webhook URL>>"
```

**For `git_report.py`**
```python
teams_webhook_url = "<< Insert Teams Webhook URL>>"

teams_git_repository_url = "<< Insert GitLab Repo URL (without .git) >>"
teams_git_repository_id =  "<< Insert GitLab Repo ID >>"
teams_git_token = "<< Insert GitLab Access Token >>"
```
Once the files are in the plugins folder of your `netcfgbu` instance the `backup_report.py` script will be ran when a backup is take. The `git_report.py` will be ran when then `netcfgbu vcs save` command is used.
